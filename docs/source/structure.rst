The overall project directory structure
=======================================

The project is set up with a set of essential files in the root directory of the project, and with several subdirectories (which have various levels of importance). The first one, :file:`src/` is mandatory, all the others are option (but tests and documentation are a good thing to have). These are listed and explained below:

``src/``
    The :file:`src/` directory contains the package source code.

    This project does not use the older style of using the package name directly in the project, but instead uses an intermediate :file:`src/` directory. The reason for this is explained in the chapter on the use of a virtual environment, but in short, it better separates the source code from the installed package, and prevents potential mistakes such as missing files during the installation: the unit tests and such test the actually installed package, and not accidentally the development directory.

    The main (and normally only) directory inside :file:`src/` is the package name. Inside that directory, there is normally an :file:`__init__.py` file, several other modules, and possibly one or more subdirectories, which could be one or more subpackages inside the main package (subpackage is not an official name, but it is how I refer to such subdivisions).

    Some more details are in the :ref:`package-directory-structure` section.

``tests``
    Unit tests go into the :file:`tests` directory.

    The unit test files will often be named after the modules they test, prefixed with :file:`test_`. Similarly, the testing functions inside the test files are also prefixed with ``test_``. A number of unit test tools rely on this convention, so that, for example, helper functions and files will not be tested by themselves.

    Some projects prefer their test files inside the installed package itself. Here, the same conventions apply: create a subdirectory :file:`tests` inside the package (or subpackage, if you have those), and within those files, create :file:`test_<module name>` files with ``test_<function name>`` functions.


``docs``
    The :file:`docs/` directory contains the documentation for the project. This can be a single file, or something more structured, such as for this template. Sphinx, used here, is one tool to produce documentation; it can include parse through the actual code and obtain the doc-strings from the functions and classes in the code, creating API [#f1]_ documentation, next to other documentation such as as a user's guide, tutorials and general usage information. An example of another tool to create documentation is MkDocs. Perhaps the biggest thing to consider is what underlying markup language is used. Sphinx uses reStructuredText (reST) as a default, but it can work with Markdown; MkDocs uses Markdown. reST can be a bit more cumbersome, but it's the default in Python doc-strings, and Sphinx has extensions to also handle NumPy-style doc-strings.

``examples/``
    An examples directory can contain code snippets, notebook or small stand-alone scripts that showcase the use of the code.



.. _package-directory-structure:

The package directory structure
-------------------------------

The package




.. rubric:: Footnotes

.. [#f1] API: Application Programming Interface
