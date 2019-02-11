"""
Module with project structures for scaffold_tests.
"""
from pyscaffold.api import helpers

from myscaffold.files.file_generators import (generate_bandit,
                                              generate_codeclimate,
                                              generate_coveragerc,
                                              generate_docker_compose,
                                              generate_dockerfile,
                                              generate_dockerignore,
                                              generate_dotenv,
                                              generate_isort_cfg,
                                              generate_mdlrc,
                                              generate_pre_commit_config,
                                              generate_pyproject_toml,
                                              generate_readme,
                                              generate_requirements_dev_txt,
                                              generate_requirements_txt,
                                              generate_setup_cfg,
                                              generate_tox_ini)


def get_flask_project_structure(project_name: str, opts: dict) -> tuple:
    flask_root_files = {
        ".coveragerc": (generate_coveragerc(), helpers.NO_OVERWRITE),
        ".dockerignore": (generate_dockerignore(), helpers.NO_OVERWRITE),
        ".bandit.yml": (generate_bandit(), helpers.NO_OVERWRITE),
        ".codeclimate.yml": (generate_codeclimate(), helpers.NO_OVERWRITE),
        ".env": (generate_dotenv(), helpers.NO_OVERWRITE),
        "Dockerfile": (generate_dockerfile(), helpers.NO_OVERWRITE),
        "docker-compose.yml": (generate_docker_compose(), helpers.NO_OVERWRITE),
        ".isort.cfg": (generate_isort_cfg(), helpers.NO_OVERWRITE),
        ".mdlrc": (generate_mdlrc(), helpers.NO_OVERWRITE),
        ".pre-commit-config.yaml": (generate_pre_commit_config(), helpers.NO_OVERWRITE),
        "pyproject.toml": (generate_pyproject_toml(), helpers.NO_OVERWRITE),
        "README.md": (generate_readme(project_name), helpers.NO_OVERWRITE),
        "requirements_dev.txt": (generate_requirements_dev_txt(), helpers.NO_OVERWRITE),
        "requirements.txt": (generate_requirements_txt(), helpers.NO_OVERWRITE),
        "setup.cfg": (generate_setup_cfg(), helpers.NO_OVERWRITE),
        "tox.ini": (generate_tox_ini(project_name), helpers.NO_OVERWRITE),
        "app.py": "import flask",
    }

    flask_project_files = {
        "logger": {"__init__.py": " "},
        "routes": {"v1": {"__init__.py": " "}, "__init__.py": " "},
        "services": {"__init__.py": " "},
        "tests": {
            "unit": {"__init__.py": " "},
            "integration": {"__init__.py": " "},
            "resources": {"__init__.py": " "},
            "__init__.py": " ",
        },
    }

    return flask_root_files, flask_project_files


def get_dotfiles_structure(project_name: str, opts: dict) -> dict:
    dotfiles = {
        ".coveragerc": (generate_coveragerc(), helpers.NO_OVERWRITE),
        ".dockerignore": (generate_dockerignore(), helpers.NO_OVERWRITE),
        ".bandit.yml": (generate_bandit(), helpers.NO_OVERWRITE),
        ".codeclimate.yml": (generate_codeclimate(), helpers.NO_OVERWRITE),
        ".env": (generate_dotenv(), helpers.NO_OVERWRITE),
        "Dockerfile": (generate_dockerfile(), helpers.NO_OVERWRITE),
        "docker-compose.yml": (generate_docker_compose(), helpers.NO_OVERWRITE),
        ".isort.cfg": (generate_isort_cfg(), helpers.NO_OVERWRITE),
        ".mdlrc": (generate_mdlrc(), helpers.NO_OVERWRITE),
        ".pre-commit-config.yaml": (generate_pre_commit_config(), helpers.NO_OVERWRITE),
        "pyproject.toml": (generate_pyproject_toml(), helpers.NO_OVERWRITE),
        "README.md": (generate_readme(project_name), helpers.NO_OVERWRITE),
        "requirements_dev.txt": (generate_requirements_dev_txt(), helpers.NO_OVERWRITE),
        "requirements.txt": (generate_requirements_txt(), helpers.NO_OVERWRITE),
        "setup.cfg": (generate_setup_cfg(), helpers.NO_OVERWRITE),
        "tox.ini": (generate_tox_ini(project_name), helpers.NO_OVERWRITE),
    }

    return dotfiles
