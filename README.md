# A-Star-Search-Algorithm-Flight-Plan

# OVERVIEW
This project is a pathfinding program in Python which finds a path between 2 points


# PROJECT DESCRIPTION
This project utilizes an A* Search Algorithm which uncovers the most efficient path between 2 points in an obsticle ridden environment.

Graph traversal techniques and a backtracking algorithm are implemented in order to enhance the accuracy and efficiency of the code.

The input is given through a text file (Input.txt) and the resulting path is outputted into a seperate text file (outputtedPath.txt).

In this project the character 'A' is deemed the starting point, 'B' is the end point and 'X' are obstacles.

The code is  slow to terminate when no path exists between 2 points. This is an aspect of the project which I am hoping to improve in the future.


# TESTING
## test 1
Input.txt:
. . . . . . . . .
. . . . . . B . .
. . X X . X . . .
. . . . X X X . .
. A . . . . . . .
. . . . . . . . .

outputtedPath.txt:
. . . . . . . . .
. * * * * * B . .
. * X X . X . . .
. * . . X X X . .
. A . . . . . . .
. . . . . . . . .

## test 2
Input.txt:
. . . . . . . . 
. . . . . . . .
. . . . . . . . 
. . . . . . . . 
. . X . . . . .
. X A X . . B . 
. . X . . . . . 
. . . . . . . .

result:
NO SOLUTION

## test 3
Input.txt:
. . X X . . . . X . . .
X X X . . X . . . . X .
. . X . X . X . . X B .
. . . . . . . . . X . .
X . X A . X . . . X . X
. . . . . . . X . . . .
. . X X . . . . . X . X

outputtedPath.txt:
. . X X . . . . X . . .
X X X . . X . . . . X .
. . X . X . X . . X B .
. . . * * * * * * X * .
X . X A . X . . * X * X
. . . . . . . X * * * .
. . X X . . . . . X . X


# REFERENCES
https://www.geeksforgeeks.org/a-search-algorithm/ (pseudo-code, h formula, general background information)
http://robotics.caltech.edu/wiki/images/e/e0/Astar.pdf (background information)
https://stackoverflow.com/questions/47297741/how-do-i-read-a-text-file-as-a-list-of-lists-in-python (reading a file and turning it into a list of lists)
