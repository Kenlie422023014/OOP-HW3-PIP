import unittest
from src.sort.insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        arr = [5, 3, 8, 4, 2, 7, 1, 6]
        sorted_arr = insertion_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()
