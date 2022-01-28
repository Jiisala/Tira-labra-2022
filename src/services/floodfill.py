

class Floodfill:

    """Floodfill algorithm identifies all connected areas from a 2d map
    """

    def __init__(self, array) -> None:
        self.h = len(array)
        self.w = len(array[0])
        
        self.map = array
        pass
    
    def flood(self, start_x, start_y, number):
        #visited = [[False] * self.w for _ in range (self.h)]
        queue = []
        queue.append([start_x,start_y])
        while queue:
            cell= queue[-1]
            
            x = cell[0]
            y = cell[1]
            queue.remove(queue[-1])
            self.map[y][x] = number
            for new in [(0,1),(0,-1),(1,0),(-1,0)]:
                if x + new[0] < 0 or y + new[1] <0 or x + new[0] >= self.w or y + new[1] >= self.h:
                    continue
                elif self.map[y+new[1]][x+new[0]] != 0:
                    continue
                queue.append([x+new[0],y+ new[1]])    
    def find_area(self):
        number= 2
        for y in range (self.h):
            for x in range(self.w):
                
                if self.map[y][x] == 0:
                    self.flood(x,y, number)
                    number +=1


testmap = [[1,0,1,1,1,1,1,1,1,1],[0,0,0,1,1,1,1,0,0,1],[1,0,1,1,1,1,1,0,0,0],[1,1,1,1,1,1,1,1,1,0]]
for line in testmap:
    print (line)
t = Floodfill(testmap)
t.find_area()
for line in t.map:
    print (line)