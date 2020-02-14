[![release](https://img.shields.io/github/v/release/cuchi/jinja2-action?style=flat-square)](https://github.com/cuchi/jinja2-action/releases/latest)
[![marketplace](https://img.shields.io/badge/marketplace-jinja2--action-blue?logo=github&style=flat-square)](https://github.com/marketplace/actions/jinja2-action)

Jinja2 is a fast and straightforward templating engine.

You can use this action to easily run the [Jinja2 CLI](https://github.com/mattrobenolt/jinja2-cli) inside your repository.


# Example
```yml
- name: Setup nginx
  uses: cuchi/jinja2-action@v1.0.1
  with:
    template: infra/nginx.conf.j2
    output_file: infra/nginx.conf
    strict: true
    variables: |
      server_host=staging.example.com
      timeout=30s
```

# See also
- [Jinja2 docs](https://jinja.palletsprojects.com/)
