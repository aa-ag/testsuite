############------------ IMPORTS ------------##################################
import unittest
from time import sleep
import subprocess
import psycopg2
from models.models import User

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

    def test_db_exists(self):
        exists = 0
        try:
            sql = "SELECT datname FROM pg_catalog.pg_database WHERE lower(datname) = lower('dbname');"
            conn = psycopg2.connect(
                "credentials"
            )
            cur = conn.cursor()
            cur.execute(sql)
            result = cur.fetchall()
            exists = result
            conn.close()
        except:
            exists = 0
        self.assertNotEqual(exists, 0)
    
    def test_x_model(self):
        self.assertTrue(User.email)
    
    def test_n_attributes_model(self):
        self.assertTrue(dir(User),3)


############------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    unittest.main()