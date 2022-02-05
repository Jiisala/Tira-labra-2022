
from services.floodfill import Floodfill
import unittest

class TestFloodfill(unittest.TestCase):

    def setUp(self) -> None:
        
        self.test_map1 = [[1,1,1,1,1,1,1,1,1,1],
                          [1,0,0,1,1,1,1,1,1,1],
                          [1,0,0,1,1,1,0,0,1,1],
                          [1,1,1,1,1,1,0,0,1,1],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1]]
        
        self.test_map2 = [[1,1,0,1,1,1,1,1,1,1],
                          [1,0,0,0,1,1,1,1,1,1],
                          [0,0,0,1,1,1,0,0,1,1],
                          [1,0,1,1,1,1,0,0,1,0],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,0,1,1]]
        
        self.test_map3 = [[0,1,0,1,1,1,1,1,1,1],
                          [1,0,0,0,1,1,1,1,1,1],
                          [0,0,0,0,0,0,0,0,1,1],
                          [1,0,1,1,1,1,0,0,1,0],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,0,1,1]]
        
        self.test_map4 = [[1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1]]

    
        
    def test_find_all_areas(self):
        ff = Floodfill(self.test_map1)
        ff.find_area()
        map = ff.map
        self.assertEqual(map, [[1,1,1,1,1,1,1,1,1,1],
                          [1,2,2,1,1,1,1,1,1,1],
                          [1,2,2,1,1,1,3,3,1,1],
                          [1,1,1,1,1,1,3,3,1,1],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1]])

    def test_find_lasrgest_area(self):
        ff = Floodfill(self.test_map2)
        largest= ff.find_area()
        ff = Floodfill(self.test_map3)
        largest2= ff.find_area()
        
        self.assertEqual(largest, 2)
        self.assertEqual(largest2, 3)

    def test_no_areas_to_find(self):
        ff = Floodfill(self.test_map4)
        ff.find_area()
        map = ff.map
        self.assertEqual(map, [[1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1]])
    
    def test_fill_leaves_only_largest(self):
        ff = Floodfill(self.test_map3)
        largest = ff.find_area()
        ff.fill_smaller(largest)
        map = ff.map
        self.assertEqual(map, [[1,1,0,1,1,1,1,1,1,1],
                          [1,0,0,0,1,1,1,1,1,1],
                          [0,0,0,0,0,0,0,0,1,1],
                          [1,0,1,1,1,1,0,0,1,1],
                          [1,1,1,1,1,1,1,1,1,1],
                          [1,1,1,1,1,1,1,1,1,1]])
