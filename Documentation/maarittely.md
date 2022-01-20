# Jaakko's Dungeon Generator

Jaakko's Dungeon generator is a roguelike style dungeon generator created for Datastructures Lab as a part of my computer sience studies (TKT). I chose python as a programming language for this project, because it's the language I have been mostly writing in lately. It is not known to be the fastest language of them all,but I believe that in this particular project it's performance capabilities will be sufficient. For purposes of peer-reviews I can also work with Java, but my skills in that might be a bit rusty.

Jaakko's Dungeon Generator creates a dungeon represented by 2d ascii map. It uses randomized binary space partitioning to divide a map to a set of smaller subareas. For each level of partitioning area will be split from randomized point either vertically or horizontally. If a sub area reaches minimum size set for areas, it will not be partitioned further. When predefined condition, yet to be fully planned, but most likely number of partitions, is met, program will fill these sub areas with rooms, one room per one area. 

Rooms will be generated using cellular automata to generate more organic, cave like structures. Ruleset for the automata will be clarified later, but it will start with picking random tiles to carve as floor and then turnig walls to floor and vice versa untill satifactory cavernous room is achieved. Not all rooms will reach the edges of the allocated space, so the generator will connect each room to it's parent with a corridor. Connection points will be chosen randomly from facing walls so that all of the corridors will not be straight. 

If it should happen that the room carving algorithm creates two ore more separate rooms inside one area, bigger will be spared and the smaller filled back with wall tiles.

This generator will generate a cave like structure with some rooms conected by sharing edges and some isolated rooms connected with corridors.

The user will be able to give the program parameters for dungeon generation. Scope of these will be decided at a bit later time, but atleast number of rooms and maximimum/minimum sizes will be among them.

If time permits, some dungeon features will be added, but the main priority will be in the actual room/corridor generation. 
