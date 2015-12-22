class Direction:
    """
    This class stores a helpfull functions to convert strings into
    degrees
    """

    @staticmethod
    def get_degrees(direction):
        if direction == "EAST":
            return 90
        elif direction == "SOUTH":
            return 180
        elif direction == "WEST":
            return 270
        else:
            return 0
