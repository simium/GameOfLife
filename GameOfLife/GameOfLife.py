class Universe:
    def __init__(self, width=16, height=16, isFiniteWorld=False):
        self.isFiniteWorld = isFiniteWorld
        self.width = width
        self.height = height
        self.cells = [[Cell() for j in range(self.width)] for i in range(self.height)]
        self.futurecells = [[Cell() for j in range(self.width)] for i in range(self.height)]
        self.bitmap = [[0 for j in range(self.width)] for i in range(self.height)]
        self.recalculateBitmap()
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.width == other.width
                and self.height == other.height
                 and self.cells == other.cells)
    
    def __repr__(self):
        matrixstr = ''
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j].isAlive:
                    matrixstr += 'X'
                else:
                    matrixstr += 'O'
            matrixstr += '\n'
        return matrixstr
    
    def evolve(self):
        for i in range(self.height):
            for j in range(self.width):
                self.futurecells[i][j].numberOfAliveNeighbours = self.getNumberOfNeighbours(i,j)
                self.futurecells[i][j].isAlive = self.cells[i][j].isAlive
                
                self.futurecells[i][j].evolve()
        
        for i in range(self.height):
            for j in range(self.width):
                self.cells[i][j].isAlive = self.futurecells[i][j].isAlive
        
        self.recalculateNeighbours()
        
        self.recalculateBitmap()
                
        return
    
    def populate(self, bitmap):        
        self.width  = len(bitmap[0])
        self.height = len(bitmap)

        self.cells = [[Cell() for j in range(self.width)] for i in range(self.height)]
        self.futurecells = [[Cell() for j in range(self.width)] for i in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                if bitmap[i][j] == 1:
                    self.cells[i][j] = Cell(True,0)
                    self.futurecells[i][j] = Cell(True,0)
                else:
                    self.cells[i][j] = Cell(False,0)
                    self.futurecells[i][j] = Cell(False,0)
        
        self.recalculateNeighbours()
        
        self.recalculateBitmap()
        
        return
    
    def getNumberOfNeighbours(self, i, j):
        res = 0
        validNeighbours = []

        if self.isFiniteWorld:
            if i==0:
                if j == 0:
                    validNeighbours = [self.cells[i][j+1],
                                       self.cells[i+1][j], self.cells[i+1][j+1]]
                elif j > 0 and j < self.width-1:
                    validNeighbours = [self.cells[i][j-1], self.cells[i][j+1],
                                       self.cells[i+1][j-1], self.cells[i+1][j], self.cells[i+1][j+1]]
                elif j == self.width-1:
                    validNeighbours = [self.cells[i][j-1],
                                       self.cells[i+1][j-1], self.cells[i+1][j]]
            elif i > 0 and i < self.height-1:
                if j == 0:
                    validNeighbours = [self.cells[i-1][j], self.cells[i-1][j+1],
                                       self.cells[i][j+1],
                                       self.cells[i+1][j], self.cells[i+1][j+1]]
                elif j > 0 and j < self.width-1:
                    validNeighbours = [self.cells[i-1][j-1],self.cells[i-1][j], self.cells[i-1][j+1],
                                       self.cells[i][j-1], self.cells[i][j+1],
                                       self.cells[i+1][j-1], self.cells[i+1][j], self.cells[i+1][j+1]]
                elif j == self.width-1:
                    validNeighbours = [self.cells[i-1][j-1],self.cells[i-1][j],
                                       self.cells[i][j-1],
                                       self.cells[i+1][j-1],self.cells[i+1][j]]
            elif i == self.height-1:
                if j == 0:
                    validNeighbours = [self.cells[i-1][j],
                                       self.cells[i-1][j+1], self.cells[i][j+1]]
                elif j > 0 and j < self.width-1:
                    validNeighbours = [self.cells[i][j-1], self.cells[i-1][j-1],
                                       self.cells[i-1][j], self.cells[i-1][j+1], self.cells[i][j+1]]
                elif j == self.width-1:
                    validNeighbours = [self.cells[i-1][j-1],
                                       self.cells[i-1][j], self.cells[i][j-1]]
        else:      
            if i==0:
                if j == 0:
                    validNeighbours = [self.cells[self.height-1][self.width-1], self.cells[self.height-1][j], self.cells[self.height-1][j+1],
                                       self.cells[0][self.width-1], self.cells[0][j+1],
                                       self.cells[1][self.width-1], self.cells[1][j], self.cells[1][j+1]]
                elif j > 0 and j < self.width-1:
                    validNeighbours = [self.cells[self.height-1][j-1], self.cells[self.height-1][j], self.cells[self.height-1][j+1],
                                       self.cells[0][j-1], self.cells[0][j+1],
                                       self.cells[1][j-1], self.cells[1][j], self.cells[1][j+1]]
                elif j == self.width-1:
                    validNeighbours = [self.cells[self.height-1][j-1], self.cells[self.height-1][j], self.cells[self.height-1][0],
                                       self.cells[0][j-1], self.cells[0][0],
                                       self.cells[1][j-1], self.cells[1][j], self.cells[1][0]]
            elif i > 0 and i < self.height-1:
                if j == 0:
                    validNeighbours = [self.cells[i-1][self.width-1],self.cells[i-1][j], self.cells[i-1][j+1],
                                       self.cells[i][self.width-1], self.cells[i][j+1],
                                       self.cells[i+1][self.width-1], self.cells[i+1][j], self.cells[i+1][j+1]]
                elif j > 0 and j < self.width-1:
                    validNeighbours = [self.cells[i-1][j-1],self.cells[i-1][j], self.cells[i-1][j+1],
                                       self.cells[i][j-1], self.cells[i][j+1],
                                       self.cells[i+1][j-1], self.cells[i+1][j], self.cells[i+1][j+1]]
                elif j == self.width-1:
                    validNeighbours = [self.cells[i-1][j-1],self.cells[i-1][j],self.cells[i-1][0],
                                       self.cells[i][j-1],self.cells[i][0],
                                       self.cells[i+1][j-1],self.cells[i+1][j],self.cells[i+1][0]]
            elif i == self.height-1:
                if j == 0:
                    validNeighbours = [self.cells[i-1][self.width-1],self.cells[i-1][j],self.cells[i-1][j+1],
                                       self.cells[i][self.width-1],self.cells[i][j+1],
                                       self.cells[0][self.width-1],self.cells[0][0],self.cells[0][1]]
                elif j > 0 and j < self.width-1:
                    validNeighbours = [self.cells[i-1][j-1],self.cells[i-1][j], self.cells[i-1][j+1],
                                       self.cells[i][j-1],self.cells[i][j+1],
                                       self.cells[0][j-1],self.cells[0][j], self.cells[0][j+1]]
                elif j == self.width-1:
                    validNeighbours = [self.cells[i-1][j-1],self.cells[i-1][j],self.cells[i-1][0],
                                       self.cells[i][j-1],self.cells[i][0],
                                       self.cells[0][j-1],self.cells[0][j],self.cells[0][0]]
        
        for cell in validNeighbours:
            if cell.isAlive:
                res += 1
                
        return res
    
    def recalculateNeighbours(self):
        for i in range(self.height):
            for j in range(self.width):
                self.cells[i][j].numberOfAliveNeighbours = self.getNumberOfNeighbours(i,j)
        
    
    def recalculateBitmap(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j].isAlive:
                    self.bitmap[i][j] = 1
                else:
                    self.bitmap[i][j] = 0
        

class Cell:
#     isAlive = False
#     numberOfAliveNeighbours = 0
    
    def __init__(self, isAlive=False, numberOfAliveNeighbours=0):
        self.isAlive = isAlive
        self.numberOfAliveNeighbours = numberOfAliveNeighbours
        
    def __repr__(self):
#         return '%d' % self.numberOfAliveNeighbours
        if self.isAlive:
            return 'X'
        else:
            return ' '
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.isAlive == other.isAlive
                and self.numberOfAliveNeighbours == other.numberOfAliveNeighbours)
        
    def evolve(self):
        if self.isAlive:
            if self.numberOfAliveNeighbours <= 1:
                self.isAlive = False
            elif self.numberOfAliveNeighbours == 2 or self.numberOfAliveNeighbours == 3:
                self.isAlive = True
            elif self.numberOfAliveNeighbours > 3:
                self.isAlive = False
        else:
            if self.numberOfAliveNeighbours == 3:
                self.isAlive = True
        return
