"""The core module provides core functionality.

Functions, classes and other items can be defined here,
but can also be imported from other modules and subpackages.

Note that items imported from other modules
will also be available to __init__ if that file
uses a wildcard import.

This file essentially takes over from __init__, leaving the
latter module to provide purely imports and a (module) doc-string.

"""

# __all__ is defined in our modules and subpackages,
# so it's safe to import *
from .integrate import integrate_simple
from .differentiate import differentiate_simple
