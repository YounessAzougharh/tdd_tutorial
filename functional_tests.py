import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_to_do_list(self):

#Edith has heard about a new 'to_do' list apps so she goes at home page
        self.browser.get("http://localhost:8000")

#she noticed the page title mention to_do lists       
        self.assertIn('to_do', self.browser.title)


if __name__=='__main__':
    unittest.main(warnings='ignore')




    



#assert 'Django' in browser.title