"""
Functions used to generate the files of the scaffold.
"""
import inspect


def generate_coveragerc():
    file_contents = """
    [run]
    omit = 
        .venv/*
        .tox/*

    [report]
    show_missing = True
    """
    return inspect.cleandoc(file_contents)


def generate_dockerignore():
    file_contents = f"""
    .venv
    __pycache__
    *.pyc
    .git
    .cache
    **/__pycache__
    htmlcov
    .coverage
    .tox
    .dist
    .pytest_cache
    """
    return inspect.cleandoc(file_contents)


def generate_dotenv():
    file_contents = """
    # Flask
    FLASK_APP=app.py
    PORT=5005
    DEBUG=True

    # Docker
    PYTHONUNBUFFERED=1
    """
    return inspect.cleandoc(file_contents)


def generate_isort_cfg():
    file_contents = """
    [settings]
    force_single_line=True
    line_length=100
    """

    return inspect.cleandoc(file_contents)


def generate_mdlrc():
    file_contents = """    
    """

    return inspect.cleandoc(file_contents)


def generate_bandit():
    file_contents = """    
    """

    return inspect.cleandoc(file_contents)


def generate_readme(project_name):
    file_contents = """
    # {project_name}
    
    Insert a nice doc here!
    """.format(
        project_name=project_name
    )

    return inspect.cleandoc(file_contents)


def generate_codeclimate():
    file_contents = """
    version: 2
    checks:
      similar-code:
        enabled: false
    
    plugins:
      pep8:
        enabled: true
    
      markdownlint:
        enabled: true
    
      sonar-python:
        enabled: true
        config:
          sonar.sourceEncoding: UTF-8
    
      bandit:
        enabled: true
        config:
          python_version: 3
    
      duplication:
        enabled: true
        config:
          languages:
            python:
              python_version: 3
    
    exclude_patterns:
      - "**/.venv/"
      - "**/.data/"
      - "**/.pytest_cache/"
      - "**/.tox/"
      - "**/.dist/" 
    """
    return inspect.cleandoc(file_contents)


def generate_pre_commit_config():
    file_contents = """
    repos:
      - repo: https://github.com/ambv/black
        rev: 18.9b0
        hooks:
          - id: black
            language_version: python3.7
    """
    return inspect.cleandoc(file_contents)


def generate_dockerfile():
    file_contents = """
    FROM python:3.7.2-stretch
    
    WORKDIR /api
    
    COPY . /api
    
    RUN pip3 install --upgrade pip==18.1 && \
        pip3 install -r requirements_dev.txt
    """
    return inspect.cleandoc(file_contents)


def generate_docker_compose():
    file_contents = """
    version: "3.5"
    services:
      app:
        build: .
        stdin_open: true
        tty: true
        ports:
          - "${PORT}:${PORT}"
        env_file: .env
        volumes:
          - .:/api
        command: ["gunicorn", "app:app"]
    """
    return inspect.cleandoc(file_contents)


def generate_pyproject_toml():
    file_contents = """
    [tool.black]
    line-length = 100
    py36 = true
    include = '\.pyi?$'
    exclude = '''
    /(
        \.git
      | \.hg
      | \.mypy_cache
      | \.tox
      | \.venv
      | _build
      | buck-out
      | build
      | dist
    )/
    '''
    """
    return inspect.cleandoc(file_contents)


def generate_requirements_txt():
    file_contents = """
    Flask==1.0.2
    gunicorn==19.9.0
    flask_log_request_id==0.10.0
    """
    return inspect.cleandoc(file_contents)


def generate_requirements_dev_txt():
    file_contents = """
    -r requirements.txt
    black
    pylint
    pep8
    flake8
    tox
    pytest
    pytest-cov
    coverage
    requests_mock
    """
    return inspect.cleandoc(file_contents)


def generate_setup_cfg():
    file_contents = """
    [flake8]
    max-line-length = 100
    
    [pep8]
    ignore = W503, E701
    max-line-length = 100    
    """
    return inspect.cleandoc(file_contents)


def generate_tox_ini(project_name):
    file_contents = """        
    [tox]
    skipsdist=True
    envlist = py37
    
    [testenv]
    setenv =
        LOGGING_LEVEL = DEBUG
    
    commands =
        pytest -vv --cov={project_name} --disable-pytest-warnings
    
    deps = 
        -r requirements_dev.txt
    """.format(
        project_name=project_name
    )
    return inspect.cleandoc(file_contents)
