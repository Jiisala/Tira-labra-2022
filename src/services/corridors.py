class Corridors:
    """Class for traversing tree of Rect entities and linking them with tunnels.
       At this point digs just two straight tunnels that conect the areas.
       If this seems like something slammed together in a rush,
       it is becaus thats just how it was made will refactor later, if time permits.
    """

    def __init__(self) -> None:
        pass

    def link(self, rect1, rect2, arr):
        """links two rectangles with a tunnel, to keep things simple will just
           find floortiles neares to the edge and use them as star and end points

        Args:
            rect1 (Rect): Rect entity
            rect2 (Rect): Rect entity
            arr (array): map that is the target of the carving
        """
        start = 0, 0
        end = 0, 0

        if rect1.x_2 == rect2.x:
            # dig sideways

            for x in range(rect1.x_2-1, rect1.x, -1):
                for y in range(rect1.y, rect1.y_2-1):
                    if arr[y][x] == 0:
                        start = (y, x)
                        break
                else:
                    continue
                break

            for x in range(rect2.x+1, rect2.x_2):
                for y in range(rect2.y, rect2.y_2):
                    if arr[y][x] == 0:
                        end = (y, x)
                        break
                else:
                    continue
                break

            for x in range(start[1], end[1]+1):
                arr[start[0]][x] = 0
            for y in range(min(start[0], end[0]), max(end[0], start[0])+1):
                arr[y][end[1]] = 0
        else:
            # dig top to bottom

            for y in range(rect1.y_2-1, rect1.y, -1):
                for x in range(rect1.x, rect1.x_2):
                    if arr[y][x] == 0:
                        start = (y, x)
                        break
                else:
                    continue
                break

            for y in range(rect2.y+1, rect2.y_2):
                for x in range(rect2.x, rect2.x_2):
                    if arr[y][x] == 0:
                        end = (y, x)
                        break
                else:
                    continue
                break

            for y in range(start[0], end[0]+1):
                arr[y][start[1]] = 0
            for x in range(min(start[1], end[1]), max(end[1], start[1])+1):
                arr[end[0]][x] = 0

    def traverse_tree(self, rect, arr):
        """Traverses tree of Rect entities and calls link function for each pair of neighbours

        Args:
            rect (Rect): Rect entity, the root of the tree to traverse
            arr (array): map that is the target of the carving, gets passed to the link function

        Returns:
            array: map with the tunnels carved
        """

        if not rect:
            return

        if rect.child_left is None and rect.child_right is None:
            return

        self.traverse_tree(rect.child_left, arr)
        self.traverse_tree(rect.child_right, arr)
        self.link(rect.child_left, rect.child_right, arr)
        return arr
