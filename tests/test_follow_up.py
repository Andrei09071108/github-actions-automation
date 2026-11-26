import unittest

from src.follow_up import needs_follow_up


class FollowUpTests(unittest.TestCase):
    def test_new_request(self):
        self.assertFalse(needs_follow_up(0))

    def test_below_limit(self):
        self.assertFalse(needs_follow_up(23))

    def test_exact_limit(self):
        self.assertTrue(needs_follow_up(24))

    def test_overdue(self):
        self.assertTrue(needs_follow_up(25))
