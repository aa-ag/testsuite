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
    def test_cf_template_existence1(self):
        location = ''
        import_command = f'aws s3 cp {location}'
        subprocess.run(import_command, shell=True)
        localcheck = os.path.isfile('')
        self.assertTrue(localcheck)

    def test_cf_template_existence2(self):
        key, bucket = '', ''
        command = f'aws s3api head-object --bucket {bucket} --key {key}'
        output = subprocess.run(command, shell=True, capture_output=True)
        stdout_stderr = f'{output.stdout.decode("utf-8")} {output.stderr.decode("utf-8")}'
        self.assertNotIn('error', stdout_stderr.lower())


############------------ DRIVER CODE ------------##############################ß
if __name__ == '__main__':
    unittest.main()