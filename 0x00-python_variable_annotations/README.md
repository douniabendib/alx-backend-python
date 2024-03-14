<h1>0x00. Python - Variable Annotations</h1>
General:
Type annotations in Python 3
How you can use type annotations to specify function signatures and variable types
Duck typing
How to validate your code with mypy

Advanced Python
Python is a dynamically-typed language. That means that variable types are dynamically set at run-time, upon assignment of a value to a variable.

In Python 3, type annotations do not change this. Python is still a dynamically-typed language. Type annotations serve the following purpose:
1-Code documentation: thanks to them, a developer reading type-annotated code (his own or someone else’s) will know exactly what type each variables is supposed to be. This helps reduce bugs and exceptions and accelerate the development cycle.
2-Linting and validation: code editors and continuous integration (CI) pipelines can be configured to automatically validate type-annotated code at build-time and catch bugs before they make it to production.

