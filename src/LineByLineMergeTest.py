#!/usr/bin/env python
# Tests for LineByLineMergeTest.py
import unittest
from LineByLineMerge import TxtFileProcessor

class LineByLineMergeTest(unittest.TestCase):
    def setUp(self):
        print "setUp"
        self.processor = TxtFileProcessor()
        
    def test_load_from_folder(self):
        self.assertEquals(self.processor.load_from_folder('.txt', './test_data'), 3)
        self.processor.unload()

    def test_load_from_args(self):
        self.assertTrue(True)

    def test_top_bottom_merge(self):
        self.assertTrue(True)
    
    def test_line_by_line_merge(self):
        self.assertTrue(True)
    
if __name__ == '__main__':
    unittest.main(buffer = True)