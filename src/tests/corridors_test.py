from services.corridors import Corridors
from entities.rect import Rect
from params import Params
import unittest

class TestCorridors(unittest.TestCase):

    def setUp(self) -> None:
        self.params = Params()
        self.params.turn_chance= 0
        self.corridors = Corridors(self.params)

    def test_corridors_horizontal_corridor(self):
        tree = Rect(0,0,8,5,Rect(0,0,4,5),Rect(4,0,8,5))
        test_map=[[1,1,1,1,1,1,1,1],
                  [1,0,0,1,1,0,0,1],
                  [1,0,0,1,1,0,0,1],
                  [1,0,0,1,1,0,0,1],
                  [1,1,1,1,1,1,1,1]]
        
        
        corr = self.corridors.traverse_tree(tree,test_map)
        
        self.assertEqual(corr,[[1,1,1,1,1,1,1,1],
                               [1,0,0,0,0,0,0,1],
                               [1,0,0,1,1,0,0,1],
                               [1,0,0,1,1,0,0,1],
                               [1,1,1,1,1,1,1,1]])
        

    def test_corridors_vertical_corridor(self):
        tree = Rect(0,0,8,5,Rect(0,0,8,3),Rect(0,3,8,5))
        test_map=[[1,1,1,1,1,1,1,1],
                  [1,0,0,0,0,0,0,1],
                  [1,1,1,1,1,1,1,1],
                  [1,0,0,0,0,0,0,1],
                  [1,1,1,1,1,1,1,1]]
        
        corr = self.corridors.traverse_tree(tree,test_map)
        
        self.assertEqual(corr,[[1,1,1,1,1,1,1,1],
                               [1,0,0,0,0,0,0,1],
                               [1,0,1,1,1,1,1,1],
                               [1,0,0,0,0,0,0,1],
                               [1,1,1,1,1,1,1,1]])
    
    def test_corridors_turning_corridor_horizontal_start(self):
        tree = Rect(0,0,8,5,Rect(0,0,4,5),Rect(4,0,8,5))
        test_map=[[1,1,1,1,1,1,1,1],
                  [1,0,0,1,1,1,1,1],
                  [1,0,0,1,1,1,1,1],
                  [1,0,0,1,1,0,0,1],
                  [1,1,1,1,1,1,1,1]]
        
        test_map2=[[1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,0,0,1],
                  [1,1,1,1,1,1,1,1],
                  [1,0,0,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1]]
        
        
        corr = self.corridors.traverse_tree(tree,test_map)
        
        self.assertEqual(corr,[[1,1,1,1,1,1,1,1],
                               [1,0,0,0,0,0,1,1],
                               [1,0,0,1,1,0,1,1],
                               [1,0,0,1,1,0,0,1],
                               [1,1,1,1,1,1,1,1]])

        corr2 = self.corridors.traverse_tree(tree,test_map2)
        self.assertEqual(corr2,[[1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,0,0,1],
                               [1,1,1,1,1,0,1,1],
                               [1,0,0,0,0,0,1,1],
                               [1,1,1,1,1,1,1,1]])

        self.corridors.turn_chance = 100
        tree = Rect(0,0,8,5,Rect(0,0,4,5),Rect(4,0,8,5))
        test_map3=[[1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,0,0,1],
                  [1,1,1,1,1,1,1,1],
                  [1,0,0,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1]]
        corr3 = self.corridors.traverse_tree(tree,test_map3)
       
        self.assertEqual(corr3,[[1,1,1,1,1,1,1,1],
                               [1,1,1,1,0,0,0,1],
                               [1,1,1,0,0,1,1,1],
                               [1,0,0,0,1,1,1,1],
                               [1,1,1,1,1,1,1,1]])

    def test_corridors_tuning_corridor_vertical_start(self):
        tree = Rect(0,0,8,5,Rect(0,0,8,3),Rect(0,3,8,5))
        test_map=[[1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,0,1],
                  [1,1,1,1,1,1,1,1],
                  [1,0,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1]]
        
        corr = self.corridors.traverse_tree(tree,test_map)
            
        self.assertEqual(corr,[[1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,0,1],
                               [1,1,1,1,1,1,0,1],
                               [1,0,0,0,0,0,0,1],
                               [1,1,1,1,1,1,1,1]])
        self.corridors.turn_chance = 100

        tree = Rect(0,0,8,5,Rect(0,0,8,3),Rect(0,3,8,5))
        
        test_map2=[[1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,0,1],
                  [1,1,1,1,1,1,1,1],
                  [1,0,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1]]
        
        corr2 = self.corridors.traverse_tree(tree,test_map2)
        
        self.assertEqual(corr2,[[1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,0,1],
                               [1,1,1,1,1,0,0,1],
                               [1,0,0,0,0,0,1,1],
                               [1,1,1,1,1,1,1,1]])
        
    def test_no_floor_wont_crash(self):
        tree = Rect(0,0,8,5,Rect(0,0,8,3),Rect(0,3,8,5))
        test_map=[[1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1]]
        corr = self.corridors.traverse_tree(tree, test_map)

        self.assertEqual(corr,[[1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1]])
        
        tree = Rect(0,0,8,5,Rect(0,0,4,5),Rect(4,0,8,5))
        
        test_map2=[[1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1],
                  [1,1,1,1,1,1,1,1]]
        corr2 = self.corridors.traverse_tree(tree, test_map2)

        self.assertEqual(corr2,[[1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1],
                               [1,1,1,1,1,1,1,1]])