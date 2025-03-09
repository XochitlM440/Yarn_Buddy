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
        expected = {"24/7 Cotton": 5.99,"Hometown": 5.99,"Coboo": 5.99,
                    "Baby Soft": 7.99,"Go for Faux": 7.99,'Heartland': 6.99,"Landscapes": 6.99,"Wool-Ease Aire": 7.99,"Hue + Me Yarn": 7.99,
                    "Color Theory": 6.99,"Ice Cream": 5.99,"Touch of Alpaca": 6.99,"Pima Cotton": 7.49,"Jeans": 6.99,
                    "Off The Hook": 5.99}
        result = Functions.price_range(catalog.reduced_cat,input1,input2)
        self.assertEqual(expected,result)

    def test_yardage_range1(self):
        input1 = 300
        input2 = 1500
        expected = {"Pound of Love": 1020,"Mandala": 590}
        result = Functions.yardage_range(catalog.short_cat,input1,input2)
        self.assertEqual(expected,result)

    def test_yardage_range2(self):
        input1 = 500
        input2 = 1000
        expected = {"Mandala": 590,"Cover Story": 547,"Bundle of Love": 688,"Re-Up Bonus Bundle": 651}
        result = Functions.yardage_range(catalog.reduced_cat,input1,input2)
        self.assertEqual(expected,result)

    def test_yarn_quant1(self):
        input1 = 20
        input2 = 1000
        expected = {"Pound of Love": '1 for $13.99, 1020 yards',"Ferris Wheel": '4 for $19.96, 1080 yards',"Mandala": '2 for $17.98, 1180 yards'}
        result = Functions.yarn_quantity(catalog.short_cat,input1,input2)

    def test_yarn_quant2(self):
        input1 = 15
        input2 = 900
        expected = {"Pound of Love": '1.0 for $13.99, 1020.0 yards'}
        result = Functions.yarn_quantity(catalog.reduced_cat,input1,input2)
        self.assertEqual(expected,result)