############------------ IMPORTS ------------##################################
import unittest
from time import sleep
import subprocess

############------------ TEST(S) ------------##############################
class TestDB(unittest.TestCase):
    def test_setup(self):
        command = ''
        subprocess.run(command)
        sleep(3)



############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    unittest.main()