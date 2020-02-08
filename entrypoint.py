#!/usr/bin/env python3

import os
import re
import subprocess

params = [os.environ['INPUT_TEMPLATE']]

for variable in os.environ.get('INPUT_VARIABLES', '').split('\n'):
    clean_variable = variable.strip()
    if clean_variable != '':
        params.extend(['-D', clean_variable])

if os.environ.get('INPUT_STRICT') == 'true':
    params.append('--strict')

params.extend(['-o', os.environ['INPUT_OUTPUT_FILE']])

subprocess.run(['jinja2'] + params)
