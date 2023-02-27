############------------ IMPORTS ------------##################################
import unittest

############------------ GLOBAL VARIABLE(S) ------------#######################
############------------ FUNCTION(S) ------------##############################
class TestCloudFormation(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual('hello world'.upper(), 'HELLO WORLD')


############------------ DRIVER CODE ------------##############################ß
if __name__ == '__main__':
    unittest.main()