import unittest
from unittest.mock import mock_open, patch
from file_reader import FileReader

class TestFileReader(unittest.TestCase):
    
    def test_read_file(self):
        file_content = "This is the content of the file"
        file_path = "test_file.txt"
        file_handler = FileReader(file_path)
        _open = mock_open(read_data=file_content)
        
        
        with patch("builtins.open", _open):
            result = file_handler.read_file()
            
        _open.assert_called_once_with(file_path, 'r')
        
        self.assertEqual(result, file_content)
        
        