from tkinter.messagebox import NO
from params import Params
from services.bsp import Bsp
import unittest

class TestBsp(unittest.TestCase):
    "Parameters imported and modified to controll randomnes from the process"

    def setUp(self) -> None:
        self.params = Params()
        self.params.stop_chance = 0
        self.params.stop_partitioning_height = 8
        self.params.stop_partitioning_width = 5
        self.params.min_area_height = 4
        self.params.min_area_width = 4

    def test_bsp_creates_tree_as_it_shoud(self):
        self.params.map_height = 8
        self.params.map_width = 4
        test_tree = Bsp(self.params)

        self.assertEqual(0, test_tree.tree.x)
        self.assertEqual(0, test_tree.tree.y)
        self.assertEqual(4, test_tree.tree.x_2)
        self.assertEqual(8, test_tree.tree.y_2)
        
        self.assertEqual(0, test_tree.tree.child_right.x)
        self.assertEqual(4, test_tree.tree.child_right.y)
        self.assertEqual(4, test_tree.tree.child_right.x_2)
        self.assertEqual(8, test_tree.tree.child_right.y_2)
        
        self.assertEqual(0, test_tree.tree.child_left.x)
        self.assertEqual(0, test_tree.tree.child_left.y)
        self.assertEqual(4, test_tree.tree.child_left.x_2)
        self.assertEqual(4, test_tree.tree.child_left.y_2)

        self.params.stop_partitioning_height = 5
        self.params.stop_partitioning_width = 8
        self.params.map_height = 4
        self.params.map_width = 8
        test_tree = Bsp(self.params)

        self.assertEqual(0, test_tree.tree.x)
        self.assertEqual(0, test_tree.tree.y)
        self.assertEqual(8, test_tree.tree.x_2)
        self.assertEqual(4, test_tree.tree.y_2)
        
        self.assertEqual(4, test_tree.tree.child_right.x)
        self.assertEqual(0, test_tree.tree.child_right.y)
        self.assertEqual(8, test_tree.tree.child_right.x_2)
        self.assertEqual(4, test_tree.tree.child_right.y_2)
        
        self.assertEqual(0, test_tree.tree.child_left.x)
        self.assertEqual(0, test_tree.tree.child_left.y)
        self.assertEqual(4, test_tree.tree.child_left.x_2)
        self.assertEqual(4, test_tree.tree.child_left.y_2)
        
        self.params.stop_partitioning_height =9
        self.params.stop_partitioning_width = 4
        self.params.min_area_height = 4
        self.params.map_height = 8
        self.params.map_width = 4
        test_tree = Bsp(self.params)

        self.assertEqual(0, test_tree.tree.x)
        self.assertEqual(0, test_tree.tree.y)
        self.assertEqual(4, test_tree.tree.x_2)
        self.assertEqual(8, test_tree.tree.y_2)
        
        self.assertIsNone(test_tree.tree.child_right)
        self.assertIsNone(test_tree.tree.child_left)
        
        

    def test_leaves_found(self):    
        self.params.map_height = 8
        self.params.map_width = 4
        test_tree = Bsp(self.params)

        test_leaves = test_tree.find_leaves(test_tree.tree, [])
        self.assertEqual(2, len(test_leaves))
    
    def test_no_leves_found_if_no_leaves_in_tree(self):
        self.params.stop_chance = 100
        self.params.map_height = 4
        self.params.map_width = 8
        test_tree = Bsp(self.params)
        test_leaves = test_tree.find_leaves(test_tree.tree, [])
        self.assertIsNone(test_leaves)

    def test_Nonetype_will_crash(self):
        self.params.map_height = 8
        self.params.map_width = 4
        test_tree= Bsp(self.params)
        none_test= test_tree.partition(None)
        self.assertIsNone(none_test)