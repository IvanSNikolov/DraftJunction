# test_draftjunction.py
"""
Tests for DraftJunction module.
"""

import unittest
from draftjunction import DraftJunction

class TestDraftJunction(unittest.TestCase):
    """Test cases for DraftJunction class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftJunction()
        self.assertIsInstance(instance, DraftJunction)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftJunction()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
