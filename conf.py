# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Quicken Already Purchased – Setup Guide'
copyright = '2026, Quicken Setup Guide'
author = 'Quicken Support Guide Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Prevent warnings related to raw HTML blocks
suppress_warnings = ['misc.highlighting_failure']

# -- Options for HTML output -------------------------------------------------

# Safe default theme (works everywhere)
html_theme = 'alabaster'

html_title = "Quicken Already Purchased – Download & Activate Guide"
html_short_title = "Quicken Setup Guide"

# Favicon (place inside _static folder)
html_favicon = '_static/quicken_favicon.ico'

# Hide source link and Sphinx footer
html_show_sourcelink = False
html_show_sphinx = False

# Static files (CSS, images, favicon)
html_static_path = ['_static']

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# -- HTML safety settings ----------------------------------------------------

# REQUIRED for buttons & footer using .. raw:: html
html_allow_unsafe = True
