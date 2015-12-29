class Direction:
    """
    This class stores a helpfull functions to convert strings into
    degrees
    """

    @staticmethod
    def get_degrees(direction):
        if direction == "EAST" or direction == "RIGHT":
            return 90
        elif direction == "SOUTH" or direction == "DOWN":
            return 180
        elif direction == "WEST" or direction == "LEFT":
            return 270
        else:
            return 0
