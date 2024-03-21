import coloringAlgForStudents
from Point import Point
import math
from coloringAlgForStudents import rectangleColoringAlg, maxCol, isOnlineAlg
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def getValues(n):
#~~~~~~~~~~~RANDOM:~~~~~~~~~~~~~

    valuesList = [random.random() * 100 for _ in range(n)]
    return valuesList
#~~~~~~~~~~~ARDESH:~~~~~~~~~~~~~
# Generate ardesh sequences (of \sqrt(n) descending blocks):
    block_size = int(math.sqrt(n))

    # Initialize an empty list to store the result
    valuesList = []

    # Generate values for each block
    for i in range(0, n, block_size):
        # Calculate the start and end of the current block
        start = i + 1
        end = i + block_size
        # Generate the numbers for the block in descending order and append to the list
        block = list(range(end, start - 1, -1))
        valuesList.extend(block)

    print(valuesList)

    return valuesList


def createPointList(n):
    yVals = getValues(n)
    xVals = sorted(yVals.copy())
    # create point list with tuples of (x,y) values from xVals,yVals accordinagly:
    pointsList = []
    for i in range(n):
        p = Point(xVals[i], yVals[i])
        pointsList.append(p)
    # print(pointsList)
    return pointsList




def plotPoints2D(points, segment=None):
    # Extracting X and Y values for plotting
    valuesX = [point.valueX for point in points]
    valuesY = [point.valueY for point in points]

    plt.figure(figsize=(12, 6))

    # Scatter plot for all points
    plt.scatter(valuesX, valuesY,color='blue', label='Points')

    # If a segment is provided, draw a rectangle around it
    if segment:
        # Calculate the bounds of the rectangle
        minX = min(point.valueX for point in segment)
        maxX = max(point.valueX for point in segment)
        minY = min(point.valueY for point in segment)
        maxY = max(point.valueY for point in segment)

        # Create the rectangle from the bounds
        rect = Rectangle((minX, minY), maxX - minX, maxY - minY, linewidth=3, edgecolor='r', facecolor='none',
                         label='Segment')

        # Add the rectangle to the plot
        plt.gca().add_patch(rect)

    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.title('Scatter Plot with Points in 2D Space and Segment Rectangle')
    plt.legend()
    plt.grid(True)
    plt.show()


def has_unique_color_in_every_segment(points):
    '''
    check the points list for "has unique color?", if not - return problematiue segment.
    :param points:
    :return: True/False, segment=None
    '''
    for iter in {1, 2}:     ## two iterations of checking - segments by Y and segments by X
        if (iter == 1):
            points = sorted(points, key=lambda point: point.valueX)
        else:
            points = sorted(points, key=lambda point: point.valueY)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                # Extracting the segment between points[i] and points[j]
                segment = points[i:j + 1]

                # Counting the occurrences of each color in this segment
                color_counts = {}
                for point in segment:
                    color_counts[point.col_num] = color_counts.get(point.col_num, 0) + 1

                # Checking if there's exactly one color that appears once
                unique_colors = [color for color, count in color_counts.items() if count == 1]
                if not (any(unique_colors) == 1):
                    return False, segment  # Found a segment without a unique color

    return True, None  # All segments have a unique color


def findMaxCol():
    maxPoint = sorted(coloringAlgForStudents.points, key=lambda point: point.col_num)[-1]
    maxColor = maxPoint.col_num
    return maxColor


def checkCorrectness():
    # Test the function with your points
    points = coloringAlgForStudents.points
    result = has_unique_color_in_every_segment(points)
    print("\n\tcorrectness:\n\t-----------")
    if result[0]:
        from coloringAlgForStudents import maxCol
        print(f"all segments has unique color in them, max color is {findMaxCol()}")
        plotPoints2D(points)
        print(f"\n\t\t\t~~~~TEST PASSED!~~~\n\t\t\t~~~~maxCol is {findMaxCol()}~~~")
    else:
        print(f"test failed, there is no unique color in the segment:"
              f"\n\n\tp{result[1][0]}"
              f"\n\t\t\t~"
              f"\n\tp{result[1][-1]}")
        print("\nsegment:")
        for point in result[1]:
            print(point)
        plotPoints2D(points, result[1])
        print(f"\n\t\t\t~~~~TEST FAILED!~~~\n\t~~~~failed segment is printed above~~~")


def runTest(n):
    # Generate a list of 100 random values
    # random_values = getValues(n)
    # random_values = [random.random() * 100 for _ in range(n)]
    # print(random_values[:5])  # Display the first 5 values for a quick check
    coloringAlgForStudents.points = createPointList(n)


    if not isOnlineAlg:

        # for val in random_values:
        #     cn = onlineColoringAlg(val)
        #     print("color is: ", cn)
        # checkCorrectness()
        print("Running RectangleColoringAlg...\n")
        rectangleColoringAlg()
    else:
        print("'isOnlineAlg' set to 'True', probably its not a RectangleColoringAlg")
        print("\n\tQUITTING PROGRAM")
        return
    # print("\n\tpoint list:\n\t-----------")
    # for p in coloringAlgForStudents.points:
    #     print(p)
    checkCorrectness()


if __name__ == "__main__":
    # getValues(10000)
    # coloringAlgForStudents.points = createPointList(100)
    # segment = points[18],points[80] ##segment to plot
    # plotPoints2D(points,segment)
    runTest(1000)
