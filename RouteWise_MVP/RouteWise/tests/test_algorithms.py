import unittest
from algorithms.graph import GRAPH, COORDS
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar

class RouteAlgorithmTests(unittest.TestCase):
    def test_both_algorithms_find_same_optimal_cost(self):
        path_d, cost_d, _ = dijkstra(GRAPH, "uran", "airoli")
        path_a, cost_a, _ = astar(GRAPH, COORDS, "uran", "airoli")
        self.assertTrue(path_d)
        self.assertTrue(path_a)
        self.assertEqual(cost_d, cost_a)

    def test_path_starts_and_ends_correctly(self):
        path, _, _ = dijkstra(GRAPH, "panvel", "vashi")
        self.assertEqual(path[0], "panvel")
        self.assertEqual(path[-1], "vashi")

if __name__ == "__main__":
    unittest.main()
