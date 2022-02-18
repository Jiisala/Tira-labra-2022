

class Floodfill:

    """Floodfill algorithm identifies all connected areas from a 2d map.
    The fill smaller function fills in all but the largest area.
    """

    def __init__(self, array) -> None:
        self.height = len(array)
        self.width = len(array[0])

        self.map = array

    def flood(self, start_x, start_y, number):
        """floodfill, starting from given cordinates and moving to NEWS when it can

        Args:
            start_x (int): start cordinate x
            start_y (int): start cordinate y
            number (int): number to keep track of the different areas found

        Returns:
            int: number of cells flooded
        """
        counter = 0
        queue = []
        queue.append([start_x,start_y])
        while queue:
            cell= queue.pop()
            x = cell[0]
            y = cell[1]
            self.map[y][x] = number
            for new in [(0,1),(0,-1),(1,0),(-1,0)]:
                if (x + new[0] < 0 or
                    y + new[1] <0 or
                    x + new[0] >= self.width or
                    y + new[1] >= self.height):
                    continue
                if self.map[y+new[1]][x+new[0]] != 0:
                    continue
                queue.append([x+new[0],y+ new[1]])
                counter += 1
        return counter

    def find_area(self):
        """scans the map for floorsquares and starts a floodfill when it finds one

        Returns:
            int: number to identify the largest area
        """
        number= 2
        largest = 0,0
        for y in range (self.height):
            for x in range(self.width):
                if self.map[y][x] == 0:
                    count = self.flood(x,y, number)
                    if largest[0] < count:
                        largest = count, number
                    number +=1
        return largest[1]

    def fill_smaller(self, number):
        """Fills in all areas except the largest

        Args:
            number (int): number representing the largest area found
        """
        for y in range (self.height):
            for x in range(self.width):
                if self.map[y][x] != number:
                    self.map[y][x]= 1
                else:
                    self.map[y][x]= 0
