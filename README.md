# A Python template

A Python template for manually creating a new Python package.


This project is a Python template for new Python packages. Detailed documentation can be found in the docs directory.

This template is one among many options to structure a Python project, but it can serve as a starting point upon which to build.

## Quick overview

The template has a number of near-mandatory files and directories, with some optional. A quick list follows:

- pyproject.toml: for straightforward Python projects, this contains all the necessary information for the project to be successfully installed, as well as being listed in repositories. Project version, author information, license choice, dependencies to install for building, development tools used for extending the project and so on.

- README.md: a text file with a quick overview of the project. When in the correct format with the right extension, many sites will also render it for nicer reading.

- LICENSE: the actual license file with the full license text.

- Citation.cff: only useful when there is an accompanying article that can be referenced; so a bit more common in scientific code.

- a continuous-integration (CI) configuration file (or directory), such as a `.travis.yml`, a `.gitlab-ci.yml` or a `.github/workflows/testing.yml` file.

- src: the directory containing the actual code, often structured in modules and subpackages.

- scripts: optional directory for command-line scripts to be installed alongside the code.

- tests: optional directory with unit tests.

- docs: directory for the documentation. In this project, this is managed using Sphinx.


## Installation

You can simply download the zip file from GitHub, under the `Code` button.

Cloning the repository is also possible, but then you get all the Git extra, while you probably want to start a fresh Git repository for this project.

Once downloaded and unpacked, just change the directories and files as you see fit, and remove directories you won't be using.


## Documentation

More detailed information can be found in the `docs/` directory. You can build it if you have Sphinx installed:
```
cd docs
make html
```
and open `docs/build/html/index.html` in a browser.

Alternatively, you can read the documentation directly in the GitHub repository from source, starting in `docs/source/index.rst`. The files may not be fully rendered by GitHub, but they should be fairly readable.


## Virtual environment and testing

For testing, both installation and unit tests, a virtual environment (v-env) is preferred. This virtual environment can live in the project directory (but should not be stored in the repository) or anywhere the developer prefers. 

Using a v-env ensures that testing happens separately from the source tree. In part, this is also the reason the source files are under a `src/` directory, and not directly in the project root (which is, or perhaps rather was, more the standard style): that way, unit tests and other tests use the actually installed package (installed in the v-env) for their tests.

For practical development while having the package installed, create and activate the v-env:
```
python -m venv .venv
source .venv/bina/activate
```

Then install with
```
pip install -e '.[dev]'
```

The `[dev]` will also install the development dependencies, so this is not necessary for a normal installation.

The `-e` option installs as an editable package, so that changes in the source files are directly reflected in the installed files.

Ideally, for a full test run, you should recreate the v-env from scratch; some package creation tools handle this for you, but it's generally just the few manual steps  above.

Automated tests using continuous integration through your repository do this near-automatically for you, since these essentially set up a completely new environment (as a container or virtual machine), install the code and then run the tests.

## Licensing

The code and documentation are distributed under the 2-clause BSD License; see LICENSE for details.
