from django.test import TestCase

from frisor_urls.views import AddUrlView
from frisor_urls.models import Url


class AddUrlViewTest(TestCase):

    def setUp(self):
        self.url_add_url = '/add_url'

    def test_valid_url_form_is_saved_in_database(self):
        title = "short title"
        nick = "short nick"
        url = "http://valid.se"
        tags = 'tag1, tag2'

        data = {
            'url': url,
            'title': title,
            'nick': nick,
            'tags': tags
        }

        resp = self.client.post(self.url_add_url, data=data, follow=True)

        db_url = Url.objects.get()
        self.assertIn("Your new url: " + url, resp.content.decode('utf-8'))
        self.assertEquals(url, db_url.url)

    def test_invalid_url_form_shows_errors(self):
        title = "short title"
        nick = "short nick"
        url = "invalid"
        tags = 'tag1, tag2'

        data = {
            'url': url,
            'title': title,
            'nick': nick,
            'tags': tags
        }

        resp = self.client.post(self.url_add_url, data=data)
        db_url = Url.objects.all()
        self.assertIn("Enter a valid URL.", resp.content.decode('utf-8'))
        self.assertFalse(db_url)
