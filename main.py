import copy
import random
import math

#Maze class used for creating Maze Object and utilizing its instance methods
class Maze:
    def __init__(self, mazedimension):
        self._Maze = [[0] * mazedimension for i in range(mazedimension)]
        self._MazeDimension = mazedimension
        self._allblocked = []
        self._allOnFire = []
        self._fireProbability = 0

    #Populates maze with walls with P = .30
    def __populateMazeWalls__(self):

        columncounter = 0
        rowcounter = 0

        for column in enumerate(self._Maze):
            rowcounter = 0

            for row in enumerate(self._Maze):

                if columncounter < self._MazeDimension or rowcounter < self._MazeDimension:
                    if columncounter == 0 and rowcounter == 0:
                        pass  # we don't want a block here so just don't do anything
                    elif columncounter == 0 and rowcounter == self._MazeDimension - 1:
                        pass  # we don't want a block here so just don't do anything
                    elif columncounter == self._MazeDimension - 1 and rowcounter == 0:
                        pass  # we don't want a block here so just don't do anything
                    elif columncounter == self._MazeDimension - 1 and rowcounter == self._MazeDimension - 1:
                        pass  # we don't want a block here so just don't do anything
                    elif columncounter == (math.ceil((self._MazeDimension / 2)) - 1) and rowcounter == (
                            (math.ceil(self._MazeDimension / 2)) - 1):
                        pass  # we don't want a block here to just don't do anything
                    else:
                        if random.random() < .30:
                            self._Maze[columncounter][rowcounter] = 1
                            self._allblocked.append(tuple((columncounter, rowcounter)))

                rowcounter = rowcounter + 1
            columncounter = columncounter + 1

        if cornerToMiddlePathCheckDFS(0, 0, self) == True and cornerToMiddlePathCheckDFS(
                self.__getMazeDimension__() - 1, 0, self) == True and cornerToMiddlePathCheckDFS(0,
                                                                                                 self.__getMazeDimension__() - 1,
                                                                                                 self) == True and cornerToMiddlePathCheckDFS(
            self.__getMazeDimension__() - 1, self.__getMazeDimension__() - 1, self) == True:
            pass
        else:
            return False

    #returns Array of Maze
    def __getMazeArray__(self):
        return self._Maze
    #returns Dimensions of Maze
    def __getMazeDimension__(self):
        return self._MazeDimension
    #returns list of all coordinates on fire
    def __getAllOnFire__(self):
        return self._allOnFire
    #returns the fire spread probability of maze
    def __getFireProbability__(self):
        return self._fireProbability
    #allows access to the list containing all coordinates on fire
    def __setAllOnFire__(self, newlyOnFire):
        self._allOnFire += newlyOnFire


