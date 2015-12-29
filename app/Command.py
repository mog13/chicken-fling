from Direction import Direction
import json

class Command:
    """
    A simple helpfull class to return python commands
    """

    def __init__(self):
        """
        Set up the command class
        """
        pass

    def process(self, command):
        """
        Given a @command parse it and return an
        object version of the commands
        """
        splits = command.strip(' \t\n\r').split(' ', 2)
        player = int(splits[0])
        method = str(splits[1])
        data = None

        if method == "MOVE" or method == "TURN":
            data = Direction.get_degrees(splits[2])
        elif method == "REGISTER":
            data = json.loads(splits[2])

        return (player, method, data)
