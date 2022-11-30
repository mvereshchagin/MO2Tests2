import unittest
from unittest.mock import Mock, MagicMock, patch, call
from main import ask_name_print_greeting, do_something, ask_name_print_greeting2
from calcer import Calcer



class TestAskName(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['Вася', 'Пупкин'])
    def test_ask_name_print_greeting(self, mocked_input, mocked_print):
        # arrange
        print_lines = ['What is your name?', 'What is your surname?', 'Hello, Вася Пупкин']
        expected_calls = [call(val) for val in print_lines]

        # act
        ask_name_print_greeting()

        # assert
        self.assertListEqual(mocked_print.mock_calls, expected_calls)

    @patch('builtins.print')
    @patch('main.get_input', side_effect=['Вася', 'Пупкин'])
    def test_ask_name_print_greeting(self, mocked_input, mocked_print):
        # arrange
        print_lines = ['What is your name?', 'What is your surname?', 'Hello, Вася Пупкин']
        expected_calls = [call(val) for val in print_lines]

        # act
        ask_name_print_greeting2()

        # assert
        self.assertListEqual(mocked_print.mock_calls, expected_calls)

    def test_first(self):
        calcer = Calcer()
        calcer.do_calc = Mock(return_value=3)
        value = calcer.do_calc()
        self.assertEqual(value, 3)

    def test_second(self):
        calcer = Calcer()

        expected_value = [1, 2, 3, 4]
        calcer.do_calc = Mock(side_effect=expected_value)
        res1 = calcer.do_calc()
        res2 = calcer.do_calc()
        res3 = calcer.do_calc()
        res4 = calcer.do_calc()

        self.assertListEqual([res1, res2, res3, res4], expected_value)


    def test_third(self):
        def factorial_side_effects(arg):
            values = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
            return values[arg]

        calcer = Calcer()
        calcer.factorial = factorial_side_effects
        res = calcer.factorial_diff(5)

        self.assertEqual(res, 120 - 24)

    def test_forth(self):

        do_something = Mock()
        do_something.return_value = 34

        res = do_something()

        self.assertEqual(res, 34)

    def test_patch(self):
        # with patch('AskNameTests.do_something') as mocked_do_something:
        #     mocked_do_something.return_value = 34
        #     res = do_something()

        with patch('AskNameTests.do_something', return_value=34):
            res = do_something()

        res2 = do_something()

        self.assertEqual(res, 34)
        self.assertEqual(res2, 5)

