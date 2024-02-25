import unittest
import sys
from main import floyd_recursive

NO_PATH = sys.maxsize


class TestFloydRecursive(unittest.TestCase):

    def setUp(self):
        self.graph = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]

    def test_floyd_recursive_base_case(self):
        distance = floyd_recursive(self.graph, intermediate=0, start_node=0, end_node= 0)
        self.assertEqual(distance, 0)

    def test_floyd_recursive_shortest_path(self):
        distance = floyd_recursive(self.graph, intermediate=0, start_node=0, end_node=2)
        self.assertEqual(distance, 12)


if __name__ == "__main__":
    unittest.main()
