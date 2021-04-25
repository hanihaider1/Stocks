import unittest
from experiment import Stocks #put the correct filename 

class StocksTest(unittest.TestCase):
    
    def test_init(self):
        '''
        method-- test_init
        testing if init int takes the value correctly 
        Parameters:
        self -- the current object
        return none 
        '''
        validation = Stocks("SQ (1).csv")
        value1,value2 = validation.name()
        self.assertEqual(value1[0], 276.570007)
        
def main():
    unittest.main()


main()
