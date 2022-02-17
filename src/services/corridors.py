from math import inf
from services.randomgen import randomgen

class Corridors:
    """Class for traversing tree of Rect entities and linking them with tunnels.
       If this seems like something slammed together in a rush,
       it is becaus thats just how it was made, will refactor later.
    """

    def __init__(self, params) -> None:
        self.turn_chance = params.turn_chance

    def dig_horizontal(self, start, end, arr, direction):
        x = start[1]
        if direction == "R":
            while x < end[1]:
                arr[start[0]][x] = 0
                turn = randomgen.random_number()
                x +=1
                if turn < self.turn_chance:
                    break
                
        else:
            while x > end[1]:
                arr[start[0]][x] = 0
                turn = randomgen.random_number()
                x -=1
                if turn < self.turn_chance:
                    break
                
        return start[0], x

    def dig_vertical(self, start, end, arr, direction):
        y = start[0]
        if direction == "D":
            while y < end[0]:
                arr[y][start[1]] = 0
                turn = randomgen.random_number()
                y +=1
                if turn < self.turn_chance:
                    break
                
        else:
            while y > end[0]:
                arr[y][start[1]] = 0
                turn = randomgen.random_number()
                y -=1
                if turn < self.turn_chance:
                    break
                
        return y, start[1]

    def link(self, rect1, rect2, arr):
        """links two rectangles with a tunnel, to keep things simple will just
           find floortiles neares to the edge and use them as star and end points.
           The method branches to two branches first taking care of rects split vertical,
           second horizontal. This method is due to get written again from scratch,
           return super().setUp()prettier next time.

        Args:
            rect1 (Rect): Rect entity
            rect2 (Rect): Rect entity
            arr (array): map that is the target of the carving
        """
        start = inf
        end = inf
        if rect1.x_2 == rect2.x:
            # dig sideways

            for x in range(rect1.x_2-1, rect1.x-1, -1):
                for y in range(rect1.y, rect1.y_2):
                    if arr[y][x] == 0:
                        start = (y, x)
                        break
                else:
                    continue
                break

            for x in range(rect2.x, rect2.x_2):
                for y in range(rect2.y, rect2.y_2):
                    if arr[y][x] == 0:
                        end = (y, x)
                        break
                else:
                    continue
                break

            if inf not in [start, end]:
                direction = "D" if start[0] < end[0] else "U"
                while start[0]!= end[0] or start[1]!=end[1]:
                    #print ("S",start,end)
                    start = self.dig_horizontal(start,end,arr,"R")
                    start = self.dig_vertical(start,end,arr,direction)
        else:
            # dig top to bottom
            for y in range(rect1.y_2-1, rect1.y-1, -1):
                for x in range(rect1.x, rect1.x_2):
                    if arr[y][x] == 0:
                        start = (y, x)
                        break
                else:
                    continue
                break
            for y in range(rect2.y, rect2.y_2):
                for x in range(rect2.x, rect2.x_2):
                    if arr[y][x] == 0:
                        end = (y, x)
                        break
                else:
                    continue
                break
            if inf not in [start, end]:
                direction = "R" if start[1] < end[1] else "L"
                while start[0]!= end[0] or start[1]!=end[1]:
                    start =self.dig_vertical(start,end,arr,"D")
                    start =self.dig_horizontal((start[0],start[1]),end,arr,direction)

    def traverse_tree(self, rect, arr):
        """Traverses tree of Rect entities and calls link function for each pair of neighbours

        Args:
            rect (Rect): Rect entity, the root of the tree to traverse
            arr (array): map that is the target of the carving, gets passed to the link function

        Returns:
            array: map with the tunnels carved
        """

      #  if not rect: This seem so be redundant Delete if nothing bad happens when it is commented out
       #     return

        if rect.child_left is None and rect.child_right is None:
            return

        self.traverse_tree(rect.child_left, arr)
        self.traverse_tree(rect.child_right, arr)
        self.link(rect.child_left, rect.child_right, arr)
        return arr
