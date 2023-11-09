[![release](https://img.shields.io/github/v/release/cuchi/jinja2-action?style=flat-square)](https://github.com/cuchi/jinja2-action/releases/latest)
[![marketplace](https://img.shields.io/badge/marketplace-jinja2--action-blue?logo=github&style=flat-square)](https://github.com/marketplace/actions/jinja2-action)

Jinja2 is a fast and straightforward templating engine. You can use this action
to easily run it in your GitHub workflows.


# Using input variables
```yml
- name: Setup nginx
  uses: cuchi/jinja2-action@v1.2.2
  with:
    template: infra/nginx.conf.j2
    output_file: infra/nginx.conf
    strict: true
    variables: |
      server_host=staging.example.com
      timeout=30s
```

# Using data files
```yml
- name: Setup nginx
  uses: cuchi/jinja2-action@v1.2.2
  with:
    template: infra/nginx.conf.j2
    output_file: infra/nginx.conf
    data_file: staging_config.json
    data_format: json # Will try to guess from the extension instead (unnecessary in this case)
```

# Using environment variables
```yml
- name: Setup nginx
  uses: cuchi/jinja2-action@v1.2.2
  with:
    template: infra/nginx.conf.j2
    output_file: infra/nginx.conf
  env:
    SERVER_HOST: staging.example.com
```

Environment variables are used this way in the template file:
```
{{ env['SERVER_HOST'] }} <-- This is always strict
```
```
{{ env.get('SERVER_HOST') }} <-- This is never strict, and displays `None` if you don't specify a default value
```

# See also
- [Jinja2 docs](https://jinja.palletsprojects.com/)
