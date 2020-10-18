import os
import unittest

from enums import GitHubActionsInput
from main import Context


class TestContext(unittest.TestCase):
    TEST_FILE = 'test_output'

    def test_load_from_env(self):
        env_vars = {
            'foo': 'bar',
            GitHubActionsInput.VARIABLES.value: 'name=John\nsurname=Doe'
        }

        context = Context(env_vars)
        context.load_from_env()
        expected = {'env': env_vars}
        
        self.assertEqual(context._variables, expected)

    def test_load_from_input(self):
        context = Context({GitHubActionsInput.VARIABLES.value: 'name=John\nsurname=Doe'})
        context.load_from_input()

        expected = {
            'name': 'John',
            'surname': 'Doe',
        }
        self.assertEqual(context._variables, expected)
        

    def test_load_from_data_file(self):
        context = Context({
            GitHubActionsInput.DATA_FILE.value: 'test/data-files/data.yml'
        })

        context.load_from_data_file()

        expected = {
            'foo': 'bar',
            'baz': 'cux',
        }
        self.assertEqual(context._variables, expected)

    def test_render_template(self):
        context = Context({
            GitHubActionsInput.DATA_FILE.value: 'test/data-files/data.json',
            GitHubActionsInput.OUTPUT_FILE.value: self.TEST_FILE,
            GitHubActionsInput.TEMPLATE.value: 'test/many-variables/template',
        })
        
        context.load_from_data_file()
        context.render_template()

        expected = "\nbar\ncux\n"

        with open('test_output', 'r') as file:
            result = file.read()
            self.assertEqual(result, expected)
    
    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.TEST_FILE):
            os.remove(cls.TEST_FILE)

if __name__ == '__main__':
    unittest.main()