# returns list of all neighbors of a grid position
def neighbors(column_number, row_number, maze, typeOfNeighbor):
    allneighbors = []

    if column_number < maze.__getMazeDimension__() or row_number < maze.__getMazeDimension__():
        # upper
        if row_number == 0:
            # for upper left corner (2 neighbors)
            if column_number == 0:
                if maze.__getMazeArray__()[column_number + 1][row_number] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number + 1, row_number)))
                if maze.__getMazeArray__()[column_number][row_number + 1] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number, row_number + 1)))
            # for upper right corner (2 neighbors)
            elif column_number == maze.__getMazeDimension__() - 1:
                if maze.__getMazeArray__()[column_number][row_number + 1] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number, row_number + 1)))
                if maze.__getMazeArray__()[column_number - 1][row_number] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number - 1, row_number)))
            # for upper non corner (3 neighbors)
            else:
                if maze.__getMazeArray__()[column_number + 1][row_number] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number + 1, row_number)))

                if maze.__getMazeArray__()[column_number][row_number + 1] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number, row_number + 1)))

                if maze.__getMazeArray__()[column_number - 1][row_number] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number - 1, row_number)))

        # lower
        elif row_number == maze.__getMazeDimension__() - 1:
            # for lower left corner
            if column_number == 0:
                if maze.__getMazeArray__()[column_number][row_number - 1] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number, row_number - 1)))
                if maze.__getMazeArray__()[column_number + 1][row_number] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number + 1, row_number)))
            # for lower right corner
            elif column_number == maze.__getMazeDimension__() - 1:
                if maze.__getMazeArray__()[column_number][row_number - 1] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number, row_number - 1)))
                if maze.__getMazeArray__()[column_number - 1][row_number] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number - 1, row_number)))
            # for lower non corner (3 neighbors)
            else:
                if maze.__getMazeArray__()[column_number][row_number - 1] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number, row_number - 1)))
                if maze.__getMazeArray__()[column_number + 1][row_number] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number + 1, row_number)))
                if maze.__getMazeArray__()[column_number - 1][row_number] == typeOfNeighbor:
                    allneighbors.append(tuple((column_number - 1, row_number)))

        # for left side nodes that aren't in corners
        elif column_number == 0:
            if maze.__getMazeArray__()[column_number][row_number + 1] == typeOfNeighbor:
                allneighbors.append(tuple((column_number, row_number + 1)))
            if maze.__getMazeArray__()[column_number + 1][row_number] == typeOfNeighbor:
                allneighbors.append(tuple((column_number + 1, row_number)))
            if maze.__getMazeArray__()[column_number][row_number - 1] == typeOfNeighbor:
                allneighbors.append(tuple((column_number, row_number - 1)))

        # for right side nodes that aren't in corners
        elif column_number == maze.__getMazeDimension__() - 1:

            if maze.__getMazeArray__()[column_number][row_number - 1] == typeOfNeighbor:
                allneighbors.append(tuple((column_number, row_number - 1)))
            if maze.__getMazeArray__()[column_number][row_number + 1] == typeOfNeighbor:
                allneighbors.append(tuple((column_number, row_number + 1)))
            if maze.__getMazeArray__()[column_number - 1][row_number] == typeOfNeighbor:
                allneighbors.append(tuple((column_number - 1, row_number)))

        # anything inbetween
        else:
            if maze.__getMazeArray__()[column_number][row_number - 1] == typeOfNeighbor:
                allneighbors.append(tuple((column_number, row_number - 1)))
            if maze.__getMazeArray__()[column_number + 1][row_number] == typeOfNeighbor:
                allneighbors.append(tuple((column_number + 1, row_number)))
            if maze.__getMazeArray__()[column_number][row_number + 1] == typeOfNeighbor:
                allneighbors.append(tuple((column_number, row_number + 1)))
            if maze.__getMazeArray__()[column_number - 1][row_number] == typeOfNeighbor:
                allneighbors.append(tuple((column_number - 1, row_number)))
    else:
        print("Error, out of bounds")
    return allneighbors

#checks if each corner of the maze has a path to the middle
def cornerToMiddlePathCheckDFS(column, row, maze):
    # make visited boolean array
    visited = [[bool] * maze.__getMazeDimension__() for i in range(maze.__getMazeDimension__())]
    fringe = []
    fringe.append((column, row))
    # input turned into tuple
    # unpacked tuple as input to neighbors ... neighbors returns tuple
    while (len(fringe)):  # while the fringe is not empty
        poppedNode = (fringe.pop())  # pop element off fringe
        visited[poppedNode[0]][poppedNode[1]] = True  # set popped off node to visited
        poppedNodeNeigbors = neighbors(*poppedNode, maze, 0)  # add all neighbors of popped off node
        # if a neighbor is visted dont add it to queue
        while len(poppedNodeNeigbors):  # while the list of neighbors is not empty
            oneNeighbor = poppedNodeNeigbors.pop()  # pop off neighbor
            if oneNeighbor == (
                    (math.ceil((maze.__getMazeDimension__() / 2)) - 1,
                     math.ceil((maze.__getMazeDimension__() / 2)) - 1)):
                return True
            if visited[oneNeighbor[0]][oneNeighbor[1]] == True:  # if neighbor node has already been visited do nothing
                pass
            else:  # if neighbor node has not been visited add it to the fringe
                fringe.append(oneNeighbor)
    return False

#constructs a maze by continuously creating one until a valid one is made
def generateUsableMaze(mazedimensions):
    maze = Maze(mazedimensions)

    # this is for the rare instance that by starting the fire in the middle the maze is no longer valid
    while maze.__populateMazeWalls__() == False:
        maze = Maze(mazedimensions)  # keeps constructing a maze until a valid one is found then returns it

    return maze

#marks the middle of the maze as on fire
def startFire(maze, probability):
    maze.__getMazeArray__()[math.ceil((maze.__getMazeDimension__() / 2)) - 1][
        math.ceil((maze.__getMazeDimension__() / 2)) - 1] = 2
    maze._fireProbability = probability
    maze.__getAllOnFire__().append(
        ((math.ceil((maze.__getMazeDimension__() / 2)) - 1), math.ceil((maze.__getMazeDimension__() / 2)) - 1))

#gets all the points on fire and sets neighboring points on fire based on probability
def advanceFire(maze):

    newFire = []
    for x in maze.__getAllOnFire__():
        neighborsx = neighbors(*x, maze, 0)

        for b in neighborsx:
            howmanyneighborsareonfire = len(neighbors(*b, maze, 2))

            if random.random() <= 1 - ((1 - maze.__getFireProbability__()) ** howmanyneighborsareonfire):
                maze.__getMazeArray__()[b[0]][b[1]] = 2
                newFire.append((b[0], b[1]))
    maze.__setAllOnFire__(newFire)
