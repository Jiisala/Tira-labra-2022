from params import Params
from entities.rect import Rect
from services.bsp import Bsp
from services.logic import Logic
import io
from contextlib import redirect_stdout
import unittest
class TestLogic(unittest.TestCase):
    """Test for logic class, most of the tests are just to see that
    calling of other classes work as intended.

    Args:
        unittest ([type]): [description]
    """
    
    def setUp(self) -> None:
        self.params = Params()
        self.params.map_height = 12
        self.params.map_width = 12
        self.params.min_area_height = 6
        self.params.min_area_width = 6
        self.params.stop_chance = 0
        self.params.stop_partitioning_height = 12
        self.params.stop_partitioning_width =12
        self.params.floor_propability = 0
        self.params.file_name = "testfile"
        self.params.output_to_console = 0
        self.params.output_to_file = 1
        self.logic = Logic(self.params)
        
    
    def test_call_bsp_works(self):
        test_tree= self.logic.call_bsp()

        self.assertIsNotNone(test_tree)
        self.assertIsNotNone(test_tree.tree)
        self.assertIsNotNone(test_tree.tree.child_left)
        self.assertIsNotNone(test_tree.tree.child_right)
        self.assertIsNotNone(test_tree.tree.child_left.child_right)
        self.assertIsNotNone(test_tree.tree.child_left.child_left)
        self.assertIsNotNone(test_tree.tree.child_right.child_right)
        self.assertIsNotNone(test_tree.tree.child_right.child_left)
    
    def test_create_list_of_leaves(self):
        test_tree=Bsp(self.params)
        test_leaves= self.logic.create_list_of_leaves(test_tree)
        self.assertEqual(4, len(test_leaves))

    def test_call_cellular_automata_works(self):
        test_map = self.logic.call_cellular_automata(Rect(0,0,self.params.map_width, self.params.map_height))

        self.assertEqual(test_map, [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                                    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    
    def test_call_floodfill_works(self):
        test_map = [[0,1,1,1,1,1],
                    [0,0,0,1,0,1],
                    [1,1,1,0,0,1],
                    [1,0,0,0,0,0]]
        flooded_map = self.logic.call_floodfill(test_map)

        self.assertEqual(flooded_map, [[1,1,1,1,1,1],
                                       [1,1,1,1,0,1],
                                       [1,1,1,0,0,1],
                                       [1,0,0,0,0,0]] ) 

    def test_call_corridors_work(self):
        self.logic.dungeon = [[1,1,1,1,1,1],
                              [1,0,1,1,0,1],
                              [1,0,1,1,0,1],
                              [1,0,1,1,0,1],
                              [1,0,1,1,0,1],
                              [1,1,1,1,1,1]]
        test_rect = Rect(0,0,6,6,(Rect(0,0,3,6)),Rect(3,0,6,6))
        self.logic.call_corridors(test_rect)
        
        self.assertEqual(self.logic.dungeon,[[1,1,1,1,1,1],
                                             [1,0,0,0,0,1],
                                             [1,0,1,1,0,1],
                                             [1,0,1,1,0,1],
                                             [1,0,1,1,0,1],
                                             [1,1,1,1,1,1]])

    def test_stitch_map_together_works(self):
        self.logic.dungeon = [[1,1,1,1,1,1],
                              [1,0,0,1,1,1],
                              [1,0,0,1,1,1],
                              [1,1,1,1,1,1],
                              [1,1,1,1,1,1],
                              [1,1,1,1,1,1]]
        test_map = [[1,1,1,1,1,1],
                    [1,1,1,0,0,1],
                    [1,1,1,0,0,1]]

        self.logic.stitch__map_together(Rect(0,3,6,6),test_map)
        for line in self.logic.dungeon:
            print (line)
        self.assertEqual(self.logic.dungeon, [[1, 1, 1, 1, 1, 1],
                                              [1, 0, 0, 1, 1, 1],
                                              [1, 0, 0, 1, 1, 1],
                                              [1, 1, 1, 1, 1, 1],
                                              [1, 1, 1, 0, 0, 1],
                                              [1, 1, 1, 0, 0, 1]])
    
    def test_display_map_works(self):
        """redirects the print out temporarily, for testing purposes, the split is to get rid of the screenclearing,
        I could not figure out how to get it working with the test
        """
        print_out = io.StringIO()
        with redirect_stdout(print_out): 
            self.logic.display_map()
        result = print_out.getvalue()
        just_map =result.split("J")
        
        self.assertEqual(just_map[1],"############\n############\n############\n############\n############\n############\n############\n############\n############\n############\n############\n############\n")

    def test_print_to_file_works(self):
        
        self.logic.dungeon = [[1,0,1,0],[0,1,0,1]]
        open ("./data/testfile", "w").close()
        self.logic.write_map_to_file()
        with open ("./data/testfile", "r") as testfile:
            
            assertline = testfile.read()
        test_text = (f"""

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
            \n#.#.\n.#.#\n""")    
        self.assertEqual(assertline, test_text)

    def test_create_dungeon_works(self):
        
        self.logic.create_map()
        self.assertEqual(self.logic.dungeon, [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                                              [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                                              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                              [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                                              [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                                              [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                                              [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                                              [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                                              [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                                              [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                                              [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

    def test_create_dungeon_works_no_corridors(self):
        self.logic.params.draw_corridors = 0
        self.logic.create_map()
        self.assertEqual(self.logic.dungeon, [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
                                              [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                                              [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                                              [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                                              [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                              [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                                              [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                                              [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                                              [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
                                            