from django.test import TestCase

from frisor_urls.views import UrlView
from frisor_urls.models import Url

class UrlViewTest(TestCase):

    def test_valid_url_form_is_saved_in_database(self):
        title = "short title"
        nick = "short nick"
        url = "http://valid.se"

        data = {
            'url': url,
            'title': title,
            'nick': nick
        }

        resp = self.client.post(UrlView.success_url, data=data, follow=True)

        self.assertIn("Your new url: " + url, resp.content.decode('utf-8'))
        db_url = Url.objects.get()
        self.assertEquals(url, db_url.url)

    def test_invalid_url_form_shows_errors(self):
        title = "short title"
        nick = "short nick"
        url = "invalid"

        data = {
            'url': url,
            'title': title,
            'nick': nick
        }

        resp = self.client.post(UrlView.success_url, data=data)
        self.assertIn("Enter a valid URL.", resp.content.decode('utf-8'))
        db_url = Url.objects.all()
        self.assertFalse(db_url)
