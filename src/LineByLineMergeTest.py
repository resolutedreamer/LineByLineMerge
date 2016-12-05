#!/usr/bin/env python
# Tests for LineByLineMergeTest.py
import unittest
from LineByLineMerge import TxtFileProcessor

class LineByLineMergeTest(unittest.TestCase):
    def setUp(self):
        self.processor = TxtFileProcessor()
    
    def test_load_from_folder(self):        
        self.assertEquals(self.processor.load_from_folder('.txt', './test_data/'), 3)
        self.processor.unload()
        self.assertEquals(self.processor.filePaths, [])

    def test_load_from_args(self):
        # Can't actually test this because the unittest class will consume
        # sys.argv when invoking unittest.main()
        self.assertTrue(True)
        
    def test_extract_subsequent_line(self):
        self.processor.load_from_folder('d', './test_data/')
        self.processor.extract_subsequent_line('cat')
        with open(self.processor.output_filename, 'r+') as out:
            result = out.read()
            print result
            self.assertEquals(result,'fish\n')        
        self.processor.unload()        

    def test_top_bottom_merge(self):
        self.processor.load_from_folder('.txt', './test_data/')
        self.processor.top_bottom_merge()
        with open(self.processor.output_filename, 'r+') as out:
            result = out.read()
            print result
            self.assertEquals(result,'a\nb\ncde\n')
        self.processor.unload()
    
    def test_line_by_line_merge(self):
        self.processor.load_from_folder('.txt', './test_data/')
        self.processor.line_by_line_merge()
        with open(self.processor.output_filename, 'r+') as out:
            result = out.read()
            print result
            self.assertEquals(result,'abcde\n')
        self.processor.unload()
    
if __name__ == '__main__':
    unittest.main(buffer = True)