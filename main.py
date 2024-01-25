# Ohm Patel
# Flight Plan Group Assignment
# Find the shortest path between A and B, avoiding obstacles ('X')


# create node class
class Node:
  # initialize node
  def __init__(self, parent, x, y):
    # parent of node
    self.parent = parent
    # position of node
    self.x = x
    self.y = y
    # g, h, and f value of node
    self.g = 0  # distance from the start (i.e. number of steps moved to get to this node)
    self.h = 0  # estimated distance to the goal
    self.f = 0  # sum of g and h


# function adds the route to the grid using asterisks ("*")
def path(currNode, col, rows):
  # list, which will become a list of lists, to hold the route (all positions visited)
  route = []

  # loop from current node to the start using the parent of each node (ends at start since start node does not have a parent)
  # Note: first currNode is the last node in the route
  while currNode is not None:
    # create list and add x and y values of the current node
    pos = []
    pos.append(currNode.y)
    pos.append(currNode.x)
    # add the list containing the position of the current node to the route list
    route.append(pos)
    # set current node as the parent of the node whos position was just added to the route
    currNode = currNode.parent

  # remove starting position from route list (to keep 'A' and not make it a '*')
  del route[-1]

  # loop through the route
  for i in range(len(route)):
    # place a star on the grid at the position within route list
    grid[route[i][0]][route[i][1]] = '*'

  # return the grid which now has the route printed on it
  return grid


# function performs a star search
def aStar(startX, startY, goalX, goalY, col, rows):
  # initalize open and closed list
  open = []  # contains all nodes that we will examine
  closed = []  # nodes that have already been examined

  # initialize the start node (no parent and g, h and f value is zero)
  startNode = Node(None, startX, startY)
  startNode.g, startNode.h, startNode.f = 0, 0, 0

  # add the start node to the open list
  open.append(startNode)

  # loop while their are still nodes in the open list
  while len(open) > 0:
    # set current node to the first node in the open list
    currNode = open[0]
    # variable holds the position of the current node in the open list
    currIndex = 0

    # loop through all nodes in open list
    for index, item, in enumerate(open):
      # if the f value of the node being checked is lower than the current node
      if item.f < currNode.f:
        # make current node the node being checked (since it has a lower f value)
        currNode = item
        # make the index the index of the node we are converting to
        currIndex = index
    # remove the new current node from the open list
    open.pop(currIndex)

    # list contains all valid neighbouring nodes
    neighbours = []
    # if the node underneath is not a barrier and is a position on the grid add it to list of neighbours
    if currNode.y < rows - 1 and grid[currNode.y + 1][currNode.x] != 'X':
      neighbours.append(Node(currNode, currNode.x, currNode.y + 1))

    # if the node above is not a barrier and is a position on the grid add it to list of neighbours
    if currNode.y > 0 and grid[currNode.y - 1][currNode.x] != 'X':
      neighbours.append(Node(currNode, currNode.x, currNode.y - 1))

    # if the node on the right is not a barrier and is a position on the grid add it to list of neighbours
    if currNode.x < col - 1 and grid[currNode.y][currNode.x + 1] != 'X':
      neighbours.append(Node(currNode, currNode.x + 1, currNode.y))

    # if the node on the left is not a barrier and is a position on the grid add it to list of neighbours
    if currNode.x > 0 and grid[currNode.y][currNode.x - 1] != 'X':
      neighbours.append(Node(currNode, currNode.x - 1, currNode.y))

  # loop through neighbours
    for possibleNode in neighbours:
      # end search if any of the neighbours is the goal
      if grid[possibleNode.y][possibleNode.x] == 'B':
        return path(currNode, col, rows)

      # calculate g by adding one to the current g value (each move increases by one)
      possibleNode.g = currNode.g + 1
      # calculate h value using manhatten distance method
      possibleNode.h = abs(possibleNode.x - goalX) + abs(possibleNode.y - goalY)
      # calculate f by adding g and h
      possibleNode.f = possibleNode.g + possibleNode.h

      # add node to open list
      open.append(possibleNode)

    # move the current node to the closed list
    closed.append(currNode)

  # if the open set ever has nothing in it this means their is no solution; print an error and quit the program
  print("NO SOLUTION")
  quit()


# open input file and store each line into grid as a list of lists using 'split()'
global grid  # grid is a global variable (usuable in all functions)
grid = [line.split() for line in open('Input.txt')]
# store the number of columns and rows
col = len(grid[0])
rows = len(grid)

# locate start position and goal position -> then store their coordinates by looping through the list of lists
startX, startY, goalX, goalY = 0, 0, 0, 0
for j in range(col):
  for i in range(rows):
    if grid[i][j] == 'B':
      goalX = j
      goalY = i
    elif grid[i][j] == 'A':
      startX = j
      startY = i

# call a star search function and store result
result = aStar(startX, startY, goalX, goalY, col, rows)

# open output file
file = open("outputtedPath.txt", "w")
# loop through each list within the result (which is a list of lists)
for list in result:
  # writes each value in the list the output file without seperated with ' ' without including brackets ("\n" ends line)
  file.write(' '.join(list) + "\n")
# close file
file.close()
print("done")

# Testing
"""
TEST 1:
Input.txt:
. . . . . . . . 
. . . . . . . .
. . . . . . . . 
. . . . . . . . 
. . X . . . . .
. X A X . . B . 
. . X . . . . . 
. . . . . . . .

RESULT:
NO SOLUTION
repl process died unexpectedly: 

TEST 2:

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

TEST 3:

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
"""

#REFERENCES
"""
- https://www.geeksforgeeks.org/a-search-algorithm/ (pseudo-code, h formula, general background information)
- http://robotics.caltech.edu/wiki/images/e/e0/Astar.pdf (background information)
- https://stackoverflow.com/questions/47297741/how-do-i-read-a-text-file-as-a-list-of-lists-in-python (reading a file and turning it into a list of lists)
"""
