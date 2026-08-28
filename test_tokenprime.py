# test_tokenprime.py
"""
Tests for TokenPrime module.
"""

import unittest
from tokenprime import TokenPrime

class TestTokenPrime(unittest.TestCase):
    """Test cases for TokenPrime class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenPrime()
        self.assertIsInstance(instance, TokenPrime)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenPrime()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
