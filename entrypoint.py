#!/usr/bin/env python3

import os
from jinja2 import Template, StrictUndefined

# Montar o objeto do template com as variáveis que eu defini em todos os modos
with open(os.environ['INPUT_TEMPLATE'], 'r') as file:
    template_kwargs = {}
    if os.environ.get('INPUT_STRICT') == 'true':
        template_kwargs.update({'undefined': StrictUndefined})
    template = Template(str(file.read()), **template_kwargs)

# Aplicar variáveis dentro do template
with open(os.environ['INPUT_OUTPUT_FILE'], 'w') as file:
    file.write(template.render(**variables) + '\n')

if __name__ == '__main__':
    main(os.environ)
