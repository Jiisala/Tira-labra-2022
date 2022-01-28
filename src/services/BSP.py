
from logic import logic


class Rect:
    """Class for easy handling of rectangular areas 
    Args:
        corners
    """
    def __init__(self, x,y,x2,y2) -> None:
        self.x = x
        self.x2 = x2
        self.y = y
        self.y2 = y2

class BSP:
    """Class for the Binary space partitioning algorithm. Takes a 2d array and creates a tree of smaller subareas
    """
    def __init__(self, h,w):
        self.root = Rect(0,0,w,h)
        self.tree = self.partition(self.root)
        
        
    
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
            splitpoint = logic.random_number(3,w-3)
            #print (w, (w-3), splitpoint)
            rect_one = Rect(rect.x,rect.y,(rect.x + splitpoint), rect.y2)
            rect_two = Rect((rect.x + splitpoint),rect.y,rect.x2, rect.y2)
        else:
            splitpoint = logic.random_number(3,(h-3))
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
        chaos= logic.random_number()
        if chaos > 8:
            return[]
        w = rect.x2 - rect.x
        h = rect.y2 - rect.y
        if w <6 and h <6:
            return []
        else:
            rect_one, rect_two = self.split_area(rect)
            children = [rect_one,rect_two,(self.partition(rect_one)+ self.partition(rect_two))]
            return children
    
test_array = [[0]*15 for _ in range (15)]
test = BSP(100,50)

def flatten(tree):
    branches=[]
    if type(tree) == type([]):
        for t in tree:  
            branches = flatten(t) + branches
    else:
        return [tree]
    return branches

branches = flatten(test.tree)
#branches = branches[:-1]
i = 1
#for b in branches:
 #   for y in range(b.y, b.y2):
  #      for x in range(b.x, b.x2):
   #         if test_array[y][x] == 0:
    #            if len(str(i))==1:
     #               test_array[y][x] = f"0{i}"    
      #          else:
       #             test_array[y][x] = f"{i}"
                
    #i +=1
    #for line in test_array:
     #   print (line)
    #print()
#for line in test_array:
 #s   print (line)

#r1, r2 = test.split_area(Rect(0,0,9,6))
#print (r1.x,r1.y,r1.x2,r1.y2)
#print (r2.x,r2.y,r2.x2,r2.y2)        


