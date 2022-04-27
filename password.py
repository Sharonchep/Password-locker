class User:
      user_list = []
      def _init_(self,user_name,user_password):
          self.user_name = user_name
          self.user_password = user_password
      def save_user(self):
          User.user_list.append(self)
      def delete_user(self):
          User.user_list.remove(self)
          
class Credential:  
      credential_list = []
      def _init_(self,account,account_username,account_password):
          self.account = account
          self.account_username = account_username
          self.account_password = account_password
      def save_credential(self):
          Credential.credential_list.append(self)
      def delete_credential(self):
          Credential.credential_list.remove(self) 
          
          @classmethod
      def find_by_account_username(cls,account_username):
          for credential in cls.credential_list:
              if credential.account_username == account_username:
                  return credential 
                  
          @classmethod 
      def credential_exists(cls,account_username):
          for credential in cls.credential_list:
              if credential.account_username == account_username:
                  return true
          return false
          
          @classmethod
      def display_credential(cls):
          return cls.credential_list
          
          @classmethod
      def display_all_credential(cls):
          return cls.credential_list