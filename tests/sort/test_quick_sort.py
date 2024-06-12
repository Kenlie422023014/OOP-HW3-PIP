import unittest
from src.sort.quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        arr = [5, 3, 8, 4, 2, 7, 1, 6]
        sorted_arr = quick_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()
