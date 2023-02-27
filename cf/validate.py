############------------ IMPORTS ------------##################################
import unittest
import requests

############------------ FUNCTION(S) ------------##############################
class TestCloudFormation(unittest.TestCase):
    def test_template_location(self):
        template = ''
        r = requests.get(template)
        self.assertEqual(r.status_code,200)


############------------ DRIVER CODE ------------##############################ß
if __name__ == '__main__':
    unittest.main()