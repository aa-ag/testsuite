############------------ IMPORTS ------------##################################
import unittest
import os.path


############------------ TEST(S) ------------##############################
class TestDocker(unittest.TestCase):
    def test_dockerfile_exists(self):
        self.assertTrue(os.path.exists('docker/Dockerfile'))

    def test_dockerignore_exists(self):
        self.assertTrue(os.path.exists('docker/.dockerignore'))
    
    '''
    TODO: 
        CHECK https://github.com/GoogleContainerTools/container-structure-test
    '''


############------------ DRIVER CODE ------------##############################
if __name__ == "__main__":
    unittest.main()
