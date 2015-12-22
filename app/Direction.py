class Direction:
    """
    This class stores a helpfull functions to convert strings into
    degrees
    """

    @staticmethod
    def get_degrees(direction):
        if direction is "EAST":
            return 90
        elif direction is "SOUTH":
            return 180
        elif direction is "WEST":
            return 270
        else:
            return 0
