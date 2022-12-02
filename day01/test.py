import main
import unittest

class Testcases(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(main.do_part1('sample.txt'), 24000) 

    def test_part2(self):
        self.assertEqual(main.do_part2('sample.txt'), 45000)

if __name__ == '__main__':
    unittest.main()