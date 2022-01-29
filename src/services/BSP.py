
from services.randomgen import randomgen
from entities.rect import Rect



class BSP:
    """Class for the Binary space partitioning algorithm. Takes a 2d array and creates a tree of smaller subareas
    """
    def __init__(self, h,w):
        self.root = Rect(0,0,w,h)
        self.tree = self.partition(self.root)
        #print (self.tree, self.tree.child_left, self.tree.child_right)
       # print (self.count(self.tree))
        
        
        
    
    def split_area(self,rect):
        """splits given rectangle to two from randomly selected point in the long  side.
        minimum length of a side after the split is three units
        Args:
            rect (Rect): rectangle
        Returns: 
            two smaller rectangles
        """
        w = rect.x2 - rect.x
        h = rect.y2 - rect.y

        if w>h:
            splitpoint = randomgen.random_number(3,w-3)
            rect_one = Rect(rect.x,rect.y,(rect.x + splitpoint), rect.y2)
            rect_two = Rect((rect.x + splitpoint),rect.y,rect.x2, rect.y2)
        else:
            splitpoint = randomgen.random_number(3,(h-3))
            rect_one = Rect(rect.x,rect.y,rect.x2, (rect.y + splitpoint))
            rect_two = Rect(rect.x,(rect.y+splitpoint),rect.x2, rect.y2)
            
        return rect_one, rect_two
    
    def partition(self, rect):
        """takes a rectangle and partitions it to a number of smaller rectangles, returns tree of rectangles.
        Added some chaos to make the area sizes vary a bit, the mechanic sould be refined later

        Args:
            rect (Rect): Rectangles

        Returns:
            tree(Rect): tree of Rectangles
        """
        chaos= randomgen.random_number()
        if chaos > 8:
            return rect
        w = rect.x2 - rect.x
        h = rect.y2 - rect.y
        if w <6 and h <6:
            return rect
        else:
            rect_one, rect_two = self.split_area(rect)
            rect.child_left = self.partition(rect_one)
            rect.child_right = self.partition(rect_two)
        return rect            


    def find_leaves(self, rect, arr):
        """compiles the leaves of a tree of Rect entities to a list and returns said list
            Args: 
                root entitiy : Rect
                arr : array (list)
            Returns:
                list or Rect entities
        """
         
        if not rect:
            return 
        
        if rect.child_left == None and rect.child_right == None:
            arr.append(rect)
            return
        self.find_leaves(rect.child_left, arr) 
        self.find_leaves(rect.child_right, arr)
        return arr

