############------------ IMPORTS ------------##################################
import unittest
import os.path


############------------ FUNCTION(S) ------------##############################
class TestDocker(unittest.TestCase):
    def test_dockerfile_exists(self):
        self.assertTrue(os.path.exists('docker/Dockerfile'))


############------------ DRIVER CODE ------------##############################
if __name__ == "__main__":
    unittest.main()
