import unittest

def values(kelvin=None, celcius=None,fahrenheit=None):
    values = [x for x in [kelvin,celcius,fahrenheit] if x]
    return len(values)

class Temperature(unittest.TestCase):
    def __init__(self, kelvin=None, celcius=None,fahrenheit=None):
        values = [x for x in [kelvin,celcius,fahrenheit] if x]
        self.assertTrue(if len(values) < 1)
            raise ValueError('Need Argument')
        if len(values) > 1:
            raise ValueError('Only one argument')
        
        if celcius is not None:
            self.kelvin = celcius + 273.15
        elif fahrenheit is not None:
            self.kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
        else:
            self.kelvin = kelvin
        
        if self.kelvin < 0:
            raise ValueError('Temperature in Kelvin cannot be negative')
    def __str__(self):
        return f'Temperature = {self.kelvin} Kelvins'
# class TestMultily(unittest.TestCase):

#     def test(self):

#         self.assertEqual(multiply(3,2),6)
if __name__ ==  "__main__":
    unittest.main()