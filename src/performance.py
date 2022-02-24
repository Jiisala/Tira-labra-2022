
from services.filewriter import Filewriter
from services.corridors import Corridors
from services.bsp import Bsp
from services.cellular_automata import CellularAutomata
from services.floodfill import Floodfill
from services.randomgen import RandomGen
from services.logic import Logic
from entities.rect import Rect
from params import Params
from random import randrange
from time import time
class Performance:
    """ Collection of tests for performance for each part of the program.
    Also included test for distribution of random numbers for RNG, compared 
    to the built in python randrange function.
    Running this will take a while, so despair if the computer seems to freeze. 
    The tests will be made with parameters that eliminate randomness where possible.
    Results will get written on file performance.log in data folder.
    """
    def __init__(self) -> None:
        
        self.params = Params()
        self.params.file_name = "performance.log"
        self.params.output_to_console = 0
        self.params.output_to_file = 0
        self.params.map_height = 100
        self.params.map_width = 100
        self.params.floor_propability = 0
        self.params.iterations =1
        self.params.stop_chance = 0
        self.params.turn_chance = 0
        self.params.stop_partitioning_height = 99
        self.params.stop_partitioning_width = 99
        self.params_default = self.params

        self.writer = Filewriter(self.params.file_name, self.params.file_path)
    def write_log(self, msg):
        self.writer.write_to_file(msg)
        
    def perform_bsp(self):
        """Measures time taken when making a small tree of root an two leaves
        then with a tree with four leaves. Traversal test is made with deeper tree only.
        """ 
        self.params = self.params_default 
    
        self.params.stop_partitioning_height = 101
        self.params.stop_partitioning_width = 99
        iterations = 10 **3
        
        then = time()
        for _ in range (iterations):
            shallow_tree = Bsp(self.params)
        now = time()
        result = now - then
        self.write_log(f"BSP shallow tree \n {result} seconds \n")
        
        self.params.stop_partitioning_height = 99
        self.params.stop_partitioning_width = 99
        
        iterations = 10 **3
        then = time()
        for _ in range (iterations):
            deep_tree = Bsp(self.params)
        now = time()
        result = now - then
        self.write_log(f"BSP deeper tree \n {result} seconds \n")
       
        then = time()
        iterations = 10 **3
        for _ in range (iterations):
            deep_tree.find_leaves
        now = time()
        result = now -then
        self.write_log(f"BSP traversal \n {result} seconds \n")
        

    def perform_ca(self):
        """Cellular automata is tested with floor propability of 0, to get consistent returns with minimun
        random effect
        """
        self.params = self.params_default    
        ca = CellularAutomata(Rect(0,0,100,100), self.params)
        iterations = 10**3
        then = time()
        for _ in range (iterations):
            ca.init_map
            ca.carve_room
        now = time()
        result = now -then
        self.write_log(f"Cellular automata \n {result} seconds \n")
        

    def perform_floodfill(self):
        test_map = [[1,1,0,0,1,0,0,0,1,1] * 10 for _ in range (100)]
       

        flood = Floodfill(test_map)
        iterations = 10 **3
        then = time()
        for _ in range (iterations):
            flood.find_area()
        now = time()
        result = now -then
        self.write_log(f"Floodfill \n {result} seconds \n")
        

    def perform_corridors(self):
        test_map = [[1] * 100 for _ in range (100)]
        test_map2 = [[1] * 100 for _ in range (100)]
        
        test_map[0][0] = 0
        test_map[99][99] = 0
        self.params = self.params_default
        self.params.turn_chance = 0
        corr = Corridors(self.params)
        iterations  = 10 **3
        then = time()
        for _ in range(iterations):
            corr.link(Rect(0,0,50,100),Rect(50,0,100,100),test_map)
            test_map = test_map2[::]
        now = time()
        result = now-then
        self.write_log(f"Corridors \n {result} seconds \n")
        

    def perform_rng(self):
        rng = RandomGen()
        iterations = 10 **3
        then = time()
        for _ in range(iterations):
            rng.random_number()
        now = time()
        result = now-then
        self.write_log(f"RNG peformance \n {result} seconds \n")


    def rng_distribution(self):
        rng = RandomGen()
        checklist = [0] * 100
        iterations = 10 **7
        for _ in range(iterations):
            n = rng.random_number()
            checklist[n] +=1
        result_own = max(checklist) - min(checklist)    
        self.write_log(f"RNG distribution mine (diference of most common and least common number) \n {result_own} \n")
        
        checklist2 = [0] * 100
        for _ in range(iterations):
            n = randrange(0,100)
            checklist2[n] +=1
        result_pyth = max(checklist2) - min(checklist2)    
        self.write_log(f"RNG distribution python (diference of most common and least common number) \n {result_pyth} \n")

    def perform_prog(self):
        self.params = self.params_default
        logic = Logic(self.params)
        iterations = 10 **3
        then = time()
        for _ in range (iterations):
            logic.create_map()
        now = time()
        result = now - then
        self.write_log(f"The whole program ran 1000 iterations \n {result} seconds \n")

    def run_all_tests(self):
        self.perform_bsp()
        self.perform_ca()
        self.perform_floodfill()
        self.perform_corridors()
        self.perform_rng()
        self.rng_distribution()
        self.perform_prog()           
test = Performance()
test.run_all_tests()