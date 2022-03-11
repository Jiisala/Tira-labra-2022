from services.randomgen import randomgen

class CellularAutomata:
    """Cellular automata to carve out rooms, parameters are defind in Params class
    """

    def __init__(self, rect, params) -> None:
        self.floor_propability = params.floor_propability
        self.wall_to_floor = params.wall_to_floor
        self.floor_to_wall = params.floor_to_wall
        self.iterations = params.iterations

        self.height = rect.y_2 - rect.y
        self.width = rect.x_2 - rect.x
        self.map = [[1] * self.width for _ in range(self.height)]

    def init_map(self):
        """Set random cells to floor
        """
        for y in range(self.height):
            for x in range(self.width):
                chance = randomgen.random_number(0, 100)
                if chance < self.floor_propability:
                    self.map[y][x] = 0

    def count_walls(self, x, y):
        """count neigbouring walls in eight directions

        Args:
            x (int): cordinate
            y (int): cordinate
        """
        walls = 0
        for new in [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, 1), (-1, -1)]:
            if (x + new[0] < 0 or
                y + new[1] < 0 or
                x + new[0] >= self.width or
                y + new[1] >= self.height):
                continue
            if self.map[(y+new[1])][x+new[0]] == 1:
                walls += 1
        return walls

    def carve_room(self):
        """Carves out cave using the parameters, set in the constructor.
        """

        for _ in range(self.iterations):
            temp_map = [[1] * self.width for _ in range(self.height)]
            for y in range(self.height):
                for x in range(self.width):
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
