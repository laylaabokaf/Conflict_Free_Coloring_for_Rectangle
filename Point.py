class Point:
    # Class variable to keep track of the total number of points created
    _total_points = 0

    def __init__(self, valueX, valueY=0):
        # Increment the total points counter and assign it as the serial number
        Point._total_points += 1
        self.serial_num = Point._total_points

        # Initialize other instance variables
        self.valueX = valueX
        self.valueY = valueY

        self.col_num = None

    def __repr__(self):
        return f"Point(serial_num={self.serial_num}, value=({self.valueX},{self.valueY}), col_num={self.col_num})"
