import unittest
from final_stocks import Stocks

class StocksTest(unittest.TestCase):
    
    def test_init(self):
        '''
        method-- test_init
        testing if init int takes the value correctly 
        Parameters:
        self -- the current object
        return none 
        '''
        validation = Stocks("PYPL.csv")
        value1,value2 = validation.name()
        self.assertEqual(value1[0], 304.790009)
        self.assertEqual(value1[1], 34.200001)
        self.assertEqual(value1[2], 110.150002)
        self.assertEqual(value1[3], 86.68)
        
    def test_init2(self):
        '''
        method-- test_init
        testing if init int takes the value correctly 
        Parameters:
        self -- the current object
        return none 
        '''
        validation = Stocks("PYPL.csv","SQ (1).csv")
        value1,value2 = validation.stock()
        self.assertEqual(value1[0], 304.790009)
        self.assertEqual(value1[1], 34.200001)
        self.assertEqual(value1[2], 110.150002)
        self.assertEqual(value2[0], 276.570007)
        self.assertEqual(value2[1], 38.09)
        self.assertEqual(value2[2], 57.040001000000004)
        
        
    def test_init3(self):
        validation = Stocks("PYPL.csv")
        with self.assertRaises(AttributeError):
            validation.comparing_summary()
            
        
      
        
def main():
    unittest.main()
    
    


main()
