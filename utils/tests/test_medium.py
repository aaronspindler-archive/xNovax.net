from django.test import TestCase

from utils.medium import get_posts


class MediumTests(TestCase):
    def test_utils_medium_get_posts(self):
        print('Testing utils.medium.get_posts()')
        posts = get_posts("hohanga")
        self.assertEqual(len(posts), 3)
