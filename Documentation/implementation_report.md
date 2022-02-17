# Implemention Report

## General structure

The program launches with launch.py which boots up the UI. The UI is a crude but sufficient text UI. It allows user to manipulate various atributes for the map creation and to output maps. All of the parameters and settings are stored in params.py file. Main engine is in the logic.py file.

When the main engine is initiated, it loads current parameters and prepares an empty map. The map is a 2D array with 1 to indicate walls and 0 for floor. When initiated it will be just full of walls. When UI calls for creation of a map, it calls various algorithms to work together and create the map. Each algorithm resides in its own class. It firs calls the BSP class to create a tree of rect entities. Rects specify an area in x/y cordinates and have up to two smaller child rect entities. It then calls BSP class again this time to create a list of leaf nodes of the tree. The leaf nodes are used to create a small portion of the map each. For each of them the program calls cellular automata and then flood fill to fill in possible blanks. The program then stiches the map together and depending of the settings, carves tunnels between all of the nodes, outputs the map to terminal and/or outputs it to a txt file (with current settings included)

## BSP (Binary Space Partitioning)

The binary space partitioning algorith takes a rect entity, that is basically just a rectangular area with up to two child entities, and partitions it to smallet areas, creating a tree in the process. It uses variety of parameters to controll the outcome. These are described in greater detail in the ![Manual](https://github.com/Jiisala/Tiralabra-2022/blob/main/Documentation/Manual.md). The algorithm starts with a rectangle same size as the area of the whole map. It then uses recursive splitting algorithm to split the area in two, split both of the halves in two... etc. Untill no rectangles bigger than the specified minimum area size remain. Rectangles geneated in each level of recursion will be assigned as children to the level above it. The rectangles are allways split so on the long side, or in the case of square horizontally. The specific point for splitting is somewhat randomized, to create areas of varying height and width. 

There is also some chaos added to force the algorithm to stop splitting before minimum size is reached. For each level of recursion random number is generated between 0 and 99, if that number is smalle than stop_chance that level of recursion will abort. The 1% chance to happen is forced because, for the dungeon generation to work, minimum of one split needs to happen. This will still generate invalid threes, but the logic will reject them later. If all of the trees would be invalid, the program would get to infinite loop.

The find_leaves function can be later to traverse the generated tree starting from the root and collect the leaves of the tree to a array. The funktion finds leaves, by traversing the tree and finding rectangles that have both of their children as None.

Time and space complexity: TBA

## Cellular automata

Cellular automata uses a bit of a different ruleset from the basic Conway s game of life. It counts neighbouring walls for each cell using what is called Moore neighbourhood, in laymans terms known as eight adjacent cells. If the cell has more than n neighbouring walls it will get converted from floor to wall or vice versa. Different n can be used for wall and floor cells. I found this method to yield aestetically pleasing shapes. The number of iterations can be controlled also, and will greatly affect the outcome. For most of the settings the algorithm will leave the edges of a area as wall, but that is not allways the case. It is also possible to generate only walls or only floors. 

The algorithms starts by creating a map of only walls, then it will go through that map and for each cell determine randomly if it will get converted to floor. Chance of that happening can be adjusted in the parameters. The actual cellular automata part of the algorithm will first make a copy of the map,then go through each cell of the area, count the neighbouring walls. Then it will determine the faith of that cell based on the number of neighbours, and if the cell is currently floor or wall. The new values get collected to the copy of the map, and at the end of each iteration changes made will get transferred to the original map. The algorithm will run as many iterations as specified in parameters. Each iteration will generate different result. Generally higher numbers will generate more "soft" looking caves, with less sigle wall blocks inside them. If number is set too high the results will not change too much compared to lower numbers and performace will plummet. It is adviced to keep number of iterations under 10. It is also possible to generate non random predetermined square, and rounded square shapes by setting the parameters right.

## Floodfill


## Corridors

Also coming soon
