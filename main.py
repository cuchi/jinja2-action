import os
from j2cli.context import read_context_data
from jinja2 import Template, StrictUndefined
from enums import GitHubActionsInput

class Context:
    def __init__(self, environ):
        self._variables = {}
        self._environ = environ

    def load_from_env(self):
        self._variables.update({'env': self._environ})

    def load_from_input(self):
        for variable in self._environ.get(GitHubActionsInput.VARIABLES, '').split('\n'):
            clean_variable = bytes(variable.strip(), 'utf-8').decode('unicode_escape')
            if clean_variable != '':
                name, value = clean_variable.split('=', 1)
                self._variables.update({name: value})

    def load_from_data_file(self):
        data_file = self._environ.get(GitHubActionsInput.DATA_FILE)
        if data_file:
            format = self._environ.get(
                GitHubActionsInput.DATA_FORMAT,
                self._guess_format(data_file),
            )
            with open(data_file, 'r') as file:
                self._variables.update(read_context_data(format, file, None))


    def render_template(self):
        with open(self._environ[GitHubActionsInput.TEMPLATE], 'r') as file:
            template_kwargs = {}
            if self._environ.get(GitHubActionsInput.STRICT) == 'true':
                template_kwargs.update({'undefined': StrictUndefined})
            template = Template(str(file.read()), **template_kwargs)

        with open(self._environ[GitHubActionsInput.OUTPUT_FILE], 'w') as file:
            file.write(template.render(**self._variables) + '\n')


    def _guess_format(self, file_name):
        _, extension = os.path.splitext(file_name)
        formats = {
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.json': 'json',
            '.ini': 'ini',
            '.env': 'env',
        }
        return formats.get(extension, 'env')

