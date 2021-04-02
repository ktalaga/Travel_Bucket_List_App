import unittest
from models.sight import Sight

class TestSight(unittest.TestCase):
    
    def setUp(self):
        self.sight = Sight("Royal Albert Hall")

    def test_sight_has_name(self):
        self.assertEqual("Royal Albert Hall", self.sight.name)

    def test_sight_visited_starts_false(self):
        self.assertEqual(False, self.sight.visited)

    def test_can_mark_sight_visited(self):
        self.sight.mark_visited()
        self.assertEqual(True, self.sight.visited)