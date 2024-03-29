from Point import Point
from random import randint
from Point import Point

maxCol = 0
points = [Point(1, 1), Point(2, 2), Point(3, 3), Point(0, 0)]
isOnlineAlg = False  # if RectangleAlg: =False
STUDENTS_ID = "314800442_322801291"  # change IDs


def onlineColoringAlg(value):
    """
    students' algorithm for "online coloring"
    methodology - iterative call for method.
    use a point (given by x-value), give it a color(according to "points" list expanding each time).
    :param value: numeric value of the point (x-coordinate)
    :return: color_num
    """
    global isOnlineAlg
    isOnlineAlg = False
    global maxCol
    p = Point(value)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # your ALG here...

    color_num = maxCol  # decide point's color depending on your algorithm

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    p.col_num = color_num
    points.append(p)
    print(f"current max col is:{maxCol}")
    return color_num


def rectangleColoringAlg():
    """
    students' algorithm for "rectangle coloring"
    methodology - one-time call for method.
    use a given "points" list, color all points.
    :param: no arguments (method called once)
    :return: nothing
    """
    global isOnlineAlg
    isOnlineAlg = False

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    current_point_list = points
    maxCol = 0
    current_point_list = sort_points_by_x(points)
    while len(current_point_list) > 0:
        maximum_monotonic_subsequence = find_maximum_monotonic_subsequence(current_point_list)
        # List to track every other point in the subsequence
        points_to_remove = []
        for i, p in enumerate(maximum_monotonic_subsequence):
            if i % 2 == 0:  # Select every other point
                p.col_num = maxCol
                points_to_remove.append(p)  # Add this point to the removal list
        maxCol += 1  # Proceed to next color
        # Remove points in maximum_monotonic_subsequence from current_point_list
        current_point_list = [p for p in current_point_list if p not in points_to_remove]
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print(f"current max col is:{maxCol}")
    print(f"finished running rectangleColoringAlg...")
    return


def sort_points_by_x(point_list):
    return sorted(point_list, key=lambda point: point.valueX)


def find_maximum_monotonic_subsequence(point_list):
    # Re-use the previously defined function and comparators
    non_decreasing = find_maximum_subsequence(point_list, leq_point)
    non_increasing = find_maximum_subsequence(point_list, geq_point)

    # Return the longer of the two subsequences
    if len(non_decreasing) >= len(non_increasing):
        return non_decreasing
    else:
        return non_increasing


# Comparators
def leq_point(a, b):
    return a.valueY <= b.valueY


def geq_point(a, b):
    return a.valueY >= b.valueY


def find_maximum_subsequence(list, comparator):
    n = len(list)
    dp = [1] * n  # Initialize the dp array
    predecessor = [-1] * n  # To reconstruct the path

    # Build dp[] using the comparator
    for i in range(1, n):
        for j in range(i):
            if comparator(list[i], list[j]) and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                predecessor[i] = j

    # Find the maximum in dp[] and its index
    max_length = max(dp)
    max_index = dp.index(max_length)

    # Reconstruct the subsequence
    subsequence = []
    current_index = max_index
    while current_index != -1:
        subsequence.append(list[current_index])
        current_index = predecessor[current_index]
    subsequence.reverse()  # Reverse to get the correct order

    return subsequence


def test_coloring_algorithm(point_list):
    # Extract all unique x and y coordinates
    x_coords = {p.valueX for p in point_list}
    y_coords = {p.valueY for p in point_list}

    # Generate rectangles from all combinations of x and y coordinates, including 0 and 1-dimensional
    for x1 in x_coords:
        for y1 in y_coords:
            for x2 in x_coords:
                for y2 in y_coords:
                    # Define the corners of the rectangle
                    rect_corner1 = Point(min(x1, x2), min(y1, y2))
                    rect_corner2 = Point(max(x1, x2), max(y1, y2))

                    # Initialize dictionary to track color occurrences
                    color_occurrences = {}

                    # Check each point to see if it's within the current rectangle
                    for p in point_list:
                        if is_within_rectangle(p, rect_corner1, rect_corner2):
                            color_occurrences[p.col_num] = color_occurrences.get(p.col_num, 0) + 1

                    # Proceed to the next rectangle if no points are found within the current rectangle
                    if not color_occurrences:
                        continue

                    # If the rectangle contains points but there's no color with exactly one occurrence
                    if 1 not in color_occurrences.values():
                        print("Test failed: There's an axis-parallel rectangle (or line) that's not conflict-free.")
                        return False

    print("Test passed: All axis-parallel rectangles (including lines) are conflict-free.")
    return True


def is_within_rectangle(p, rect_corner1, rect_corner2):
    """
    Check if point p is within the axis-parallel rectangle defined by rect_corner1 and rect_corner2.
    """
    return (min(rect_corner1.valueX, rect_corner2.valueX) <= p.valueX <= max(rect_corner1.valueX,
                                                                             rect_corner2.valueX) and
            min(rect_corner1.valueY, rect_corner2.valueY) <= p.valueY <= max(rect_corner1.valueY, rect_corner2.valueY))


def generate_unique_points(n, max_range):
    unique_points = set()
    point_list = []
    while len(point_list) < n:
        x, y = randint(0, max_range), randint(0, max_range)
        # Convert the coordinates to a string (or a tuple) to check uniqueness
        coord_str = f"{x},{y}"
        if coord_str not in unique_points:
            unique_points.add(coord_str)
            point_list.append(Point(x, y))
    return point_list


# Generate 10,000 unique points with coordinates in the range [0, 10000]
points = generate_unique_points(20, 20)

rectangleColoringAlg()
for p in sort_points_by_x(points):
    print(p)
test_coloring_algorithm(points)