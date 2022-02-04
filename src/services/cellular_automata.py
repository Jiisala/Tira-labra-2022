from services.randomgen import randomgen
from entities.rect import Rect


class CellularAutomata:
    """Cellular automata to carve out rooms, parameters are defind in Params class
    """

    def __init__(self, rect, params) -> None:
        self.floor_propability = params.floor_propability
        self.wall_to_floor = params.wall_to_floor
        self.floor_to_wall = params.floor_to_wall
        self.iterations = params.iterations

        self.h = rect.y2 - rect.y
        self.w = rect.x2 - rect.x
        self.map = [[1] * self.w for _ in range(self.h)]

    def init_map(self):
        """Set random cells to floor
        """
        for y in range(self.h):
            for x in range(self.w):
                chance = randomgen.random_number(0, 100)
                if chance < self.floor_propability:
                    self.map[y][x] = 0

    def count_walls(self, x, y):
        """count neigbourinc walls

        Args:
            x (int): cordinate
            y (int): cordinate
        """
        walls = 0
        for new in [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, 1), (-1, -1)]:
            if x + new[0] < 0 or y + new[1] < 0 or x + new[0] >= self.w or y + new[1] >= self.h:
                continue
            else:
                if self.map[(y+new[1])][x+new[0]] == 1:
                    walls += 1
        return walls

    def carve_room(self):
        """Carves out cave using the parameters, set in the constructor. 
        """

        for i in range(self.iterations):
            temp_map = [[1] * self.w for _ in range(self.h)]
            for y in range(self.h):
                for x in range(self.w):
                    walls = self.count_walls(x, y)
                    if self.map[y][x] == 1:
                        if walls > self.wall_to_floor:
                            temp_map[y][x] = 0
                        else:
                            temp_map[y][x] = 1
                    else:
                        if walls > self.floor_to_wall:
                            temp_map[y][x] = 1
                        else:
                            temp_map[y][x] = 0
            self.map = [row[:] for row in temp_map]

        return temp_map
