from unittest import mock
from unittest.mock import Mock, patch
from unittest import TestCase
import unittest
import sys


class Test(TestCase):
    @patch('builtins.exit')
    @patch('builtins.print')
    @patch('builtins.input', return_value=["pasuwo12!#$3", "baume763!!!"])
    def test_password_happy_flow(self, mock_input, mock_print, mock_exit):
        import validator
        try:
            mock_print.assert_any_call("Validation Succeeded!")
        finally:
            sys.modules.pop('validator')

    @patch('builtins.exit')
    @patch('builtins.print')
    @patch('builtins.input', return_value=["pass", "check", "Yus?1'"])
    def test_password_length(self, mock_input, mock_print, mock_exit):
        import validator
        try:
            mock_print.assert_any_call("Validation Failed: Password length should be between 9 and 12")
        finally:
            sys.modules.pop('validator')
        mock_exit.assert_called_with(0)
    
    @patch('builtins.exit')
    @patch('builtins.print')
    @patch('builtins.input', return_value=["passwo1235", "Yus?1ad''31"])
    def test_password_special_chars(self, mock_input, mock_print, mock_exit):
        import validator
        try:
            # sys.stdout.write(str( mock_print.call_args ) + '\n')
            # sys.stdout.write(str( mock_print.call_args_list ) + '\n')
            mock_print.assert_any_call("Validation Failed: You need to have a minimum of 3 special characters")
        finally:
            sys.modules.pop('validator')
        mock_exit.assert_called_with(0)

    @patch('builtins.exit')
    @patch('builtins.print')
    # @patch('builtins.input', return_value=["pass123!#$#", "Yus?1''$&"])
    @patch('builtins.input', return_value=["pass123!#$#"])
    def test_password_alpha_chars(self, mock_input, mock_print, mock_exit):
        import validator
        try:
            # sys.stdout.write(str( mock_print.call_args ) + '\n')
            # sys.stdout.write(str( mock_print.call_args_list ) + '\n')
            mock_print.assert_any_call("Validation Failed: You need to have a minimum of 5 alpha characters")
        finally:
            sys.modules.pop('validator')
        mock_exit.assert_called_with(0)
    
    @patch('builtins.exit')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["pasuwop12!#$", "Yus?1''$&qa"])
    def test_password_numbers(self, mock_input, mock_print, mock_exit):
        import validator
        try:
            # sys.stdout.write(str( mock_print.call_args ) + '\n')
            # sys.stdout.write(str( mock_print.call_args_list ) + '\n')
            mock_print.assert_any_call("Validation Failed: You need to have a minimum of 3 numbers")
        finally:
            sys.modules.pop('validator')
        mock_exit.assert_called_with(0)
    

if __name__ == '__main__':
    unittest.main()