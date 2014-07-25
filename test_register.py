import unittest
import register

class TestRegister(unittest.TestCase):
    def test_initialise_size(self):
        r = register.Register(3)
        self.assertEqual(len(r.state), 8)

if __name__ == '__main__':
    unittest.main()