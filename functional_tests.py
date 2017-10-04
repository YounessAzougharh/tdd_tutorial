import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_to_do_list(self):
           
#Edith has heard about a new 'to_do' list apps so she goes at home page
        from time import sleep
        self.browser.get("http://localhost:8000")
        sleep(2)
#she noticed the page title mention to_do lists       
        self.assertIn('to-do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('to-do', header.text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        assertEqual(inputbox.getattribute('placeholder'),'Enter a to-do item')

        inputbox.send_keys("buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')

        self.assertIn(
            "1: buy pecock feathers",
            [rows.text for row in rows]
        )

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')

        self.assertIn(
            "2: use peacock feathers to make a fly",
            [rows.text for row in rows]
        )
        self.assertIn(
            "1: buy pecock feathers",
            [rows.text for row in rows]
        )

        self.fail('Finish the test')

if __name__=='__main__':
    unittest.main(warnings='ignore')




    



#assert 'Django' in browser.title