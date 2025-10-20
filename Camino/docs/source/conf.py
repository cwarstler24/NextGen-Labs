# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os

#sys.path.insert(0, os.path.abspath(os.path.join("..", "..", 'camino')))
#appdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
#print("AppDir", appdir)
#sys.path.insert(0, appdir)
#sys.path.insert(0, os.path.abspath(os.path.join(appdir, 'camino')))
#sys.path.insert(0, os.path.abspath(os.path.join(appdir, 'camino', 'config')))
#sys.path.insert(0, os.path.abspath(os.path.join(appdir, 'camino', 'logger')))
#sys.path.insert(0, os.path.abspath(os.path.join(appdir, 'camino', 'model')))
#sys.path.insert(0, os.path.abspath(os.path.join(appdir, 'camino', 'model', 'database')))
#sys.path.insert(0, os.path.abspath(os.path.join(appdir, 'camino', 'model', 'webservice')))
#sys.path.insert(0, os.path.abspath(os.path.join(appdir, 'camino', 'view')))



#sys.path.insert(0, os.path.abspath('..'))
#sys.path.insert(0, os.path.abspath('../../..'))  # Source code dir relative to this file
#sys.path.insert(0, os.path.abspath('../..'))  # Source code dir relative to this file

appdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, appdir)


print("Path", sys.path)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Camino'
copyright = '2023, Jonathan Earl'
author = 'Jonathan Earl'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx.ext.todo',
    'sphinx.ext.autosummary',
    'autoapi.extension'
]

autoapi_dirs = ['path/to/source/files', 'src']

try:
   import sphinxcontrib.spelling
except ImportError:
    pass
else:
    extensions.append('sphinxcontrib.spelling')

templates_path = ['_templates']
exclude_patterns = ['_build']
autosummary_generate = True

master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxdoc'
html_static_path = ['_static']
