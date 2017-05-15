import unittest

from brackets.brackets import split_group, re_split_group


class TestSplitter(unittest.TestCase):
    data = {
        '(asdasda)(asd': '(asdasda)',
        '(asdaasda)(asdasd)': '(asdaasda)(asdasd)',
        '(asdaasda)(()(as': '(asdaasda)(()',
    }

    def test_split_group(self):
        for input_line in self.data:
            self.assertEqual(split_group(input_line), self.data[input_line])

    def test_re_split_group(self):
        for input_line in self.data:
            print(input_line, re_split_group(input_line))
            self.assertEqual(self.data[input_line], re_split_group(input_line))
