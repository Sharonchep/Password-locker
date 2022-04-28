import unittest
from password import User,Credential
 
class TestUser(unittest.TestCase):
     def setUp(self):
         self.new_user = user("sharon","3245")
     def tearDown(self):
         User.user_list = []
         def test_init(self):
             self.assertEqual(self.new_user.name, "sharon")
             self.assertEqual(self.new_user.user_password, "3245")
         def test_save_user(self):
             self.new_user.save_user()
             self.assertEqual(len(User.user_list),1)
         def test_save_multiple_user(self):
             self.name_user.save_user()
             test_user = user("sharon", "1234")
             test_user.save_user()
             self.assertEqual(len(User.user_list), 2)
         def test_delete_user(self):
             self.new_user.save_user()
             test_user = user("sharon", "1234")
             test_user.save_user()

             self.new_user.delete_user()
             self.assertEqual(len(User.user_list), 1)
    
class TestCredential(unittest.TestCase):
         def setUp(self):
             self.new_credential = credential("facebook", "Korir", "12345")
         def tearDown(self):
             Credential.credential_list = []
         def test_init(self):
                 self.assertEqual(self.new_credential.account, "facebook")
                 self.assertEqual(self.new_credential.account_username, "Korir")
                 self.assertEqual(self.new_credential.account_password, "12345")
         def test_save_credential(self):
                 self.new_credential.save_credential()
                 self.assertEqual(len(Credential.credential_list), 1)
         def test_save_multiple_credential(self):
                 test_credential = credential("twitter", "Kemei", "0000")
                 test_credential.save_credential()
                 self.assertEqual(len(Credential.credential_list), 2)
         def test_delete_credential(self):
             self.new_credential.save_credential(self)
             test_credential = credential("twitter", "Kemei", "0000")
             test_credential.save_credential()

             self.new_credential.delete_credential()
             self.assertEqual(len(Credential.credential_list), 1)
         def test_find_credential_by_account_username(self):
             self.new_credential.save_credential()
             test_credential = Credential("facebook", "sharon", "3245")
             test_credential.save_credential()
             found_credential = credential.find_by_account_username("sharon")
             self.assertEqual(found_credential.account_password, test_credential.account_password)
         def test_credential_exists(self):
             self.new_credential.save_credential()
             test_credential = Credential("facebook", "sharon", "3245")
             test_credential.save_credential()
             credential_exists = Credential.credential_exists("sharon")
             self.assertTrue(test_credential_exists)
         def test_display_all_credentials(self):
             self.assertEqual(Credential.display_credentials(),Credential.credential_list)

if _name_ == '_main_':
    unittest.main()
    