"""
A quick test to try using Appium to automate the Android calculator app
"""

import unittest
from appium import webdriver


class Calculator():
    # Class to define elements of the calculator
    def __init__(self, driver):
        # Define number pad
        self.zero = driver.find_element_by_name("0")
        self.one = driver.find_element_by_name("1")
        self.two = driver.find_element_by_name("2")
        self.three = driver.find_element_by_name("3")
        self.four = driver.find_element_by_name("4")
        self.five = driver.find_element_by_name("5")
        self.six = driver.find_element_by_name("6")
        self.seven = driver.find_element_by_name("7")
        self.eight = driver.find_element_by_name("8")
        self.nine = driver.find_element_by_name("9")
        self.point = driver.find_element_by_name(".")

        # Define operation pad
        self.divide = driver.find_element_by_id("com.android.calculator2:id/op_div")
        self.multiply = driver.find_element_by_id("com.android.calculator2:id/op_mul")
        self.subtract = driver.find_element_by_id("com.android.calculator2:id/op_sub")
        self.add = driver.find_element_by_name("+")
        self.equals = driver.find_element_by_name("=")

        # Define results area
        self.result = driver.find_element_by_id("com.android.calculator2:id/formula")

        #Define symbols area
        self.lparen = driver.find_element_by_id("com.android.calculator2:id/lparen")
        self.rparen = driver.find_element_by_id("com.android.calculator2:id/rparen")


class AndroidCalculatorTests(unittest.TestCase):
    "Class to run tests against the Calculator app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.calc = Calculator(self.driver)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_addition(self):
        # Test integer addition
        self.calc.one.click()
        self.calc.add.click()
        self.calc.two.click()
        self.calc.equals.click()
        self.assertEqual((1+2), int(self.calc.result.text))
        # CLR button not displayed on startup and thus not found by id when Calculator class started.  Available now.
        self.driver.find_element_by_id("com.android.calculator2:id/clr").click()

        # Test floating point addition
        self.calc.four.click()
        self.calc.point.click()
        self.calc.four.click()
        self.calc.add.click()
        self.calc.five.click()
        self.calc.point.click()
        self.calc.five.click()
        self.calc.equals.click()
        self.assertEqual((4.4+5.5), float(self.calc.result.text))
        self.driver.find_element_by_id("com.android.calculator2:id/clr").click()

        # Test negative integer addition
        self.calc.subtract.click()
        self.calc.three.click()
        self.calc.add.click()
        self.calc.lparen.click()
        self.calc.subtract.click()
        self.calc.six.click()
        self.calc.rparen.click()
        self.calc.equals.click()
        print(self.calc.result.text)
        print(self.driver.find_elements_by_class_name("com.andriod.EditText"))
        self.assertEqual((-3+(-6)), int(self.calc.result.text))
        self.driver.find_element_by_id("com.android.calculator2:id/clr").click()

        # Test mixed floating point addition
        self.calc.subtract.click()
        self.calc.seven.click()
        self.calc.point.click()
        self.calc.eight.click()
        self.calc.add.click()
        self.calc.nine.click()
        self.calc.point.click()
        self.calc.zero.click()
        self.calc.nine.click()
        self.calc.equals.click()
        self.assertEqual((-7.8+9.09), float(self.calc.result.text))
        self.driver.find_element_by_id("com.android.calculator2:id/clr").click()

    def test_subtraction(self):
        # Test integer subtraction
        self.calc.one.click()
        self.calc.subtract.click()
        self.calc.two.click()
        self.calc.equals.click()
        self.assertEqual(str(1-2), self.calc.result.text)
        # CLR button not displayed on startup and thus not found by id when Calculator class started.  Available now.
        self.driver.find_element_by_id("com.android.calculator2:id/clr").click()

        # Test floating point subtraction
        self.calc.five.click()
        self.calc.point.click()
        self.calc.six.click()
        self.calc.subtract.click()
        self.calc.four.click()
        self.calc.point.click()
        self.calc.seven.click()
        self.calc.equals.click()
        self.assertEqual(str(5.6-4.7), self.calc.result.text)
        self.driver.find_element_by_id("com.android.calculator2:id/clr").click()

        # Test negative integer subtraction
        self.calc.subtract.click()
        self.calc.three.click()
        self.calc.subtract.click()
        self.calc.lparen.click()
        self.calc.subtract.click()
        self.calc.six.click()
        self.calc.rparen.click()
        self.calc.equals.click()
        self.assertEqual(str(-3-(-6)), self.calc.result.text)
        self.driver.find_element_by_id("com.android.calculator2:id/clr").click()

        # Test mixed floating point subtraction
        self.calc.seven.click()
        self.calc.point.click()
        self.calc.eight.click()
        self.calc.subtract.click()
        self.calc.lparen.click()
        self.calc.subtract.click()
        self.calc.nine.click()
        self.calc.point.click()
        self.calc.zero.click()
        self.calc.nine.click()
        self.calc.rparen.click()
        self.calc.equals.click()
        self.assertEqual(str(7.8-(-9.09)), self.calc.result.text)
        self.driver.find_element_by_id("com.android.calculator2:id/clr").click()

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
