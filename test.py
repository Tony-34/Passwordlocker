import unittest
from user import User
from info import Info

class TestUser(unittest.TestCase):
    def setup(self):
        self.new_user = User('Tony','Abongo','tr33947@gmail.com')

    def test1(self):
            self.assertEqual = user(self.new_user.fname,'Tony')
            self.assertEqual = user(self.new_user.lname,'Abongo')
            self.assertEqual = (self.new_user.email,'tr33947@gmail.com')
            
    def test_save_user(self):
            self.new_user.save_user(),
            test_data = User('Tony','Abongo','tr33947@gmail.com')
            test_data.save_user()
            self.assertEqual(len(User.save_userlist),2)

    def test_display_user(self):
        self.assertEqual(User.display_users(),User.save_userlist)
if __name__ == '__main__':
     unittest.main()       

       
