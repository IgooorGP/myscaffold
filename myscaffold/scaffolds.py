"""
Module with the pyscaffold extensio used to generate Flask-based
projects.
"""
from pyscaffold.api import Extension as PyScaffoldExtension
from pyscaffold.api import create_project, helpers

from myscaffold.structures import (get_dotfiles_structure,
                                   get_flask_project_structure)


class ScaffoldFlask(PyScaffoldExtension):
    """
    Scaffold extension class for Flask projects scaffold_tests.
    """

    def activate(self, actions):
        """Activate extension

        Args:
            actions (list): list of actions to perform

        Returns:
            list: updated list of actions
        """
        # adds a custom action (helpers always return a new list)
        actions = helpers.register(
            actions, self.create_my_own_structure, after="define_structure"
        )

        # removes the init git step
        actions = helpers.unregister(actions, "init_git")

        return actions

    def create_my_own_structure(self, struct, opts):
        """Perform some actions that modifies the structure and options

        Args:
            struct (dict): project representation as (possibly) nested
                :obj:`dict`.
            opts (dict): given options, see :obj:`create_project` for
                an extensive list.

        Returns:
            struct, opts: updated project representation and options
        """
        flask_root_files, flask_project_files = get_flask_project_structure(
            self.name, opts
        )

        struct = flask_root_files
        struct[self.name] = flask_project_files

        return struct, opts


class ScaffoldDotfiles(PyScaffoldExtension):
    """
    Scaffold extension class for dot files only.
    """

    def activate(self, actions):
        """Activate extension

        Args:
            actions (list): list of actions to perform

        Returns:
            list: updated list of actions
        """
        # adds a custom action (helpers always return a new list)
        actions = helpers.register(
            actions, self.create_my_own_structure, after="define_structure"
        )

        # removes the init git step
        actions = helpers.unregister(actions, "init_git")

        return actions

    def create_my_own_structure(self, struct, opts):
        """Perform some actions that modifies the structure and options

        Args:
            struct (dict): project representation as (possibly) nested
                :obj:`dict`.
            opts (dict): given options, see :obj:`create_project` for
                an extensive list.

        Returns:
            struct, opts: updated project representation and options
        """
        struct = get_dotfiles_structure(self.name, opts)

        return struct, opts


def build():
    create_project(
        project="my_test_folder",
        author="Your Name",
        license="mit",
        extensions=[ScaffoldDotfiles("my_flask")],
    )
