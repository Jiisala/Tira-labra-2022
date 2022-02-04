
from services.BSP import BSP
from services.cellular_automata import CellularAutomata
from services.corridors import Corridors
from services.floodfill import Floodfill
from params import Params


class Logic:

    """Main program logic, ties everything else together, still very much work in progress
    """

    def __init__(self) -> None:
        self.params = Params()
        self.mapsize = self.params.map_height, self.params.map_width
        self.dungeon = [[1] * (self.mapsize[1])
                        for _ in range(self.mapsize[0])]

    def call_BSP(self):
        try:
            while True:

                tree = BSP(self.mapsize[0], self.mapsize[1], self.params)
                if tree.root.child_left or tree.root.child_right:
                    break
        except:
            print("error handling still in progres, error happened while calling BSP")

        return tree

    def create_list_of_leaves(self, tree):
        temp_array = []
        try:

            leaves = tree.find_leaves(tree.root, temp_array)
        except:
            print(
                "error handling still in progres, error happened while creating list of leaves")

        return leaves

    def call_cellular_automata(self, rect):
        try:
            ca = CellularAutomata(rect, self.params)
            ca.init_map()
            area_map = ca.carve_room()
        except:
            print("error handling still in progres, error happened while carving rooms")
        return area_map

    def call_floodfill(self, area_map):
        try:
            flood = Floodfill(area_map)
            area = flood.find_area()
            flood.fill_smaller(area)
            area_map = flood.map
        except:
            print(
                "error handling still in progres, error happened while calling floodfill")

        return area_map

    def carve_corridors(self, rect):
        corridors = Corridors()
        self.dungeon = corridors.traverse_tree(rect, self.dungeon)

    def stich__map_together(self, rect, area_map):
        """Stiches together the small area maps 
        """
        for y in range(len(area_map)):
            for x in range(len(area_map[0])):

                self.dungeon[y + rect.y][x + rect.x] = area_map[y][x]

    def display_map(self):
        """clears console and prints current map
        """
        print("\033c\033[3J", end='')
        for y in range(len(self.dungeon)):
            line = ""
            for x in range(len(self.dungeon[0])):
                if self.dungeon[y][x] == 1:
                    line += "#"
                else:
                    line += "."
            print(line)

    def write_map_to_file(self):
        """Placeholder for future use
        """

    def create_map(self):
        """creates map by calling everything needed. Due to be split up to smaller functions in later iterations. Made just to test that everything works together.
        First calls BSP to divide map to sub areas, then finds the bottom layer of BSP tree (called leaves here). Calls cellular automata for each of the leaves, 
        floodfill to clean up after cellluar automata. Finally it stiches everything together and prints the map to console.  
        """
        tree = self.call_BSP()

        leaves = self.create_list_of_leaves(tree)

        for leaf in leaves:
            area_map = self.call_cellular_automata(leaf)
            area_map = self.call_floodfill(area_map)

            self.stich__map_together(leaf, area_map)

        self.carve_corridors(tree.root)

        self.display_map()


logic = Logic()
