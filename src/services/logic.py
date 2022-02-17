from entities.rect import Rect
from services.bsp import Bsp
from services.cellular_automata import CellularAutomata
from services.corridors import Corridors
from services.floodfill import Floodfill
from services.filewriter import Filewriter


class Logic:

    """Main program logic, ties everything else together, still very much work in progress
    """

    def __init__(self, params) -> None:
        self.params = params
        self.mapsize = self.params.map_height, self.params.map_width
        self.dungeon = [[1] * (self.mapsize[1])
                        for _ in range(self.mapsize[0])]
        self.filewriter = Filewriter(self.params.file_name, self.params.file_path)

    def call_bsp(self):
            
        while True:
            tree = Bsp(self.params)
            if tree.tree.child_left or tree.tree.child_right:
                break    
        
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
            cellular_a = CellularAutomata(rect, self.params)
            cellular_a.init_map()
            area_map = cellular_a.carve_room()
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

    def call_corridors(self, rect):
        corridors = Corridors(self.params)
        self.dungeon = corridors.traverse_tree(rect, self.dungeon)

    def stitch__map_together(self, rect, area_map):
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

        content = (f"""

        GENERAL:
            1. Map width: {self.params.map_width}
            2. Map height: {self.params.map_height}

            BINARY SPACE PARTITIONING:  
            3. Minimum sub area width: {self.params.min_area_width}
            4. Minimum sub_area_height: {self.params.min_area_height}
            5. Stop chance: {self.params.stop_chance}
            6. Width to cease partitioning: {self.params.stop_partitioning_width}
            7. Height to cease partitioning: {self.params.stop_partitioning_height}

            CELLULAR AUTOMATA:
            8. Initial floor propability: {self.params.floor_propability}
            9. Min neighbouring walls to set wall to floor: {self.params.wall_to_floor}
            10. Min neighbouring walls to set floor to wall: {self.params.floor_to_wall} 
            11. Iterations: {self.params.iterations}  

            CORRIDORS
            12. Chance to make a turn on each step: {self.params.turn_chance}
            13. Draw corridors 1 = yes 0 = no: {self.params.draw_corridors}

            OUTPUT

            14. Output to console: {self.params.output_to_console}
            15. Output to file: {self.params.output_to_file}
            16. Path to file: {self.params.file_path}
            17. Filename: {self.params.file_name}
            
""")    
        for y in range(len(self.dungeon)):
            line = ""
            for x in range(len(self.dungeon[0])):
                if self.dungeon[y][x] == 1:
                    line += "#"
                else:
                    line += "."
            content += line + "\n"
        self.filewriter.write_to_file(content)

    def create_map(self):
        """creates map by calling everything needed.
        First calls Bsp to divide map to sub areas, then finds the bottom layer of
        Bsp tree (called leaves here). Calls cellular automata for each of the leaves,
        floodfill to clean up after cellluar automata. Finally it stitches everything
        together. Optionally it will carve tunnels and output the map to console/ file if
        those ations are allowed in settings.
        """
        tree = self.call_bsp()

        leaves = self.create_list_of_leaves(tree)
        if not leaves:
            leaves = [Rect(0,0,self.mapsize[0],self.mapsize[1])]
        for leaf in leaves:
            area_map = self.call_cellular_automata(leaf)
            area_map = self.call_floodfill(area_map)

            self.stitch__map_together(leaf, area_map)
        if self.params.draw_corridors:
            self.call_corridors(tree.root)
        if self.params.output_to_console:
            self.display_map()
        if self.params.output_to_file:
            self.write_map_to_file()

