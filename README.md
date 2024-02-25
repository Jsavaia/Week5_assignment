Readme.dm
---------
import sys

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(graph[0])

# base case and recursive functions
def floyd_recursive(distance, intermediate, start_node, end_node):
    if intermediate == MAX_LENGTH - 1:
        return distance[start_node][end_node]
    else:
        # Recursively find the minimum distance
        no_inter = floyd_recursive(distance, intermediate + 1, start_node, end_node)
        with_inter = (floyd_recursive(distance, intermediate + 1, start_node, intermediate) +
                      floyd_recursive(distance,
                                      intermediate + 1,
                                      intermediate,
                                      end_node))

    # Update the distance matrix
    distance[start_node][end_node] = min(distance[start_node][end_node], no_inter, with_inter)

    return distance[start_node][end_node]


# Example use


result = floyd_recursive(graph, intermediate=0, start_node=0, end_node=2)
print(result)


# Usage
Python version 3.11 recommended

#Run the performance tests:
import sys
import timeit

NO_PATH = sys.maxsize

graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]


def performance_test():
    setup_code = f"from main import floyd_recursive; graph = {graph}"
    stmt = "floyd_recursive(graph, 0, 0, 2)"

    execution_time = timeit.timeit(stmt, setup=setup_code, number=1000)
    print(f'Execution time: {execution_time:.6f} seconds for 1000 iterations')


if __name__ == "__main__":
    performance_test()

#Run the unit tests:
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

# Files
main.py: Implementation of floyd_recursive function

performance_floyd: Performance test for floyd_recursive

test_floyd: Unit tests for floyd_recursive

requirements.txt: no external dependencies needed

Readme.dm: Project documentation

Directory tree.txt: Tree structure of Week5_assignment

# License

MIT License
