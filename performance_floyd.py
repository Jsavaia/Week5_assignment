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
