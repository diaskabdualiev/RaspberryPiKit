# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Alash Raspberry Pi 5 Kit'
copyright = '2025, Dias Kabdualiyev'
author = 'Dias Kabdualiyev'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_favicon = '_static/favicon.png'
html_logo = '_static/logo.png'

html_theme_options = {
    "navigation_depth": 3,  # Показывать вложенные уровни
    "collapse_navigation": False,  # Оставлять меню открытым
}

html_static_path = ['_static']
html_css_files = ['custom.css']

extensions.append("sphinx.ext.todo")
extensions.append("sphinx_design")
extensions.append("sphinx.ext.imgmath")  # Улучшает работу с изображениями

todo_include_todos = True
