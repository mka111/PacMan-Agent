# PacMan-

The Pac-Man agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. The general search algorithms(DFS, BFS, aStar) are built and applied to Pac-Man scenarios.

The python files and their functions
```
search.py        where all of your search algorithms will reside. 
searchAgents.py  Where all of your search-based agents will reside. 
pacman.py       	The main file that runs Pac-Man games.
game.py      	   The logic behind how the Pac-Man world works.
util.py          Useful data structures for implementing search algorithms. 
```

Supporting files you can ignore:
```
graphicsDisplay.py	Graphics for Pac-Man
graphicsUtils.py	Support for Pac-Man graphics
textDisplay.py	   ASCII graphics for Pac-Man
ghostAgents.py	  Agents to control ghosts
keyboardAgents.py	Keyboard interfaces to control Pac-Man
layout.py Code for reading layout files and storing their contents
```

We have implemented search based algorithms: Depth First Search(DFS), Breadth first Search (BFS), A* graph search and search based agents: CornersProblem search and heuristic for the CornersProblem.

Use the following commands to run the files:
```
python pacman.py  (you should be able to play a game of Pac-Man using this command)
```

DFS search commands:
```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```

BFS search commands:
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

A* search commands:
```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
```

CornersProblem search commands:
```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

Heuristic for CornersProblem command:
```
python pacman.py -l mediumCorners -p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic -z 0.5
```



