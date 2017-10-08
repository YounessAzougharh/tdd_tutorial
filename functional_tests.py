import unittest
from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from time import sleep

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3000)
        
    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_to_do_list(self):
           
#Edith has heard about a new 'to_do' list apps so she goes at home page
        
        self.browser.get("http://localhost:8000")
        #sleep(2)
#she noticed the page title mention to_do lists       
        self.assertIn('to-do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('to-do', header.text)

#Edith noticed that the inputbox invited her to enter a new to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

#she enters a new item : buy peacock feathers
        inputbox.send_keys("1: buy peacock feathers")

#she hits ENTER, the page Updates and now the page lists
        inputbox.send_keys(Keys.ENTER)

#"buy a peacock fethers" is an item in a to-do list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(
            "1: buy peacock feathers",
            [row.text for row in rows]
        )
        sleep(2)
#she can add another to-do item:"use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("2: use peacock feathers to make a fly")
        sleep(2)
        
        inputbox.send_keys(Keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

#"use peacock feathers to make a fly" is added to Edith to-do items list
        self.assertIn(
            "2: use peacock feathers to make a fly",
            [row.text for row in rows]
        )
        self.assertIn(
            "1: buy peacock feathers",
            [row.text for row in rows]
        )

        self.fail('Finish the test')

if __name__=='__main__':
    unittest.main(warnings='ignore')




    



#assert 'Django' in browser.title