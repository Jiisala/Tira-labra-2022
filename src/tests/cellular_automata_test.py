from services.cellular_automata import CellularAutomata
from entities.rect import Rect
from params import Params

import unittest

class TestCellularAutomata(unittest.TestCase):
    """Collection of tests for the cellular automata class

    """

    def setUp(self) -> None:
        self.params = Params()
        
        self.params.iterations = 1
        
    def test_init_map(self):
        self.params.floor_propability = 0
        test_CA = CellularAutomata(Rect (0,0,3,3),self.params)
        test_CA.init_map()
        self.assertEqual(test_CA.map, [[1,1,1],[1,1,1],[1,1,1]])
        test_CA.floor_propability = 100
        test_CA.init_map()
        self.assertEqual(test_CA.map, [[0,0,0],[0,0,0],[0,0,0]])

    def test_counting_walls(self):
        self.params.floor_propability = 0
        test_CA = CellularAutomata(Rect (0,0,3,3),self.params)
        test_CA.init_map()
        count = test_CA.count_walls(1,1)
        
        test_CA.floor_propability = 100
        test_CA.init_map()
        count2 = test_CA.count_walls(1,1)
        
        self.assertEqual(8,count)
        self.assertEqual(0,count2)

    def test_carve_rooms_wall_to_floor(self):
        self.params.floor_propability = 0
        self.params.wall_to_floor = 4
        self.params.floor_to_wall = 9
        test_CA = CellularAutomata(Rect (0,0,5,5),self.params)
        test_CA.init_map()
        test_map = test_CA.carve_room()
        self.params.wall_to_floor = 5
        test_CA = CellularAutomata(Rect (0,0,5,5),self.params)
        test_map2 = test_CA.carve_room()
        
        self.assertEqual(test_map, [[1, 0, 0, 0, 1],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[1, 0, 0, 0, 1]])
        self.assertEqual(test_map2, [[1, 1, 1, 1, 1],[1, 0, 0, 0, 1],[1, 0, 0, 0, 1],[1, 0, 0, 0, 1],[1, 1, 1, 1, 1]])

    def test_carve_rooms_floor_to_wall(self):
        self.params.floor_propability = 0
        self.params.wall_to_floor = 6
        self.params.floor_to_wall = 3
        self.params.iterations = 2
        test_CA = CellularAutomata(Rect (0,0,5,5),self.params)
        test_CA.init_map()
        test_map = test_CA.carve_room()
        self.params.floor_to_wall = 0
        test_CA = CellularAutomata(Rect (0,0,5,5),self.params)
        test_map2 = test_CA.carve_room()
        
        self.assertEqual(test_map, [[1, 1, 1, 1, 1],[1, 1, 0, 1, 1],[1, 0, 0, 0, 1],[1, 1, 0,1, 1],[1, 1, 1, 1, 1]])
        self.assertEqual(test_map2, [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 0, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1]])
