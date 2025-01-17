# Configuration file for the Sphinx documentation builder.

import os
import sys


# -- Path setup --------------------------------------------------------------

# To find the vc2_quantisation_matrices module
sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------

project = "SMPTE ST 2042-1 (VC-2) Quantisation Matrix Computation Routines"
copyright = "2021, BBC"
author = "BBC"

from vc2_quantisation_matrices import __version__ as version
release = version

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
    "sphinx.ext.mathjax",
    "numpydoc",
    "sphinxcontrib.inkscapeconverter",
    "sphinxcontrib.intertex",
]

# -- Options for numpydoc/autodoc --------------------------------------------

# Fixes autosummary errors
numpydoc_show_class_members = False

autodoc_member_order = "bysource"

add_module_names = False

autodoc_default_flags = [
    "members",
    "undoc-members",
]

# -- Options for intersphinx -------------------------------------------------

intersphinx_mapping = {
    "python": ("http://docs.python.org/3", None),
    "sympy": ("https://docs.sympy.org/latest/", None),
    "vc2_data_tables": ('https://bbc.github.io/vc2_data_tables/', None),
}


# -- Options for intertex ----------------------------------------------------

intertex_mapping = {
    "vc2_data_tables": [
        "{vc2_data_tables}/../docs/build/latex/*.aux",
        "https://bbc.github.io/vc2_data_tables/vc2_data_tables_manual.aux",
    ],
}


# -- Options for HTML output -------------------------------------------------

html_theme = "nature"

html_static_path = ["_static"]


# -- Options for PDF output --------------------------------------------------

latex_elements = {
    "papersize": "a4paper",
}
