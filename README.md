
# Example

## Simple usage
```yml
- name: Setup nginx
  uses: cuchi/jinja2-action@v1
  with:
    template: infra/nginx.conf.j2
    output_file: infra/nginx.conf
    variables: |
      server_host=staging.example.com
      timeout=30s
```
