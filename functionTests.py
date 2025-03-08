import Functions
import unittest
import catalog

# price range, yardage range, yarn quantity
class TestCases(unittest.TestCase):
    def test_price_range1(self):
        input1 = 0
        input2 = 10
        expected = {"Ferris Wheel": 4.99,"Mandala": 8.99}
        result = Functions.price_range(catalog.short_cat,input1,input2)
        self.assertEqual(expected,result)

    def test_price_range2(self):
        input1 = 5
        input2 = 8
        expected = {"24/7 Cotton": 5.99,"Ferris Wheel": 4.99, "Hometown": 5.99, "Coboo": 5.99, "Feels Like Butta": 4.99,
                    "Baby Soft": 7.99, "Go for Faux": 7.99, "Landscapes": 6.99, "Wool-Ease Aire": 7.99, "Hue + Me Yarn": 7.99,
                    "Color Theory": 6.99, "Ice Cream": 5.99, "Touch of Alpaca": 6.99, "Pima Cotton": 7.49, "Jeans": 6.99,
                    "Stitch Soak Scrub": 3.99, "Off The Hook": 5.99}
        result = Functions.price_range(catalog.reduced_cat,input1,input2)
        self.assertEqual(expected,result)
