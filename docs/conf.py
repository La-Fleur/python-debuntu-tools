# Debian and Ubuntu system administration tools.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: July 11, 2017
# URL: https://debuntu-tools.readthedocs.io

"""Sphinx documentation configuration for the `debuntu-tools` project."""

import os
import sys

# Add the debuntu-tools source distribution's root directory to the module path.
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration -----------------------------------------------------

# Sphinx extension module names.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'humanfriendly.sphinx',
]

# Paths that contain templates, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'debuntu-tools'
copyright = '2017, Peter Odding'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# Find the package version and make it the release.
from debuntu_tools import __version__ as debuntu_tools_version  # NOQA

# The short X.Y version.
version = '.'.join(debuntu_tools_version.split('.')[:2])

# The full version, including alpha/beta/rc tags.
release = debuntu_tools_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# http://sphinx-doc.org/ext/autodoc.html#confval-autodoc_member_order
autodoc_member_order = 'bysource'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Refer to the Python standard library.
# From: http://twistedmatrix.com/trac/ticket/4582.
intersphinx_mapping = dict(
    python=('https://docs.python.org/2/', None),
    coloredlogs=('https://coloredlogs.readthedocs.io/en/latest/', None),
    debpkgtools=('https://deb-pkg-tools.readthedocs.io/en/latest/', None),
    executor=('https://executor.readthedocs.io/en/latest/', None),
    humanfriendly=('https://humanfriendly.readthedocs.io/en/latest/', None),
    propertymanager=('https://property-manager.readthedocs.io/en/latest/', None),
)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'nature'

# Output file base name for HTML help builder.
htmlhelp_basename = 'debuntutoolsdoc'
