
from services.BSP import BSP
from services.cellular_automata import CellularAutomata
from services.floodfill import Floodfill


class Logic:

    """Main program logic, ties everything else together, still very much work in progress
    """

    def __init__(self) -> None:
        self.mapsize = 50, 200
        self.dungeon = [[1] * (self.mapsize[1]) for _ in range(self.mapsize[0])]

    
    
    def create_map(self):
        """creates map by calling everything needed. Due to be spit up to smaller functions in later iterations. Made just to test that everything works together
        First calls BSP to divide map to sub areas, then finds the bottom layer of BSP tree (called leaves here). Calls cellular automata for each of the leaves, 
        floodfill to clean up after cellluar automata. Finally it stiches everything together and prints the map to console.  
        """
        tree = BSP(self.mapsize[0], self.mapsize[1])
        if not tree:
            print("we are not prepared for empty tree yet")
            return
        leaves_list = []
        leaves = tree.find_leaves(tree.root, leaves_list)
        try:
            for leaf in leaves:
                
                ca = CellularAutomata(leaf)
                ca.init_map()
                
                area_map = ca.carve_room()
                
                ff = Floodfill(area_map)
                n =ff.find_area()
                ff.fill_smaller(n)
                area_map = ff.map
                ah = len(area_map)
                aw = len(area_map[0])

                for y in range(ah):
                    for x in range (aw):
                    
                        self.dungeon[y + leaf.y][x+ leaf.x] = area_map[y][x]
            for y in range (len(self.dungeon)):
                line = ""
                for x in range(len(self.dungeon[0])):
                    if self.dungeon[y][x] == 1:
                        line +="#"
                    else:
                        line += "."
                print(line)
        except:
            print ("error handling yet to be implemented")        
         
    
logic = Logic()    
    
