# {{cookiecutter.project_name}}

{{cookiecutter.short_description}}

## Setup

```shell
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .
pre-commit install
```

## Test

```shell
pytest
pre-commit run --all-files
docker build --target=test -t {{cookiecutter.project_name}}_test .
docker run --name {{cookiecutter.project_name}}_test -t {{cookiecutter.project_name}}_test pytest
```
