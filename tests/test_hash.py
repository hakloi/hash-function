import unittest
from hash_function.hash import simple_hash

class TestSimpleHash(unittest.TestCase):

    def test_simple_hash(self):
        test_input = b"example@example.com"
        output = simple_hash(test_input)
        
        self.assertEqual(len(output), 32)
        
        self.assertNotEqual(output, b'\x00' * 32)

if __name__ == "__main__":
    unittest.main()
