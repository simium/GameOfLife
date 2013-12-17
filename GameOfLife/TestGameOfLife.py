import unittest

from GameOfLife import Cell, Universe

class GameOfLifeTests(unittest.TestCase):

    def testRule1CellIsAliveAndCellHasOneOrLessAliveNeighboursThenDies(self):
        '''
        GIVEN we have a Cell and the Cell is Alive and the Cell has One or Less Alive neighbours
        WHEN the Cell evolves
        THEN the Cell dies
        '''
        # Arrange
        cell = Cell(True,0)
        
        # Act
        cell.evolve()
        
        # Assert
        self.assertFalse(cell.isAlive)
        
        # Arrange
        cell = Cell(True,1)
        
        # Act
        cell.evolve()
        
        # Assert
        self.assertFalse(cell.isAlive)
        
    def testRule2CellIsAliveAndCellHasTwoOrThreeAliveNeighboursThenRemainsAlive(self):
        '''
        GIVEN we have a Cell and the Cell is Alive and the Cell has Two or Three Alive neighbours
        WHEN the Cell evolves
        THEN the Cell remains Alive
        '''
        # Arrange
        cell = Cell(True,2)
        
        # Act
        cell.evolve()
        
        # Assert
        self.assertTrue(cell.isAlive)
        
        # Arrange
        cell = Cell(True,3)
        
        # Act
        cell.evolve()
        
        # Assert
        self.assertTrue(cell.isAlive)
        
    def testRule3CellIsAliveAndCellHasMoreThanThreeAliveNeighboursDies(self):
        '''
        GIVEN we have a Cell and the Cell is Alive and the Cell has more than Three Alive neighbours
        WHEN the Cell evolves
        THEN the Cell dies
        '''
        # Arrange
        cell = Cell(True,4)
        
        # Act
        cell.evolve()
        
        # Assert
        self.assertFalse(cell.isAlive)
        
    def testRule4CellIsDeadAndCellHasThreeAliveNeighboursIsBorn(self):
        '''
        GIVEN we have a Cell and the Cell is Dead and the Cell has Three Alive neighbours
        WHEN the Cell evolves
        THEN the Cell is born
        '''
        # Arrange
        cell = Cell(False,3)
        
        # Act
        cell.evolve()
        
        # Assert
        self.assertTrue(cell.isAlive)
        
    def testUniverseIsCreatedWithRightDimensions(self):
        '''
        GIVEN we want a universe with M rows and N columns
        WHEN the universe is created 
        THEN the universe has exactly M*N cells
        '''
        w=4
        h=4
        universe = Universe(w,h)
        self.assertEquals(len(universe.cells)*len(universe.cells[0]), w*h)
    
    def testUniverseIsPopulatedProperly(self):
        '''
        GIVEN we want a universe with a given pattern
        WHEN the universe is populated
        THEN the universe has correct dimensions
        '''
        universe = Universe()
        
        universe.populate([[0,0,0,0],
                           [0,0,1,0],
                           [0,0,1,0],
                           [0,0,1,0],
                           [0,0,0,0]])
        
        self.assertEquals(universe.width, 4)
        self.assertEquals(universe.height, 5)
    
    def testUniverseEquality(self):
        '''
        GIVEN we create a universe with one pattern and another universe with same pattern
        WHEN we compare them
        THEN they are equals
        '''
        universe = Universe()
        
        universe.populate([[0,0,0,0,0],
                           [0,0,1,0,0],
                           [0,0,1,0,0],
                           [0,0,1,0,0],
                           [0,0,0,0,0]])
        
        another_universe = Universe()
        
        another_universe.populate([[0,0,0,0,0],
                                   [0,0,1,0,0],
                                   [0,0,1,0,0],
                                   [0,0,1,0,0],
                                   [0,0,0,0,0]])
        
        self.assertEqual(universe, another_universe)
        
    def testUniverseEvolvesCorrectlySet1(self):
        '''
        GIVEN we create a universe with Blinker pattern
        WHEN the universe evolves
        THEN the universe shows expected Blinker period
        '''
        universe = Universe()
         
        universe.populate([[0,0,0,0,0],
                           [0,0,1,0,0],
                           [0,0,1,0,0],
                           [0,0,1,0,0],
                           [0,0,0,0,0]])
        
        
        universe.evolve()
         
        postuniverse = Universe()
         
        postuniverse.populate([[0,0,0,0,0],
                               [0,0,0,0,0],
                               [0,1,1,1,0],
                               [0,0,0,0,0],
                               [0,0,0,0,0]])
        
        self.assertEqual(universe, postuniverse)
        
    def testUniverseEvolvesCorrectlySet2(self):
        '''
        GIVEN we create a universe with Toad pattern
        WHEN the universe evolves
        THEN the universe shows expected Toad period
        '''
        universe = Universe()
         
        universe.populate([[0,0,0,0,0,0],
                           [0,0,0,1,0,0],
                           [0,1,0,0,1,0],
                           [0,1,0,0,1,0],
                           [0,0,1,0,0,0],
                           [0,0,0,0,0,0]])
        
        
        universe.evolve()
         
        postuniverse = Universe()
         
        postuniverse.populate([[0,0,0,0,0,0],
                               [0,0,0,0,0,0],
                               [0,0,1,1,1,0],
                               [0,1,1,1,0,0],
                               [0,0,0,0,0,0],
                               [0,0,0,0,0,0]])
        
        self.assertEqual(universe, postuniverse)
        
    def testUniverseEvolvesContinuoslySet1(self):
        '''
        GIVEN we create a universe with Blinker pattern
        WHEN the universe evolves
        THEN the universe shows next expected Blinker period
        '''
        universe = Universe()
        universe.populate([[0,0,0,0,0],
                           [0,0,1,0,0],
                           [0,0,1,0,0],
                           [0,0,1,0,0],
                           [0,0,0,0,0]])
        
        auxuniverse = Universe()
        auxuniverse.populate([[0,0,0,0,0],
                              [0,0,1,0,0],
                              [0,0,1,0,0],
                              [0,0,1,0,0],
                              [0,0,0,0,0]])

        universe.evolve()
        
        universe.evolve()
        
        universe.evolve()
        
        universe.evolve()
        
        self.assertEqual(universe, auxuniverse)
        
    def testUniverseEvolvesContinuoslySet2(self):
        '''
        GIVEN we create a universe with Toad pattern
        WHEN the universe evolves
        THEN the universe shows next expected Toad period
        '''
        universe = Universe()
        universe.populate([[0,0,0,0,0,0],
                           [0,0,0,1,0,0],
                           [0,1,0,0,1,0],
                           [0,1,0,0,1,0],
                           [0,0,1,0,0,0],
                           [0,0,0,0,0,0]])
        
        auxuniverse = Universe()
        auxuniverse.populate([[0,0,0,0,0,0],
                              [0,0,0,0,0,0],
                              [0,0,1,1,1,0],
                              [0,1,1,1,0,0],
                              [0,0,0,0,0,0],
                              [0,0,0,0,0,0]])

        universe.evolve()
        
        universe.evolve()

        universe.evolve()
        
        universe.evolve()
        
        universe.evolve()
        
        self.assertEqual(universe, auxuniverse)
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()
