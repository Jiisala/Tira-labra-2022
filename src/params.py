from datetime import date

class Params:
    """Class to collect parameters for dungeon generations. This can be modified through settings
    menu (not yet implemented) or by manually changing them.
    """

    def __init__(self) -> None:
        """paramters grouped by the algorithm they controll
        """
        # General
        self.map_width = 150
        self.map_height = 50

        # Bsp
        self.min_area_width = 6
        self.min_area_height = 6
        self.stop_chance = 20
        self.stop_partitioning_width = 30
        self.stop_partitioning_height = 30

        # Cellular Automata
        self.floor_propability = 45
        self.wall_to_floor = 6
        self.floor_to_wall = 3
        self.iterations = 5

        # Corridors

        self.turn_chance = 50
        self.draw_corridors = 1

        # Output

        self.output_to_console = 1
        self.output_to_file = 1
        self.file_path = "./data/"
        self.file_name = str(date.today())+".txt"
        
        