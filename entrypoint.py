#!/usr/bin/env python3

import os
import re
import subprocess

params = [os.environ['INPUT_TEMPLATE']]

for variable in os.environ.get('INPUT_VARIABLES', '').split('\n'):
    clean_variable = bytes(variable.strip(), 'utf-8').decode('unicode_escape')
    if clean_variable != '':
        params.extend(['-D', clean_variable])

if os.environ.get('INPUT_STRICT') == 'true':
    params.append('--strict')

params.extend(['-o', os.environ['INPUT_OUTPUT_FILE']])

params.extend([os.environ.get('INPUT_DATA_FILE','')])

subprocess.run(['jinja2'] + params, check = True)
