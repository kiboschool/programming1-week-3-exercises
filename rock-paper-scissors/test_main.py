from unittest.mock import patch
from unittest import TestCase
import unittest
import sys
import io

from gradescope_utils.autograder_utils.decorators import weight

class Test(TestCase):
    @patch('builtins.input', return_value="Paper")
    @weight(1)
    def test_rock_paper(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout, patch('random.randint') as mock_rand:
            mock_rand.return_value = 1
            import main
            try:
                lines = mock_stdout.getvalue().split("\n")
            finally:
                sys.modules.pop('main')
        computer_choice = lines[1].lower()
        result = lines[2].lower()
        print(f"Read in computer choice: \"{computer_choice}\"")       
        print(f"Read in result: \"{result}\"")

        expected_results = [
            # (var, contains_each_of_these)
            (computer_choice, ('computer', 'chooses', 'rock')),
            (result, ('rock', 'paper', 'win'))
        ]

        not_expected = [
            # (var, contains_each_of_these)
            (computer_choice, ('scissors', 'paper')),
            (result, ('scissors', 'lose'))
        ]

        for var, expected_words in expected_results:
            for word in expected_words:
                self.assertTrue(word in var, msg=f"\"{word}\" not in \"{var}\"")

        for var, unexpected_words in not_expected:
            for word in unexpected_words:
                self.assertFalse(word in var, msg=f"\"{word}\" unexpectedly in \"{var}\"")

    @patch('builtins.input', return_value="Scissors")
    @weight(1)
    def test_paper_scissors(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout, patch('random.randint') as mock_rand:
            mock_rand.return_value = 2
            import main
            try:
                lines = mock_stdout.getvalue().split("\n")
            finally:
                sys.modules.pop('main')
        computer_choice = lines[1].lower()
        result = lines[2].lower()
        print(f"Read in computer choice: \"{computer_choice}\"")       
        print(f"Read in result: \"{result}\"")

        expected_results = [
            # (var, contains_each_of_these)
            (computer_choice, ('computer', 'chooses', 'paper')),
            (result, ('scissors', 'paper', 'win'))
        ]

        not_expected = [
            # (var, contains_each_of_these)
            (computer_choice, ('rock', 'scissors')),
            (result, ('rock', 'lose'))
        ]

        for var, expected_words in expected_results:
            for word in expected_words:
                self.assertTrue(word in var, msg=f"\"{word}\" not in \"{var}\"")

        for var, unexpected_words in not_expected:
            for word in unexpected_words:
                self.assertFalse(word in var, msg=f"\"{word}\" unexpectedly in \"{var}\"")

    @patch('builtins.input', return_value="Scissors")
    @weight(1)
    def test_rock_scissors(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout, patch('random.randint') as mock_rand:
            mock_rand.return_value = 1
            import main
            try:
                lines = mock_stdout.getvalue().split("\n")
            finally:
                sys.modules.pop('main')
        computer_choice = lines[1].lower()
        result = lines[2].lower()
        print(f"Read in computer choice: \"{computer_choice}\"")       
        print(f"Read in result: \"{result}\"")

        expected_results = [
            # (var, contains_each_of_these)
            (computer_choice, ('computer', 'chooses', 'rock')),
            (result, ('rock', 'scissors', 'lose'))
        ]

        not_expected = [
            # (var, contains_each_of_these)
            (computer_choice, ('scissors', 'paper')),
            (result, ('paper', 'win'))
        ]

        for var, expected_words in expected_results:
            for word in expected_words:
                self.assertTrue(word in var, msg=f"\"{word}\" not in \"{var}\"")

        for var, unexpected_words in not_expected:
            for word in unexpected_words:
                self.assertFalse(word in var, msg=f"\"{word}\" unexpectedly in \"{var}\"")

if __name__ == '__main__':
    unittest.main()