# MAIN CODE DONE-------------------------------


# AGENT 1-------------------------------------------------------
#Runs Agent 1 on a input maze and specified fire spread probability
def runAgent1(inputMaze, fireSpreadProbability):
    inputMazeOriginal = copy.deepcopy(inputMaze)

    dead = False

    inputMazeAfterBFS = (BFS(inputMaze, (0, 0)))

    if inputMazeAfterBFS[1] == True:
        currentBestPath = copy.deepcopy(getBestPath(inputMazeAfterBFS[0]))
        currentBestPath.reverse()
        startFire(inputMazeOriginal, fireSpreadProbability)
        count = -1

        for i in currentBestPath:
            if count == -1:
                inputMazeOriginal.__getMazeArray__()[i[0]][i[1]] = 3
            else:
                inputMazeOriginal.__getMazeArray__()[i[0]][i[1]] = 3
                advanceFire(inputMazeOriginal)

            count = count + 1

            if i in inputMazeOriginal.__getAllOnFire__():
                dead = True
                break
        if dead == False:
            return True
        else:
            return False
    else:
        return False

#runs BFS on a maze from a specified current node and returns True if there exists a path from the current node to goal or false otherwise
#along with a list of the path BFS took
def BFS(maze, currentNode):
    visited = []
    queue = []
    goalNode = (maze.__getMazeDimension__() - 1, maze.__getMazeDimension__() - 1)
    goalNodeFound = False
    prev = []

    startFire(maze, .00001)

    maze.__getMazeArray__()[currentNode[0]][currentNode[1]] = 4
    visited.append(currentNode)
    queue.append(currentNode)

    while queue:
        m = queue.pop(0)

        for neighbor in neighbors(*m, maze, 0):
            if neighbor not in visited:

                if neighbor == goalNode:
                    goalNodeFound = True
                    maze.__getMazeArray__()[neighbor[0]][neighbor[1]] = 4
                    visited.append(neighbor)
                    queue.append(neighbor)

                    break
                visited.append(neighbor)
                queue.append(neighbor)
            if m not in prev:
                prev.append((m, neighbor))  # parent and its child

                maze.__getMazeArray__()[neighbor[0]][neighbor[1]] = 4

                # for now just to see what it looks like on the graph
        if goalNodeFound == True:
            prev.append((m, neighbor))  # parent and its child
            return prev, True
            break
    if goalNodeFound == False:
        return prev, False

#Traces back the list given by running BFS and returns the shortest path from the goal node
def getBestPath(listOfPrev):

    listOfPrev.reverse()
    listOfParentOfCurrentNode = []
    parent = listOfPrev[0]
    listOfParentOfCurrentNode.append(parent[1])
    listOfParentOfCurrentNode.append(parent[0])

    while (listOfPrev[len(listOfPrev) - 1])[0] not in listOfParentOfCurrentNode:
        z = parent[0]

        for i in listOfPrev:
            if i[1] == z:
                listOfParentOfCurrentNode.append(i[0])
                parent = i
                break

    return listOfParentOfCurrentNode

#Runs Agent 2 on a input maze and specified fire spread probability
def runAgent2(inputMaze, fireSpreadProbability):

    setNewBestPathRequired = False
    BFSFailure = False
    dead = False
    reachedGoal = False
    inputMazeOriginal = copy.deepcopy(inputMaze)



    inputMazeAfterBFS = (BFS(inputMaze, (0, 0)))
    # runs BFS on the input maze to make sure there's a path from the start to goal

    if inputMazeAfterBFS[1] == True:
        # if a path to the goal exists

        currentBestPath = copy.deepcopy(getBestPath(inputMazeAfterBFS[0]))
        #returns the shortest path from the start to the goalnode

        currentBestPath.reverse()
        # reverse list of currentbestpath so we start from 0,0
        startFire(inputMazeOriginal, fireSpreadProbability)
        # start the fire in the center (middle should always start on fire no matter the probability)

        count = -1

        while dead == False and reachedGoal == False:
            for i in currentBestPath:

                if setNewBestPathRequired == True:
                    setNewBestPathRequired = False
                    count = count -1
                    break
                if count == -1:
                    inputMazeOriginal.__getMazeArray__()[i[0]][i[1]] = 3
                    count = 0
                else:
                    for point in currentBestPath:
                        if point in inputMazeOriginal.__getAllOnFire__():
                            inputMazeOriginalToRunBFSOn = copy.deepcopy(inputMazeOriginal)
                            newPath = copy.deepcopy(BFS(inputMazeOriginalToRunBFSOn, i))
                            if newPath[1] == False:
                                BFSFailure = True
                                break
                            if newPath[1] == True:

                                currentBestPath = copy.deepcopy(getBestPath(newPath[0]))
                                currentBestPath.reverse()
                                setNewBestPathRequired = True
                                break


                    if inputMazeOriginal.__getMazeArray__()[i[0]][i[1]] == 2:
                        dead = True
                        inputMazeOriginal.__getMazeArray__()[i[0]][i[1]] = 3
                        advanceFire(inputMazeOriginal)
                        count = count + 1
                        break
                    if (inputMazeOriginal.__getMazeArray__()[i[0]][i[1]] == 3):
                        pass
                    else:
                        inputMazeOriginal.__getMazeArray__()[i[0]][i[1]] = 3
                        advanceFire(inputMazeOriginal)
                    if i == (inputMazeOriginal.__getMazeDimension__() -1,inputMazeOriginal.__getMazeDimension__()-1):
                        reachedGoal = True
                        break
                count = count + 1

        if dead == True:
            return False
        elif reachedGoal == True:
            return True

