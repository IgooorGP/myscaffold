"""
Module with the argument parsers of the application.
"""
import argparse


def parse_args() -> dict:
    """
    Parses user arguments and returns and dict with such values.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("project_name")
    parser.add_argument("-t", "--type", required=True)
    # parser.add_argument("-d", "--debug", default=None, nargs="?", const=True)
    args = vars(parser.parse_args())

    return args
