############------------ IMPORTS ------------##################################
import unittest
import requests
import subprocess
import os

############------------ TEST(S) ------------##############################
class TestCloudFormation(unittest.TestCase):
    '''
     TODO:
        - test launch form is up-to-date
        - test launch form launches what is expected
        - test infra is resourced as expected
    '''
    def test_cf_template_existence(self):
        location = ''
        import_command = f'aws s3 cp {location}'
        subprocess.run(import_command, shell=True)
        localcheck = os.path.isfile('')
        self.assertTrue(localcheck)

    # def test_cf_template_location(self):
    #     r = requests.get(template)
    #     self.assertEqual(r.status_code,200)
    
    # def test_cf_template_url_validity(self):
    #     validation_command = f'aws cloudformation validate-template --template-url {template}'
    #     r = subprocess.run(validation_command, shell=True)
    #     self.assertNotIn('error',r)

    # def test_cf_template_body_validity(self):
    #     validation_command = f'aws cloudformation validate-template --template-body {template}'
    #     r = subprocess.run(validation_command, shell=True)
    #     self.assertNotIn('error',r)


############------------ DRIVER CODE ------------##############################ß
if __name__ == '__main__':
    unittest.main()