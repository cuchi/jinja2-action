#!/usr/bin/env python3

import os

from main import Context

if __name__ == '__main__':
    context = Context(os.environ)
    context.load_from_env()
    context.load_from_input()
    context.load_from_data_file()
    context.render_template()
