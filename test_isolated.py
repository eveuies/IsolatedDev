# test_isolated.py
"""
Tests for Isolated module.
"""

import unittest
from isolated import Isolated

class TestIsolated(unittest.TestCase):
    """Test cases for Isolated class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Isolated()
        self.assertIsInstance(instance, Isolated)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Isolated()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
