"""
Dump all variables, functions and classes in this file
which we are planning to use it in other programs

This is file is also called "PYTHON-MODULE" or "PYTHON-LIBRARY"
"""

course = "python"


def add(a, b):
    return a + b


class Employee:
    def add_name(self, name):
        self.name = name
    def view_name(self):
        return self.name