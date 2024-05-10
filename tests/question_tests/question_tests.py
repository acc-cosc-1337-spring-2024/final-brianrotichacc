import io
import unittest
from unittest.mock import patch
from src.question_a.question_a import numbers

class Test_Config(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5']) #pass values to the number function without prompting the user.
    @patch('sys.stdout', new_callable=io.StringIO) # value output
    def test_question_a_numbers(self, mock_stdout, mock_input):
        numbers()

        output = mock_stdout.getvalue()

        # Check the expected output
        expected_output = "\nResults:\n"
        expected_output += "The lowest number in the list: 1\n"
        expected_output += "The highest number in the list: 5\n"
        expected_output += "The total of the numbers in the list: 15\n"
        expected_output += "The average of the numbers in the list: 3.0\n"
        
        self.assertIn(expected_output, output)


