# Jaakko's Dungeon Generator

Jaakko's Dungeon generator is a roguelike style dungeon generator created for Datastructures Lab as a part of my computer sience studies (TKT). I chose python as a programming language for this project, because it's the language I have been mostly writing in lately. It is not known to be the fastest language of them all,but I believe that in this particular project it's performance capabilities will be sufficient. For purposes of peer-reviews I can also work with Java, but my skills in that might be a bit rusty.

Jaakko's Dungeon Generator creates a dungeon represented by 2d ascii map. It uses randomized binary space partitioning to divide a map to a set of smaller subareas. For each level of partitioning area will be split from randomized point either vertically or horizontally. If a sub area reaches minimum size set for areas, it will not be partitioned further. When predefined condition, yet to be fully planned, but most likely number of partitions, is met, program will fill these sub areas with rooms, one room per one area. 

Rooms will be generated using cellular automata to generate more organic, cave like structures. Ruleset for the automata will be clarified later, but it will start with picking random tiles to carve as floor and then turnig walls to floor and vice versa untill satifactory cavernous room is achieved. Not all rooms will reach the edges of the allocated space, so the generator will connect each room to it's parent with a corridor. Connection points will be chosen randomly from facing walls so that all of the corridors will not be straight. 

If it should happen that the room carving algorithm creates two ore more separate rooms inside one area, bigger will be spared and the smaller filled back with wall tiles.

This generator will generate a cave like structure with some rooms conected by sharing edges and some isolated rooms connected with corridors.

The user will be able to give the program parameters for dungeon generation. Scope of these will be decided at a bit later time, but atleast number of rooms and maximimum/minimum sizes will be among them.

If time permits, some dungeon features will be added, but the main priority will be in the actual room/corridor generation. 

Algorithms used:
For Dividing the map to sub areas I intend to use binary space partitioning. I plan on implementing it as a recursive algorithm so time and space comlexity are going to be roughly the same. Each step of the recursion generates two new leaves for the the generated tree, complexity is going to therefore be O(2^n) where n is the depth of the tree.

For the cellular automata used for cave carvig the rooms, I will use a simple algorithm to checks the neighbourhood of the current celt willl and uses a rule set specified later to determine the state of the cell. It will use Moore neighborhood, so eight cells for every cell will be inspected. I am not aware at this point if there is a named algortihm to do it and the time/space complexity eludes me. Some unforseen circumstances in life beoynd studying are getting in the way of delving deep enough in this. I will get back to in further weeks, (and I'm very open to listening to the input from the teacher in this matter). The algorithm will have to to make at least one copy of the map, but at this point I dont believe that the space complexity is going to be anything too massive.

For finding out if the sub area has one or more separate carved areas, I will use a flood fill algorihtm starting from the first cell marked as floor. When the algorithm stops it will store the number of the filled cells and check the area for any cell not yet filled. If it finds one it will start a new fill etc. until every cell is filled. It will then compare the stored numbers and fill in areas other than the largest. I plan on using a fairly simple stack based version of the algorithm. There are more optimised algorithms available, but for the scope of this project simpler will be sufficient. In the wors case scenario the algorithm needs to visit each cell of the given area, so the time clomplexity should be O(n*m) where n and m are width and length of the area.

## References for algorithms used at this point:
### Binary space partitioning
http://www.roguebasin.com/index.php?title=Basic_BSP_Dungeon_generation
https://en.wikipedia.org/wiki/Binary_space_partitioning

### Cellular automata
https://en.wikipedia.org/wiki/Cellular_automaton

### Flood fill
https://en.wikipedia.org/wiki/Flood_fill
