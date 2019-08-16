import unittest
from rectangle.rectangleintersection import intersect
from rectangle.rectangleintersection import rectangle_intersections


class TestIntersectionDetectionFunctions(unittest.TestCase):

    def test_intersect_two_collisions(self):
        results = intersect(2, 6, 3, 3, 5, 2, 5)
        expected_results = [(3, 3), (5, 3)]
        self.assertCountEqual(
           results, expected_results, "\nintersect Results: {}\nExpected Results: {}".format(results, expected_results)
        )
        print("{} success:\nResults: {} Expected Results: {}\n".format(self._testMethodName, results, expected_results))

    def test_intersect_one_collision(self):
        results = intersect(-2, 5, -3, -1, 7, -4, -1)
        expected_results = [(-1, -3)]
        self.assertCountEqual(
            results, expected_results, "\nintersect Results: {}\nExpected Results: {}".format(results, expected_results)
        )
        print("{} success:\nResults: {} Expected Results: {}\n".format(self._testMethodName, results, expected_results))

    def test_intersect_no_collisions(self):
        results = intersect(1, 4, 4, 1, 3, -1, 1)
        expected_results = []
        self.assertCountEqual(
            results, expected_results, "\nintersect Results: {}\nExpected Results: {}".format(results, expected_results)
        )
        print("{} success:\nResults: {} Expected Results: {}\n".format(self._testMethodName, results, expected_results))

    def test_rectangle_intersections_bottom_right(self):
        results = rectangle_intersections(4, 10, 3, 6, 8, 12, 4, 8)
        expected_results = [(10, 4), (8, 6)]
        self.assertCountEqual(
            results, expected_results,
            "\nrectangle_intersections Results: {}\nExpected Results: {}".format(results, expected_results)
        )
        print("{} success:\nResults: {} Expected Results: {}\n".format(self._testMethodName, results, expected_results))

    def test_rectangle_intersections_left(self):
        results = rectangle_intersections(4, 10, 3, 6, 8, 12, 4, 5)
        expected_results = [(10, 4), (10, 5)]
        self.assertCountEqual(
            results, expected_results,
            "\nrectangle_intersections Results: {}\nExpected Results: {}".format(results, expected_results)
        )
        print("{} success:\nResults: {} Expected Results: {}\n".format(self._testMethodName, results, expected_results))

    def test_rectangle_intersections_top(self):
        results = rectangle_intersections(6, 9, 6, 10, 6.5, 8.5, 7, 3)
        expected_results = [(6.5, 6), (8.5, 6)]
        self.assertCountEqual(
            results, expected_results,
            "\nrectangle_intersections Results: {}\nExpected Results: {}".format(results, expected_results)
        )
        print("{} success:\nResults: {} Expected Results: {}\n".format(self._testMethodName, results, expected_results))

    def test_rectangle_intersections_top_3_intersections(self):
        results = rectangle_intersections(6, 9, 6, 10, 6.5, 9, 7, 3)
        expected_results = [(6.5, 6), (9, 6), (9, 7)]
        self.assertCountEqual(
            results, expected_results,
            "\nrectangle_intersections Results: {}\nExpected Results: {}".format(results, expected_results)
        )
        print("{} success:\nResults: {} Expected Results: {}\n".format(self._testMethodName, results, expected_results))

    def test_rectangle_intersections_left_4_intersections(self):
        results = rectangle_intersections(6, 9, 6, 10, 7, 4, 6, 10)
        expected_results = [(6, 6), (6, 10), (7, 6), (7, 10)]
        self.assertCountEqual(
            results, expected_results,
            "\nrectangle_intersections Results: {}\nExpected Results: {}".format(results, expected_results)
        )
        print("{} success:\nResults: {} Expected Results: {}\n".format(self._testMethodName, results, expected_results))

    def test_rectangle_intersections_no_intersections(self):
        results = rectangle_intersections(3, 7, 4, 8, 9, 12, 6, 10)
        expected_results = 0
        self.assertEqual(
            results, expected_results,
            "\nrectangle_intersections Results: {}\nExpected Results: {}".format(results, expected_results)
        )
        print("{} success:\nResults: {} Expected Results: {}\n".format(self._testMethodName, results, expected_results))

    def test_rectangle_intersections_no_intersections(self):
        results = rectangle_intersections(3, 7, 4, 8, 9, 12, 6, 10)
        expected_results = 0
        self.assertEqual(
            results, expected_results,
            "\nrectangle_intersections Results: {}\nExpected Results: {}".format(results, expected_results)
        )
        print("{} success:\nResults: {} Expected Results: {}\n".format(self._testMethodName, results, expected_results))

    def test_rectangle_same_rectangle(self):
        results = rectangle_intersections(9, 12, 6, 10, 9, 12, 6, 10)
        expected_results = [(9, 6), (12, 6), (9, 10), (12, 10)]
        self.assertCountEqual(
            results, expected_results,
            "\nrectangle_intersections Results: {}\nExpected Results: {}".format(results, expected_results)
        )
        print("{} success:\nResults: {} Expected Results: {}\n".format(self._testMethodName, results, expected_results))


if __name__ == '__main__':
    unittest.main()
