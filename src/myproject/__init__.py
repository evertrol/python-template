"""Package to showcase package structure.

This top-level __init__ file contains imports that are
available at the top-level (e.g. `from myproject import inter_simple`).

This specific module doc-string documents the overall
package use.

"""

# Make selected functions, classes and other items
# available at top level. Importing all, using `*`,
# can also be done here.
from .core import *
from .subpackage import *
