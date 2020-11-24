import unittest
from info import Info

class TestInfo(unittest.TestCase):
    def setUp(self):
        self.new_info =Info(1234,3454,4566,6785,'Tony','@Tony','Tee47')

    def test_init(self):
        self.assertEqual(self.new_info.facebookp,1234)
        self.assertEqual(self.new_info.instagramp,4566)  
        self.assertEqual(self.new_info.twitterp,6785) 
        self.assertEqual(self.new_info.email,3454)
        self.assertEqual(self.new_info.facebookusername,'Tony')
        self.assertEqual(self.new_info.twitusername,'@Tony')
        self.assertEqual(self.new_info.instagramusername,'Tee47')

    def test_save_info(self):
        '''
        to test if the user info is saved
        '''
        self.new_info.save_info() 
        self.assertEqual(len(Info.info_list),1)  

    def test_display_info(self):
        self.assertEqual(Info.display_info(),Info.info_list)


if __name__ =='__main__':
    unittest.main()