#Runs Agent 3 on a input maze and specified fire spread probability
def runAgent3(inputMaze, fireSpreadProbability):

    dead = False
    reachedGoal = False
    inputMazeOriginal = copy.deepcopy(inputMaze)
    startFire(inputMazeOriginal, fireSpreadProbability)
    inputMazeOriginal.__getMazeArray__()[0][0] = 3
    bestPathFromFuture = getBestPathAfterFirePrediction(inputMazeOriginal,(0,0))

    while dead == False and reachedGoal == False:

        if bestPathFromFuture[1] == False:
            inputMazeOriginal.__getMazeArray__()[nextmove[0]][nextmove[1]] = 3
            dead = True
            return False

        nextmove = bestPathFromFuture[1][0]

        if nextmove == (inputMazeOriginal.__getMazeDimension__()-1,inputMazeOriginal.__getMazeDimension__()-1):
            inputMazeOriginal.__getMazeArray__()[nextmove[0]][nextmove[1]] = 3
            reachedGoal = True
            inputMazeOriginal.__getMazeArray__()[nextmove[0]][nextmove[1]] = 3
            return True

        if inputMazeOriginal.__getMazeArray__()[nextmove[0]][nextmove[1]] == 2:
            dead = True
            return False
        else:
            nextmove = bestPathFromFuture[1][0]
            inputMazeOriginal.__getMazeArray__()[nextmove[0]][nextmove[1]] = 3
            advanceFire(inputMazeOriginal)
            bestPathFromFuture = getBestPathAfterFirePrediction(inputMazeOriginal,nextmove)

#Returns the best path after simulating the maze 3 moves ahead from a specified point
def getBestPathAfterFirePrediction(maze,currentNode):

    simulationMaze = copy.deepcopy(maze)
    advanceFire(simulationMaze)
    advanceFire(simulationMaze)
    advanceFire(simulationMaze)
    BFSResults = BFS(simulationMaze, currentNode)

    if BFSResults[1] == True:

        bestPath = getBestPath(BFSResults[0])
        bestPath.reverse()
        bestPath.pop(0)
        return True,bestPath

    elif BFSResults[1] == False:
        return False,False

#Runs Agent 4 on a input maze and specified fire spread probability
def MegaMind(inputMaze, fireSpreadProbability):

    startFire(inputMaze,fireSpreadProbability)
    inputMaze.__getMazeArray__()[0][0] = 3
    inputMazeAfterMM = MegaMindFortuneTeller(inputMaze)
    inputMazeAfterMM.pop(0)

    for z in inputMazeAfterMM:
        if inputMaze.__getMazeArray__()[z[0]][z[1]] == 2:
            return False
        elif z == (inputMaze.__getMazeDimension__() - 1, inputMaze.__getMazeDimension__() - 1):
            return True
        inputMaze.__getMazeArray__()[z[0]][z[1]] = 3
        advanceFire(inputMaze)

#simulates the maze's fire spread until there's no longer a path from the start point. Then returns the last valid best path
def MegaMindFortuneTeller(maze):

    inputMaze = copy.deepcopy(maze)
    lastFutureBestPathFound = False
    lastBestFuturePath = 0

    while lastFutureBestPathFound == False:
        simulationMaze = copy.deepcopy(inputMaze)
        BFSOnSimulatedMaze = BFS(simulationMaze,(0,0))
        advanceFire(inputMaze)

        if BFSOnSimulatedMaze[1] == True:
            lastBestFuturePath = getBestPath(BFSOnSimulatedMaze[0])
            lastBestFuturePath.reverse()

        elif BFSOnSimulatedMaze[1] == False:
            return lastBestFuturePath
