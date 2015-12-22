#!/usr/bin/env python3

import signal
import sys
import socket
import select

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

  def _process_read(self, sock):
    """
    For each read from the client process the data
    """
    if sock == self.mysock:
      sockfd, addr = self.mysock.accept()
      self.SOCKETS.append(sockfd)
      print("Client (%s, %s) connected" % addr)
    else:
      data = sock.recv(self.BUFFER_SIZE)
      if data:
        return data.decode("utf-8")
      else:
        # remove the socket that's broken
        if sock in Server.SOCKETS:
            self.SOCKETS.remove(sock)
            print("Removed connection")

  def listen(self):
    """
    Set up the connection, and start listening using
    """
    self.mysock.bind((self.HOST, self.PORT))
    self.mysock.listen(10)
    print('Listening on %s port %s' % (self.HOST, self.PORT))

    self.SOCKETS.append(self.mysock)

    while ChickenFling.running is True:
      ready_to_read, ready_to_write, in_error = select.select(
        self.SOCKETS,
        [],
        [],
        1
      )
      for sock in ready_to_read:
        print(self._process_read(sock), end="")

    self.mysock.close()

"""
Simple class for general program variables
"""
class ChickenFling:
  running = True

  @staticmethod
  def signal_int(signal, frame):
    print("\nShutting Down...", end="")
    ChickenFling.running = False

  @staticmethod
  def main():
    server = Server()
    server.listen()
    print("Exiting!")

signal.signal(signal.SIGINT, ChickenFling.signal_int)
ChickenFling.main()
