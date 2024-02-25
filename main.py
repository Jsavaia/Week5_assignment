import sys

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(graph[0])

# base case
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


# Example


result = floyd_recursive(graph, intermediate=0, start_node=0, end_node=2)
print(result)
