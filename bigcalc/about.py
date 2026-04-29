# about.py

import re
import os


def _get_setup_data():
    setup_path = os.path.join(os.path.dirname(__file__), "..", "setup.py")

    with open(setup_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content


def _extract(field):
    content = _get_setup_data()

    match = re.search(rf'{field}\s*=\s*["\'](.*?)["\']', content)

    if match:
        return match.group(1)

    return "Not Found"


def name():
    return _extract("name")


def version():
    return _extract("version")


def author():
    return _extract("author")


def author_email():
    return _extract("author_email")


def description():
    return _extract("description")


def python_requires():
    return _extract("python_requires")