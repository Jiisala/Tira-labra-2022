from services.randomgen import randomgen
from entities.rect import Rect

class Bsp:
    """Class for the Binary space partitioning algorithm. Takes height and width for the desired
        map size and creates a tree of smaller subareas.
        Parameters are defined in Params class.
    """

    def __init__(self,params):

        self.min_w = params.min_area_width
        self.min_h = params.min_area_height
        self.stop_chance = params.stop_chance
        self.stop_partitioning_width = params.stop_partitioning_width
        self.stop_partitioning_height = params.stop_partitioning_height
        self.root = Rect(0, 0, params.map_width, params.map_height)

        self.tree = self.partition(self.root)

    def split_area(self, rect):
        """splits given rectangle to two from randomly selected point in the long side.
        minimum length of a side after the split is defined in Params class
        Args:
            rect (Rect): rectangle
        Returns:
            two smaller rectangles
        """
        width = rect.x_2 - rect.x
        height = rect.y_2 - rect.y

        rect_one = None
        rect_two = None
        if width >= height and width >= self.stop_partitioning_width:
            splitpoint = randomgen.random_number(self.min_w, width-self.min_w)
            rect_one = Rect(rect.x, rect.y, (rect.x + splitpoint), rect.y_2)
            rect_two = Rect((rect.x + splitpoint), rect.y, rect.x_2, rect.y_2)
        elif height >= self.stop_partitioning_height:
            splitpoint = randomgen.random_number(self.min_h, height-self.min_h)
            rect_one = Rect(rect.x, rect.y, rect.x_2, (rect.y + splitpoint))
            rect_two = Rect(rect.x, (rect.y+splitpoint), rect.x_2, rect.y_2)

        return rect_one, rect_two

    def partition(self, rect):
        """takes a rectangle and partitions it to a number of smaller rectangles,
        returns tree of rectangles. Added some chaos to make the area sizes vary.
        Args:
            rect (Rect): Rectangles

        Returns:
            tree(Rect): tree of Rectangles
        """
        chaos = randomgen.random_number()
        if not rect:
            return
        if chaos < self.stop_chance:
            return rect
        width = rect.x_2 - rect.x
        height = rect.y_2 - rect.y
        if width < self.stop_partitioning_width and height < self.stop_partitioning_height:
            return rect

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
        if rect.child_left is None and rect.child_right is None:
            arr.append(rect)
            return
        self.find_leaves(rect.child_left, arr)
        self.find_leaves(rect.child_right, arr)
        return arr
