import unittest
from password import User,Credential
 
class TestUser(unittest.TestCase):
     def setUp(self):
         self.new_user = user("Sharon","2923")
     def tearDown(self):
         User.user_list = []
         def test_init(self): 
             self.assertEqual(self.new_user.name, "Sharon")
             self.assertEqual(self.new_user.user_password, "2923")
         def test_save_user(self):
             self.new_user.save_user()
             self.assertEqual(len(User.user_list),1)
         def test_save_multiple_user(self):