from services.randomgen import randomgen

class Corridors:
    """Class for traversing tree of Rect entities and linking them with tunnels.
       If this seems like something slammed together in a rush,
       it is becaus thats just how it was made. Some refactoring has happened since,
       but this will be the first thing to get rewritten if the project never evolves further.
    """

    def __init__(self, params) -> None:
        self.turn_chance = params.turn_chance

    def dig_horizontal(self, start, end, arr, direction):
        """Digs horizontal corridor untill vertical axis of end point is reached
        or random stop condition is activated

        Args:
            start (tuple(int,int)): startpoint as a tuple (y,x)
            end (tuple, int): endpoint as a tuple (y,x)
            arr (int): mapt to dig in, an 2d array of numbers
            direction (String): The direction to dig as a string "R" for left to right,
            anything else for right to left

        Returns:
            tuple(int,int): the point reached as a tuple (y,x)
        """
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
        """Digs vertical corridor untill vertical axis of end point is reached
        or random stop condition is activated

        Args:
            start (tuple(int,int)): startpoint as a tuple (y,x)
            end (tuple, int): endpoint as a tuple (y,x)
            arr (int): mapt to dig in, an 2d array of numbers
            direction (String): The direction to dig as a string "D" for top to bottom,
            anything else for bottom to top

        Returns:
            tuple(int,int): the point reached as a tuple (y,x)
        """

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
           find the row or column with floortiles nearest to the edge and randomly choose
           tiles from them to use them as start and end points.
           The method branches to two branches. First takes care of rects split vertically,
           second horizontally.

        Args:
            rect1 (Rect): Rect entity
            rect2 (Rect): Rect entity
            arr (array): map that is the target of the carving
        """

        startlist = []
        endlist = []
        if rect1.x_2 == rect2.x:
            # dig sideways

            for x in range(rect1.x_2-1, rect1.x-1, -1):
                for y in range(rect1.y, rect1.y_2):
                    if arr[y][x] == 0:
                        startlist.append((y, x))

                if startlist:
                    break

            for x in range(rect2.x, rect2.x_2):
                for y in range(rect2.y, rect2.y_2):
                    if arr[y][x] == 0:
                        endlist.append((y, x))

                if endlist:
                    break

            if startlist and endlist:
                start = startlist[randomgen.random_number(0,len(startlist))]
                end = endlist[randomgen.random_number(0,len(endlist))]
                direction = "D" if start[0] < end[0] else "U"
                while start[0]!= end[0] or start[1]!=end[1]:
                    start = self.dig_horizontal(start,end,arr,"R")
                    start = self.dig_vertical(start,end,arr,direction)
        else:
            # dig top to bottom

            for y in range(rect1.y_2-1, rect1.y-1, -1):
                for x in range(rect1.x, rect1.x_2):
                    if arr[y][x] == 0:
                        startlist.append((y, x))

                if startlist:
                    break

            for y in range(rect2.y, rect2.y_2):
                for x in range(rect2.x, rect2.x_2):
                    if arr[y][x] == 0:
                        endlist.append((y, x))

                if endlist:
                    break

            if startlist and endlist:
                start = startlist[randomgen.random_number(0,len(startlist))]
                end = endlist[randomgen.random_number(0,len(endlist))]
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

        if rect.child_left is None and rect.child_right is None:
            return

        self.traverse_tree(rect.child_left, arr)
        self.traverse_tree(rect.child_right, arr)
        self.link(rect.child_left, rect.child_right, arr)
        return arr
