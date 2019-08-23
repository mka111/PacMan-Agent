# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
num_hours_i_spent_on_this_assignment = 13
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>

"""
#Most interesting -> A* search
#have trouble understanding the vaccum cleaner world topic
#####################################################
#####################################################



"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from queue import LifoQueue
from collections import deque

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Questoin 1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    print (problem.isGoalState(problem.getStartState()) )
    print ( problem.getSuccessors(problem.getStartState()) )

    """
    "*** YOUR CODE HERE ***"
    #import Queue
    begin_node = problem.getStartState()
    visited_Nodes = []
    path =[]
    queue=[]
    visited_Nodes.append(begin_node)
    queue.append((begin_node, path))
    #print(queue)
    #print(len(queue))
    #print(queue)
    #if problem.isGoalState(startNode):
    #    return path

    while len(queue) != 0:
        node = queue.pop()
        #print("nodeee",node)
        #print(queue)
        #print("direction", node[1])
        visited_Nodes.append(node[0])

        if problem.isGoalState(node[0]):
            #print(paths)
            return paths
        #    return path + [node[1]]
            #return paths

        NodeSuccessor = problem.getSuccessors(node[0])
        for n in NodeSuccessor:
            if n[0] not in visited_Nodes:
                visited_Nodes.append(n[0])
                #if problem.isGoalState(n[0]):
                #    return path + [n[1]]
                    #return paths
                #paths = path + [n[1]]
                side = n[1]
                #paths.append((node[1],[side]
                paths = node[1]+[side]
                queue.append((n[0], paths))
    #print("pathhhh",paths)
    return paths

def breadthFirstSearch(problem):
    """Questoin 1.2
     Search the shallowest nodes in the search tree first.
     """
    "*** YOUR CODE HERE ***"
    begin_node = problem.getStartState()
    visited_Nodes = []
    path =[]
    queue=[]
    visited_Nodes.append(begin_node)
    queue.append((begin_node, path))
    #print(queue)
    #print(len(queue))
    #print(queue)
    #if problem.isGoalState(startNode):
    #    return path

    while len(queue) != 0:
        node = queue.pop(0)
        #print("nodeee",node)
        #print(queue)
        #print("direction", node[1])
        visited_Nodes.append(node[0])

        if problem.isGoalState(node[0]):
            #print(paths)
            return node[1]
        #    return path + [node[1]]
            #return paths

        NodeSuccessor = problem.getSuccessors(node[0])
        for n in NodeSuccessor:
            if n[0] not in visited_Nodes:
                visited_Nodes.append(n[0])
                #if problem.isGoalState(n[0]):
                #    return path + [n[1]]
                    #return paths
                #paths = path + [n[1]]
                side = n[1]
                #paths.append((node[1],[side]
                paths = node[1]+[side]
                queue.append((n[0], paths))
    #print("pathhhh",paths)
    return paths



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Question 1.3
    Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    begin_node = problem.getStartState()
    visited_Nodes = []
    path =[]
    queue=util.PriorityQueue()
    costForNode = 0
    priority = heuristic(begin_node, problem) + costForNode
    queue.push((begin_node, path, 0), priority)
    #visited_Nodes.append(begin_node)
    #queue.append((begin_node, path))

    while not queue.isEmpty():
        node = queue.pop()
        #print("nodeee",node)
        #print(queue)
        #print("direction", node[1])
        #visited_Nodes.append(node[0])
        if problem.isGoalState(node[0]):
            #print(paths)
            return node[1]
        if node[0] not in visited_Nodes:
            NodeSuccessor = problem.getSuccessors(node[0])



            for n in NodeSuccessor:
                #visited_Nodes.append(n[0])
                costForNode = node[2] + n[2]
                side= n[1]
                paths = node[1]+[side]

                priority = heuristic(n[0], problem) + costForNode
                queue.push((n[0], paths, costForNode), priority)
        visited_Nodes.append(node[0])
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
