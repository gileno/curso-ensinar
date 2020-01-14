import unittest

def fatorial(n):
    """Return fatorial of n
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    elif n <= 1:
        return 1
    return n * fatorial(n - 1)


class FatorialTestCase(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.values = [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]
    @classmethod
    def setUpClass(cls):
        print('setUpClass')
    def tearDown(self):
        print('tearDown')
        self.values = []
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
    def test_values(self):
        for case, value in self.values:
            self.assertEqual(fatorial(case), value)
    def test_value_error(self):
        with self.assertRaises(ValueError) as cm:
            fatorial(-1)


if __name__ == '__main__':
    unittest.main()
