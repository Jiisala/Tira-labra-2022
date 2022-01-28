from logic import logic
class CellularAutomata:
    """Cellular automata to carve out rooms
    """

    def __init__(self, rect) -> None:
        self.floor_propability = 45
        self.to_floor = 6
        self.to_wall = 3
        self.iterations = 2
        self.map = [[1] * 13 for _ in range (6)]
        self.h = (len(self.map))
        self.w = (len(self.map[0]))
    
    def init_map(self):
        """Set random cells to floor
        """
        for y in range (self.h):
            for x in range (self.w):
                chance = logic.random_number(0,100)
                if chance < self.floor_propability:
                    self.map[y][x] = 0
    
    def count_walls(self, x,y):
        """count neigbourinc walls

        Args:
            x (int): cordinate
            y (int): cordinate
        """
        walls = 0
        for new in [(0,1),(0,-1),(1,0),(1,-1),(1,1),(-1,0),(-1,1),(-1,-1)]:
            if x + new[0] < 0 or y + new[1] <0 or x + new[0] >= self.w or y + new[1] >= self.h:
                continue
            else:
                if self.map[(y+new[1])][x+new[0]] == 1:
                    walls += 1
        return walls

    def carve_room(self):
        
        for i in range (self.iterations):
            temp_map = [[1] * 13 for _ in range (6)]
            for y in range(self.h):
                for x in range(self.w):
                    walls = self.count_walls(x,y)
                    if self.map[y][x] == 1:
                        if walls > self.to_floor:
                            temp_map[y][x] = 0
                        else:
                            temp_map[y][x] = 1    
                    else:
                        if walls > self.to_wall:
                            temp_map[y][x] = 1
                        else:
                            temp_map[y][x] = 0
            self.map = [row[:] for row in temp_map]
            for y in range (len(self.map)):
                line = ""
                for x in range(len (self.map[0])):
                    if self.map[y][x]== 1: 
                        line += "#"
                    else:
                        line += "."
                print (line)
            print()
        return temp_map         


ca = CellularAutomata(0)

ca.init_map()

for line in ca.map:
    print(line)
ca.carve_room()
print()
for y in range (len(ca.map)):
    line = ""
    for x in range(len (ca.map[0])):
        if ca.map[y][x]== 1: 
            line += "#"
        else:
            line += "."
    print (line)
