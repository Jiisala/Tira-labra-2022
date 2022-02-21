from tkinter import E
from services.logic import Logic
from params import Params


class UI:

    def __init__(self) -> None:
        self.params= Params()
        self.logic = Logic(self.params)
        
    
    def settings(self):
        new_params = self.params
        message= ""
        error_message = "NOT A VALID VALUE, TRY AGAIN!"
        success_message = "VALUE CHANGED!"
        while True:
            
            print("\033c\033[3J", end='')
            print()
            print (f"""Current settings:
            
            GENERAL:
            1. Map width: {self.logic.params.map_width}
            2. Map height: {self.logic.params.map_height}

            BINARY SPACE PARTITIONING:  
            3. Minimum sub area width: {self.logic.params.min_area_width}
            4. Minimum sub_area_height: {self.logic.params.min_area_height}
            5. Stop chance: {self.logic.params.stop_chance}
            6. Width to cease partitioning: {self.logic.params.stop_partitioning_width}
            7. Height to cease partitioning: {self.logic.params.stop_partitioning_height}

            CELLULAR AUTOMATA:
            8. Initial floor propability: {self.logic.params.floor_propability}
            9. Min neighbouring walls to set wall to floor: {self.logic.params.wall_to_floor}
            10. Min neighbouring walls to set floor to wall: {self.logic.params.floor_to_wall} 
            11. Iterations: {self.logic.params.iterations}  

            CORRIDORS
            12. Chance to make a turn on each step: {self.logic.params.turn_chance}
            13. Draw corridors: {self.logic.params.draw_corridors}
            
            OUTPUT

            14. Output to console: {self.logic.params.output_to_console}
            15. Output to file: {self.logic.params.output_to_file}
            16. Path to file: {self.logic.params.file_path}
            17. Filename: {self.logic.params.file_name}
            
            To change a setting enter index of the value you want to change 
            
            ___[1->17]_____[C]reate_____[B]ack___
            
            {message}
            """)
            
            try:
                next = input("> ").lower()
             
                if next == "b":
                    break   
                if next == "c":
                    self.logic.create_map()
                    break
                
                if next == "1":
                    print("""Map width: positive integer,
setting, both width and height smaller than BSP dimensions will cause problems""")
                    print()
                    value = int(input("New value: "))
                    if value < 0 or (value < new_params.stop_partitioning_width 
                    and new_params.map_height < new_params.stop_partitioning_height):
                        message = error_message
                        
                    else:
                        new_params.map_width = value    
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "2":
                    print("""Map height: positive integer,
setting, both width and height smaller than BSP dimensions will cause problems""")
                    print()
                    value = int(input("New value: "))
                    if value < 0 or (value < new_params.stop_partitioning_height 
                    and new_params.map_width < new_params.stop_partitioning_width):
                        message = error_message
                    else:
                        new_params.map_height = value
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "3":

                    print("""Minimum width of a sub area: positive integer,
setting, larger than half of Width to stop partitioning will cause problems""")
                    print()
                    value = int(input("New value: "))
                    if value < 0 or value > (new_params.stop_partitioning_width //2):
                        message = error_message
                    else:
                        new_params.min_area_width = value    
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "4":
                    print("""Minimum height of a sub area: positive integer,
setting, larger than half of Height to stop partitioning will cause problems""")
                    print()
                    value = int(input("New value: "))
                    if value < 0 or value > (new_params.stop_partitioning_height //2):
                        message = error_message
                    else:
                        new_params.min_area_height = value    
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "5":
                    print("Stop chance: integer between 0 and 99")
                    print()
                    value = int(input("New value: "))
                    if value not in range(100):
                        message = error_message
                    else:
                        new_params.stop_chance = value    
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "6":
                    print("""Width to stop partitioning: positive integer,
setting smaller than twice the minimum width of a subarea will cause problems,
as will setting both stop partitioning height and width larger than map dimension """)
                    print()
                    value = int(input("New value: "))
                    if value < 0 or value < (new_params.min_area_width *2):
                        message = error_message
                    else:
                        new_params.stop_partitioning_width = value    
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "7":
                    print("""Height to stop partitioning: positive integer,
setting smaller than twice of minimum height of a subarea will cause problems,
as will setting both stop partitioning height and width larger than map dimension """)
                    print()
                    value = int(input("New value: "))
                    if value < 0 or value < (new_params.min_area_height *2):
                        message = error_message
                    else:    
                        new_params.stop_partitioning_height = value    
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "8":
                    print("Floor propability: Integer between 0 and 100")
                    print()
                    value = int(input("New value: "))
                    if value not in range(101):
                        message = error_message
                    else:
                        new_params.floor_propability = value    
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "9":
                    print("Min neighbouring walls to set wall to foor: Integer between 0 and 9 (9 = never)")
                    print()
                    value = int(input("New value: "))
                    if value not in range(10):
                        message = error_message
                    else:    
                        new_params.wall_to_floor = value    
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "10":
                    print("Min neighbouring walls to set to foor wall: Integer between 0 and 9 (9 = never")
                    print()
                    value = int(input("New value: "))
                    if value not in range (10):
                        message = error_message
                    else:    
                        new_params.floor_to_wall = value    
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "11":
                    print("Iterations of cellular automata: Integer above zero")
                    print()
                    value = int(input("New value: "))
                    if value < 0:
                        message = error_message
                    else:
                        new_params.iterations = value    
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "12":
                    print("Chance to make a turn on each step: Integer between 0 and 100")
                    print()
                    value = int(input("New value: "))
                    if value not in range (101):
                        message = error_message
                    else:
                        new_params.turn_chance = value    
                        self.logic = Logic(new_params)
                        message = success_message
                if next == "13":
                    print("Draw corridors: Boolean(integer): 0 for false, everything else will evaluate true")
                    print()
                    value = int(input("New value: "))
                    new_params.draw_corridors = value
                    self.logic = Logic(new_params)    
                    message = success_message

                if next == "14":
                    print("Output to console: Boolean(integer): 0 for false, everything else will evaluate true")
                    print()
                    value = int(input("New value: "))
                    new_params.output_to_console = value
                    self.logic = Logic(new_params)
                    message = success_message

                if next == "15":
                    print("Output to file: Boolean(integer): 0 for false, everything else will evaluate true")
                    print()
                    value = int(input("New value: "))
                    new_params.output_to_file = value
                    self.logic = Logic(new_params)
                    message = success_message        
                if next == "16":
                    print("Path to file, for now please use relative path to src folder")
                    print()
                    value = input("New path: ")
                    new_params.file_path = value
                    self.logic = Logic(new_params)
                    message = success_message        
                if next == "17":
                    print("""Name of the output file. If file exists, new text will be appended,
if not, file will be created to specified path""")
                    print()
                    value = input("New value: ")
                    new_params.file_name = value
                    self.logic = Logic(new_params)
                    message = success_message        
            except:
                message = error_message
    def start(self):
        print("\033c\033[3J", end='')
        
        logo = (">v<                                            ",
                "_+_____________________________________________, ",
                " | *      *               *    *      *** **  *| ",
                " |  *  *    **      *           *        *   * |  ",
                " |   *       JAAKKO's       * *    *        *  |   ",
                " |     **          DUNGEON  *   ** *   *** *   +-=-> ",
                " |   *      GENERATOR  *      *    *   *  *    |   ",
                "\| * *     *                *       * * *      |  ",
                " L__________________________________be amazed _|  ",
                "  \                                             ",
                "              Lets go go go!                   ",
                "                                              ")
                
        for row in logo:
            print(row)

        print()
        while True:
            print()
            print("___[C]reate_____[S]ettings_____[Q]uit___")
            print()
            next = input(">").lower()
            if next == "q":
                break
            if next == "c":
                self.logic.create_map()
            if next == "s":
                self.settings()


ui = UI()
