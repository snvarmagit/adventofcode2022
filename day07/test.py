import unittest
import main

class Testcases(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(main.do_part1('sample.txt'), 95437)
    
    def test_part2(self):
        self.assertEqual(main.do_part2('sample.txt'), 24933642)


if __name__ == '__main__':
    unittest.main()