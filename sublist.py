# coding: utf-8
import unittest


class SubListCase(unittest.TestCase):


    def test_sublist(self):
        full_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        index = 2
        quantity = 5
        expected = [1, 2, 3, 4, 5,]
        self.assertEqual(sublist(full_list, index, quantity), expected)

        index = 7
        quantity = 5
        expected = [6, 7, 8, 9, 10]
        self.assertEqual(sublist(full_list, index, quantity), expected)

        index = 2
        quantity = 4
        expected = [1, 2, 3, 4,]
        self.assertEqual(sublist(full_list, index, quantity), expected)

        index = 7
        quantity = 4
        expected = [6, 7, 8, 9]
        self.assertEqual(sublist(full_list, index, quantity), expected)

        index = 5
        quantity = 2
        expected = [5, 6]
        self.assertEqual(sublist(full_list, index, quantity), expected)

        index = 1
        quantity = 5
        expected = [1, 2, 3, 4, 5,]
        self.assertEqual(sublist(full_list, index, quantity), expected)

        index = 8
        quantity = 8
        expected = [3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sublist(full_list, index, quantity), expected)

        index = 8
        quantity = 1
        expected = [9]
        self.assertEqual(sublist(full_list, index, quantity), expected)

        index = 0
        quantity = 1
        expected = [1]
        self.assertEqual(sublist([1], index, quantity), expected)

        index = 0
        quantity = 1
        expected = []
        self.assertEqual(sublist([], index, quantity), expected)

        full_list = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        index = 2
        quantity = 7
        expected = [6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(sublist(full_list, index, quantity), expected)


def sublist(full_list, index, quantity):

    '''
        Return a sublist of a list according
        to the index and number of elements

        Ex.:
        full_list = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        index = 2 (full_list[2] == 8)
        quantity = 7

        returned:
        [6, 7, 8, 9, 10, 11, 12]
    '''

    len_list = len(full_list)
    if len_list == 0:
        return []

    _sublist = []
    cont = quantity

    _sublist.append(full_list[index])
    cont -= 1

    distance_from_index = 1
    set_lower = True
    set_upper = True

    while cont > 0:

        if index - distance_from_index < 0:
            set_lower = False
        if index + distance_from_index >= len_list:
            set_upper = False

        if set_lower:
            _sublist.insert(0, full_list[index - distance_from_index])
            cont -= 1
            if cont <= 0:
                break

        if set_upper:
            _sublist.append(full_list[index + distance_from_index])
            cont -= 1

        distance_from_index += 1

    return _sublist


if __name__ == '__main__':
    unittest.main()
