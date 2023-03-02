############------------ IMPORTS ------------##################################
import unittest
from time import sleep
import subprocess
import psycopg2

############------------ TEST(S) ------------##############################
class TestDB(unittest.TestCase):
    def test_setup(self):
        command = ''
        subprocess.run(command)
        sleep(3)

    def test_db_connection(self):
        connected = 0
        try:
            conn = psycopg2.connect(
                "credentials"
            )
            conn.close()
            connected = 1
        except:
            connected = 0
        self.assertEqual(connected, 1)


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    unittest.main()