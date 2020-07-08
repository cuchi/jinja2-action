#!/usr/bin/env python3

import os
from jinja2 import Template, StrictUndefined
from j2cli.context import read_context_data

def guess_format(file_name):
    _, extension = os.path.splitext(file_name)
    print(extension)
    formats = {
        '.yaml': 'yaml',
        '.yml': 'yaml',
        '.json': 'json',
        '.ini': 'ini',
        '.env': 'env',
    }
    return formats.get(extension, 'env')

variables = {'env': os.environ}
for variable in os.environ.get('INPUT_VARIABLES', '').split('\n'):
    clean_variable = bytes(variable.strip(), 'utf-8').decode('unicode_escape')
    if clean_variable != '':
        name, value = clean_variable.split('=', 1)
        variables.update({name: value})

data_file = os.environ.get('INPUT_DATA_FILE')
if data_file:
    format = os.environ.get('INPUT_DATA_FORMAT', guess_format(data_file))
    with open(data_file, 'r') as file:
        variables.update(read_context_data(format, file, None))

with open(os.environ['INPUT_TEMPLATE'], 'r') as file:
    template_kwargs = {}
    if os.environ.get('INPUT_STRICT') == 'true':
        template_kwargs.update({'undefined': StrictUndefined})
    template = Template(str(file.read()), **template_kwargs)

with open(os.environ['INPUT_OUTPUT_FILE'], 'w') as file:
    file.write(template.render(**variables) + '\n')
