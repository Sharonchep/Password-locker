import unittest
from password import User,Credential
 
class TestUser(unittest.TestCase):
     def setUp(self):
         self.new_user = user("Sharon","2923")
     def tearDown(self):
         User.user_list = []
         def test_init(self):