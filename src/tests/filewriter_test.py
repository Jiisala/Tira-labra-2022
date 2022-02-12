from services.filewriter import Filewriter
import unittest

class TestFilewriter(unittest.TestCase):

    def setUp(self) -> None:
        self.filewriter = Filewriter("testfile","./data/")

    def test_written_file_gets_written(self):
        test_line = "The god dog has OCD and only eats hod dogs"
        open ("./data/testfile", "w").close()
            
        self.filewriter.write_to_file(test_line)
        
        with open ("./data/testfile", "r") as testfile:
            
            assertline = testfile.read()
        
        self.assertEqual(assertline, test_line)

        test_line2 = "This nonsense makes no sense like a good nonsense should indeed do"

        self.filewriter.write_to_file(test_line2)

        with open ("./data/testfile", "r") as testfile:
            assertline2 = testfile.read()
        
        self.assertEqual(assertline2, test_line + test_line2)

