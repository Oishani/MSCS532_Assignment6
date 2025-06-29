import unittest
import logging
from deterministic_select import deterministic_select

# Configure logging so messages show up in test output
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

class TestDeterministicSelect(unittest.TestCase):
    def test_sorted_input(self):
        arr = [1, 2, 3, 4, 5]
        for k in range(1, len(arr) + 1):
            expected = k
            result = deterministic_select(arr, k)
            logger.info(f"[deterministic_select] input={arr}, k={k} → result={result}, expected={expected}")
            self.assertEqual(result, expected)

    def test_random_input(self):
        arr = [7, 2, 5, 3, 9, 1, 4, 6, 8]
        expected_sorted = sorted(arr)
        for k in range(1, len(arr) + 1):
            expected = expected_sorted[k - 1]
            result = deterministic_select(arr, k)
            logger.info(f"[deterministic_select] input={arr}, k={k} → result={result}, expected={expected}")
            self.assertEqual(result, expected)

    def test_with_duplicates(self):
        arr = [5, 1, 5, 3, 5]
        cases = [
            (1, 1),
            (2, 3),
            (3, 5),
            (5, 5),
        ]
        for k, expected in cases:
            result = deterministic_select(arr, k)
            logger.info(f"[deterministic_select] input={arr}, k={k} → result={result}, expected={expected}")
            self.assertEqual(result, expected)

    def test_invalid_k_raises(self):
        cases = [
            ([], 1),
            ([1, 2, 3], 0),
            ([1, 2, 3], 4),
        ]
        for arr, k in cases:
            with self.subTest(arr=arr, k=k):
                logger.info(f"[deterministic_select] input={arr}, k={k} → expecting ValueError")
                with self.assertRaises(ValueError):
                    deterministic_select(arr, k)

if __name__ == "__main__":
    unittest.main()
