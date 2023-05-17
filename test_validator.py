from unittest.mock import patch
import unittest
import sys

@patch('builtins.exit')
class TestValidator(unittest.TestCase):
    @patch('builtins.print')
    def check_password(self, password, expected_output, mock_print):
        patcher = patch('builtins.input', return_value=[password])
        patcher.start()
        import validator
        try:
            mock_print.assert_any_call(expected_output)
        finally:
            sys.modules.pop('validator')
            patcher.stop()

    def test_password_happy_flow(self, mock_exit):
        self.check_password("pasuwo12!#$3", "Validation Succeeded!")
        self.check_password("baume763!!!", "Validation Succeeded!")
        
    def test_password_length(self, mock_exit):
        self.check_password("pass", "Validation Failed: Password length should be between 9 and 12")
        self.check_password("check", "Validation Failed: Password length should be between 9 and 12")
        self.check_password("Yus?1'", "Validation Failed: Password length should be between 9 and 12")
    
    def test_password_special_chars(self, mock_exit):
        self.check_password("passwo1235",  "Validation Failed: You need to have a minimum of 3 special characters")
        self.check_password("Yus?1ad''31",  "Validation Failed: You need to have a minimum of 3 special characters")

    def test_password_alpha_chars(self, mock_exit):
        self.check_password("pass123!#$#", "Validation Failed: You need to have a minimum of 5 alpha characters")
    
    def test_password_numbers(self, mock_exit):
        self.check_password("pasuwop12!#$", "Validation Failed: You need to have a minimum of 3 digits")
        self.check_password("Yus?1''$&qa", "Validation Failed: You need to have a minimum of 3 digits")
    

if __name__ == '__main__':
    unittest.main()
