[![release](https://img.shields.io/github/v/release/cuchi/jinja2-action?style=flat-square)](https://github.com/cuchi/jinja2-action/releases/latest)
[![marketplace](https://img.shields.io/badge/marketplace-jinja2--action-blue?logo=github&style=flat-square)](https://github.com/marketplace/actions/jinja2-action)

Jinja2 is a fast and straightforward templating engine.

You can use this action to easily run the [Jinja2 CLI](https://github.com/mattrobenolt/jinja2-cli) inside your repository.


# Example
```yml
jobs:
  foo:
    strategy:
      matrix:
        files: foo/*.yml
- name: Setup nginx
  uses: wbwork/jinja2-action@v0.1.0
  with:
    template: ${{matrix.files}}
    strict: true
    variables: |
      server_host=staging.example.com
      timeout=30s
```

# See also
- [Jinja2 docs](https://jinja.palletsprojects.com/)
