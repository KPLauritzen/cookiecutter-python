# Kasper's Cookiecutter for new Python projects

## Using this cookiecutter

```shell
cookiecutter <URL>
```

## Setting up your project

```shell
cd <project_name>
python -m venv venv # or python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .
git init
pre-commit install
git add .
git commit -m "Initial commit"
```

## Test your project

```shell
pre-commit run --all-files
pytest
docker build --target=test -t <project>-test . && docker run <project>-test
```
