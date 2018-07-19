import unittest


def find_repeat(the_list):
    n = len(the_list)
    i = n
    j = n
    while True:
        print("looking for cycle: i %s j %s" % (i, j))
        i = the_list[i - 1]  
        j = the_list[j - 1]  
        j = the_list[j - 1]  
        if i == j:
            print("cycle found at %s" % i)
            break

    j = n
    while True:
        print("looking for dup: i %s j %s" % (i, j))
        i = the_list[i - 1]
        j = the_list[j - 1]
        if i == j:
            print("dup found at %s" % i)
            break

    print("dup is %s" % i)
    return i


















# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)