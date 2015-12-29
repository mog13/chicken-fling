import sys
import socket
import select
import json
import logging

from app.Command import Command
from app.World import World
from app.Position import Position
from app.exceptions.InvalidMove import InvalidMove
from app.exceptions.InvalidPlayer import InvalidPlayer
from app.exceptions.OutOfAmmo import OutOfAmmo


class Server():
    """
    This class is simply setting up the connections and
    """

    SOCKETS = []
    BUFFER_SIZE = 4096

    HOST = '0.0.0.0'
    PORT = 10000

    def __init__(self):
        """
        Set the socket connections ready to go
        """
        self.mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mysock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.command = Command()
        self.set_world(World(10, 10))

    def set_world(self, world):
        """
        The setter for world
        """
        self.world = world

    def get_world(self):
        """
        The getter for world
        """
        return self.world

    def _process_read(self, sock):
        """
        For each read from the client process the data
        """
        if sock == self.mysock:
            sockfd, addr = self.mysock.accept()
            self.SOCKETS.append(sockfd)
            logging.info("Client (%s, %s) connected", addr[0], addr[1])
        else:
            data = sock.recv(self.BUFFER_SIZE)
            if data:
                try:
                    return data.decode("utf-8")
                except UnicodeDecodeError as e:
                    logging.warning(str(e))
            else:
                # remove the socket that's broken
                if sock in Server.SOCKETS:
                    self.SOCKETS.remove(sock)
                    logging.info("Removed connection")

        return None

    def listen(self):
        """
        Set up the connection, and start listening using
        """
        self.mysock.bind((self.HOST, self.PORT))
        self.mysock.listen(10)
        logging.info('Listening on %s port %s', self.HOST, self.PORT)

        self.SOCKETS.append(self.mysock)

        while True:
            ready_to_read, ready_to_write, in_error = select.select(
                self.SOCKETS,
                [],
                [],
                1
            )
            for sock in ready_to_read:
                command = self._process_read(sock)
                if command is not None:
                    (playernum, method, data) = self.run_command(command)

                    if method == "PRINT":
                        sock.send(str(self.world) + "\n")
                    if method == "GET":
                        sock.send(json.dumps(self.world.to_data()) + "\n")

                    #sock.send("Performing a " + method + "\n")

            if self.world.allPlayersLocked() is True:
                self.world.doStep()
                logging.info(self.world)

        self.mysock.close()

    def run_command(self, command):
        """
        for each command that comes in process it
        """

        command = str(command).strip()

        (playernum, method, data) = self.command.process(command)
        logging.info("P: " + str(playernum) + ", M: " + method + ", D: " + str(data) + ", C:" + command)

        try:
            if method == "REGISTER":
                position = Position(data['position'][0], data['position'][1])
                self.world.addPlayer(str(data['name']), position)
            elif method == "MOVE":
                self.world.setInputMovePlayer(playernum, data)
            elif method == "TURN":
                self.world.setInputTurnPlayer(playernum, data)
            elif method == "SHOOT":
                self.world.setInputShootPlayer(playernum)
            elif method == "LOCK":
                if playernum is None:
                    self.world.lockAllPlayers()
                else:
                    self.world.setInputLockPlayer(playernum)
        except InvalidMove as e:
            logging.warning("Invalid Move: " + str(e))
        except InvalidPlayer as e:
            logging.warning("Invalid Player: " + e.message)
        except OutOfAmmo as e:
            logging.info("OutOfAmmo: " + str(e))

        return (playernum, method, data)
