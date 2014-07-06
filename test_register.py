import unittest
import register

class Test(unittest.TestCase):
    def test_initialise_size(self):
        r = register.Register(3)
        self.assertEqual(len(r.basis), 8)

if __name__ == '__main__':
    unittest.main()