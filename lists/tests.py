import re
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

#from lists.models import Item, List
from lists.views import homepage


class HomePageTest(TestCase):

    def assertEqualExceptCSRF(self, html_code1, html_code2):
        return self.assertEqual(
            self.remove_csrf(html_code1),
            self.remove_csrf(html_code2)
        )

    def test_homepage_is_about_todo_lists(self):
        request = HttpRequest()
        response = homepage(request)
        expected_content = render_to_string('home.html')

        self.assertEqualExceptCSRF(response.content.decode(), expected_content)
    # remove csrf from html code
    @staticmethod
    def remove_csrf(html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', html_code)

    def test_homepage_can_remembre_post_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new item'
        response = homepage(request)
        
        self.assertIn('A new item',response.content.decode())

        expected_content = render_to_string('home.html', {'new_item_text' : 'A new item'})
        self.assertEqualExceptCSRF(response.content.decode(), expected_content)
