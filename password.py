class User:
      user_list = []
      def _init_(self,user_name,user_password):
          self.user_name = user_name
          self.user_password = user_password
      def save_user(self):
          User.user_list.append(self)
      def delete_user(self):
          User.user_list.remove(self)