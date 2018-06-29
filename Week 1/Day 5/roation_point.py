import unittest


def find_rotation_point(words):

    # Find the rotation point in the list
    

  min = 0
  max = len(words) - 1
  firstWord = words[0]

  while min < max:
    pivot = ( min + max ) // 2
    if words[pivot] < firstWord: 
      max = pivot 
    
    else:
      min = pivot + 1
    
    if min + 1 == max:
      return max
    
  
  return min


















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)