import unittest


def iq_test(numbers):
    number_list = list(map(int, numbers.split(' ')))
    for key, num in enumerate(number_list):
        modulo = num % 2
        if modulo > 0:
            number_list[key] = 1
        else:
            number_list[key] = 0

    if number_list.count(1) < number_list.count(0):
        return number_list.index(1) + 1
    else:
        return number_list.index(0) + 1


class Test(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(iq_test("2 4 7 8 10"), 3)
        self.assertEqual(iq_test("1 2 2"), 1)
        self.assertEqual(iq_test("3 9 1 7 4"), 5)


if __name__ == '__main__':
    unittest.main()
