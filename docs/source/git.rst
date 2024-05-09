Git: files to not store in your repository
==========================================

Proper versioning is important in software development, and Git is by far the most used tool. Anything related to versioning in this example project and documentation will be done with Git.

As far as versioning is concerned, lThis document only describes what files to ignore (and, Git-specific), how. In other words, what are the files relevant to keep for your project, and what are considered temporary files or local, developer-personal, files.

Temporary files
---------------

For starters, there are files to ignore, with the `.gitignore` file in the root folder. This file should contain patterns related to the project, not to the development style. You'll want to ignore byte-compiled Python files (`*.pyc`), and the `build/` directory when building the package. Note that you can put the `__pycache__` file here if you want to, but since Git works on a file bases, and the files in the `__pycache__/` directory are all `*.pyc` files, only using `*.pyc` tends to be good enough. So ``.gitignore`` could contain

.. code-block:: none

   *.pyc
   build/


Developer specific files
------------------------

The following are files, directories and patterns I don't put a `.gitignore` file, because they are specific to my development workflow, not necessarily that of the project.


the virtual environment directory
    Using a virtual environment is a development style specific to a person, not to the project (even if it's very practical to use). Since I don't know for 100% that I want to ignore every `.venv` or `venv`, I store this in a local file related to the project, namely `.git/info/exclude`, which has only one non-commented line for this particular project:
  
    .. code-block:: none

       .venv


automated backup files
    I'm using Emacs as editor, so I end up with lots of ``<filename>~`` Emacs backup files. While definitely useful at times, I want to ignore these for versioning. Since this is the case for all my projects, I'm using a ``$HOME/.git-core.excludesfile`` which contains the lines
  
    .. code-block:: none

       *~

 The ``.venv`` or ``venv`` could also be added here instead of in ``.git/info/exclude``, since you hardly ever want to store a virtual environment in Git (a virtual environment should always be built from basic principles, that is, a Python version and a list of packages to install. So you'd store the "principles", not the final result.).


editor-specific configuration files
    If someone else uses VS Code while I'm using Emacs, then a ``.vscode`` configuration file is of no use to me. It should go in ``.git/info/exclude``, or in ``$HOME/.git-core.excludesfile``.

    An exception might be a generic ``.editorconfig`` file in the root of the project, since this should work for all editors. It helps to keep the project in the same style. But these days I rely on formatters, which can do a much better job (they'll remove trailing whitespace, add or remove blank lines between functions and so on); I have never found a need for an ``.editorconfig`` file.


A note on  ``$HOME/.git-core.excludesfile``: you may have to configure Git for this to find the file. Use:

  .. code-block:: none

     git config --global core.excludesFile '~/.git-core.excludesfile'

(Actually, you can give it any name you want; this name just makes it abundantly clear. But ``.gitignore`` is probably a bad idea since it may cause confusion, even if your home directory is not a Git repository.)

You can see the setting in ``$HOME/.gitconfig``, in the ``[core]`` section.
