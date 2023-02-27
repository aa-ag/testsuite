############------------ IMPORTS ------------##################################
import unittest
import requests
import subprocess

############------------ GLOBAL VARIABLE(S) ------------#######################
template = ''

############------------ FUNCTION(S) ------------##############################
class TestCloudFormation(unittest.TestCase):
    def test_cf_template_location(self):
        r = requests.get(template)
        self.assertEqual(r.status_code,200)
    
    def test_cf_template_url_validity(self):
        validation_command = f'aws cloudformation validate-template --template-url {template}'
        r = subprocess.run(validation_command, shell=True)
        self.assertNotIn('error',r)

    def test_cf_template_body_validity(self):
        validation_command = f'aws cloudformation validate-template --template-body {template}'
        r = subprocess.run(validation_command, shell=True)
        self.assertNotIn('error',r)


############------------ DRIVER CODE ------------##############################ß
if __name__ == '__main__':
    unittest.main()