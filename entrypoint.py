#!/usr/bin/env python3

import os
import re
import subprocess

flags = []

variables = re.compile('\n+', re.MULTILINE).sub(
    ',',
    os.environ['INPUT_VARIABLES']
)

if os.environ.get('INPUT_STRICT') == 'true':
    flags.append('--strict')

flags.extend([
    os.environ['INPUT_TEMPLATE'],
    '-D', variables,
    '-o', os.environ['INPUT_OUTPUT_FILE']
])

subprocess.run(['jinja2'] + flags)
