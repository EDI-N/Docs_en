#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Docs documentation build configuration file, created by
# sphinx-quickstart on Thu Dec 20 17:53:45 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinxcontrib.contentui',
    'sphinxcontrib.plantuml',
    'notfound.extension',
    'versionwarning.extension',
]

# for 404 page
notfound_default_language = 'en'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# добавил для возможности использования файлов .md
from recommonmark.parser import CommonMarkParser

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md']

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Docs'
copyright = '2022, EDIN'
author = 'EDIN'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.1'
# The full version, including alpha/beta/rc tags.
release = '0.0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = ['ru', 'uk_UA', 'en']

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# Это самый рабочий вариант:
html_theme = 'sphinx_rtd_theme'

def setup(app):
    app.add_stylesheet('theme_overrides.css')
    app.add_javascript('galaga.js')

# old js was added like this
#def setup(app):
#    app.add_stylesheet('theme_overrides.css')
#    app.add_javascript('galaga.js')

html_js_files = [
    'lang.js',
    'galaga.js',
]

# А это то, что я нагородил (не используй это):
# import os
# on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
# 
# if not on_rtd:  # only import and set the theme if we're building docs locally
#   import sphinx_rtd_theme
#   html_theme = 'sphinx_rtd_theme'
#   html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# else:
#   html_context = { 
#     'css_files': [
#         'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
#         'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
#         '_static/theme_overrides.css',
#     ],
# }

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme_options = {
    'logo_only': True,
    'display_version': False
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/logo_edin3.png"

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon-yellow-blue.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Docsdoc'

# -- Options for LaTeX output ---------------------------------------------

# latex_engine = 'xelatex' have no idea why it was here

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'Docs.tex', 'Docs Documentation',
     'Docs', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'docs', 'Docs Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Docs', 'Docs Documentation',
     author, 'Docs', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
#epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True

# -- sphinx-version-warning config ----------------------------------------------

versionwarning_messages = {
    "latest": (
        "<span нelpapu='lang'><svg width='22' height='29' viewBox='0 0 22 29' fill='none' xmlns='http://www.w3.org/2000/svg'><mask id='mask0_1335_8391' maskUnits='userSpaceOnUse' x='0' y='0' width='22' height='29' style='mask-type: alpha;'><path d='M8.24365 19.6805C8.24365 19.7009 8.24434 19.7211 8.24462 19.7414H9.19177C9.19102 19.7161 9.19044 19.6906 9.19015 19.6652C9.18979 19.6443 9.18951 19.6233 9.18947 19.6024C9.18875 19.2864 9.26112 18.9793 9.26974 18.8597C9.51839 17.0353 10.7041 16.2545 10.7293 16.238C10.8111 16.309 11.9721 17.2562 12.193 18.8839C12.2013 19.0034 12.2681 19.313 12.2721 19.6293C12.2726 19.6503 12.2729 19.6713 12.2728 19.6924C12.2727 19.7087 12.2725 19.7251 12.2722 19.7414H13.2172C13.2176 19.7211 13.2182 19.701 13.2182 19.6805C13.2182 18.0758 12.5398 16.937 11.8916 16.2149H11.9101C11.356 15.0414 11.2562 13.7287 11.3132 12.4257C11.3678 11.1804 11.4086 9.57345 11.4553 8.32784C11.4807 7.64729 11.3183 7.01729 10.8592 6.46772C10.8314 6.43442 10.7446 6.35086 10.7209 6.33559C10.7209 6.33559 10.6105 6.43565 10.5827 6.46884C10.1236 7.01845 9.96127 7.64841 9.98675 8.32892C10.0334 9.5745 10.0742 11.1814 10.1288 12.4268C10.1855 13.7234 10.1257 15.0509 9.55524 16.2073C8.91167 16.9211 8.24365 18.0536 8.24365 19.6805V19.6805Z' fill='#333333'></path><path d='M16.0804 8.11164C16.0531 8.11561 16.0342 8.11431 16.0191 8.12135C15.9758 8.1415 15.9325 8.16256 15.8919 8.18754C15.3354 8.52984 14.8543 8.95783 14.4485 9.47119C13.6342 10.5014 13.2374 11.6855 13.1345 12.9876C13.0798 13.6813 12.9793 14.3714 12.9019 15.0633C12.8627 15.4131 12.8291 15.7635 12.7927 16.1165C13.1345 16.06 13.3999 16.1858 13.6274 16.3937C13.9388 16.6784 13.9904 17.1393 13.724 17.4675C13.6021 17.6175 13.4176 17.7243 13.2449 17.8252C13.2385 17.8289 13.2321 17.8325 13.2259 17.8359C13.3218 18.1063 13.3999 18.398 13.4532 18.7114C13.4734 18.704 13.4952 18.6961 13.5076 18.6917C14.2304 18.437 14.6755 17.9427 14.7846 17.1714C14.8774 16.5147 14.5174 15.8185 13.9051 15.4658C13.8006 15.4057 13.7675 15.3492 13.7823 15.2284C13.8763 14.4596 13.9761 13.6912 14.0455 12.92C14.1098 12.2057 14.3085 11.5453 14.619 10.896C14.7638 10.593 15.1753 9.98934 15.1753 9.98934C15.1753 9.98934 15.1753 16.7454 15.1753 20.1055H11.5428V20.9198H12.1514C11.9689 21.7972 11.5267 22.3843 11.1833 22.7248V19.9563C11.2346 19.7399 11.397 19.4504 11.8813 19.3048C11.9057 19.2975 11.93 19.289 11.9544 19.2805C11.9386 19.1508 11.9213 19.0445 11.9177 18.9873C11.8942 18.7969 11.8596 18.6192 11.8175 18.453C11.7333 18.4799 11.6634 18.5029 11.6135 18.5211C11.3084 18.6319 10.8338 19.0325 10.7322 19.115C10.6306 19.0325 10.156 18.6319 9.85085 18.5211C9.80099 18.5029 9.73111 18.4799 9.64692 18.453C9.60479 18.6192 9.57021 18.7969 9.54674 18.9873C9.54307 19.0445 9.52578 19.1508 9.51 19.2805C9.53437 19.289 9.55874 19.2975 9.58315 19.3048C10.0583 19.4477 10.2236 19.7291 10.2781 19.9441V22.7143C9.93652 22.3685 9.49662 21.7794 9.3121 20.9197H9.92462V20.1055H6.28599V9.98931C6.28599 9.98931 6.69741 10.5931 6.84228 10.896C7.15279 11.5453 7.35148 12.2057 7.41579 12.9199C7.48524 13.6911 7.58496 14.4596 7.67896 15.2283C7.69377 15.3492 7.66063 15.4056 7.55613 15.4658C6.94383 15.8185 6.58389 16.5147 6.6767 17.1714C6.78573 17.9426 7.23091 18.437 7.95367 18.6917C7.96554 18.6958 7.98585 18.7032 8.00533 18.7104C8.05724 18.395 8.13345 18.1021 8.22734 17.8313C8.22368 17.8293 8.22008 17.8273 8.21634 17.8251C8.04369 17.7243 7.8591 17.6175 7.73727 17.4674C7.47086 17.1393 7.52245 16.6783 7.83386 16.3937C8.06134 16.1858 8.32674 16.0599 8.6686 16.1165C8.63215 15.7635 8.59854 15.4131 8.55939 15.0633C8.482 14.3713 8.38152 13.6813 8.32674 12.9875C8.22389 11.6854 7.82714 10.5014 7.01278 9.47115C6.607 8.9578 6.12584 8.52984 5.56941 8.18751C5.52875 8.16252 5.48547 8.14147 5.44215 8.12132C5.42705 8.11431 5.40814 8.11561 5.38086 8.1116V20.9199H8.33857C8.79331 23.0741 10.7306 24.0446 10.7306 24.0446C10.7306 24.0446 12.6779 23.1168 13.1262 20.9199H16.0805V8.1116L16.0804 8.11164Z' fill='#333333'></path></mask><g mask='url(#mask0_1335_8391)'><rect y='5.5' width='22' height='19.8' fill='#0082D1'></rect><rect y='15.4' width='22' height='9.9' fill='#0082D1'></rect></g></svg> Help Ukraine’s Armed Forces </span>"
    ),
}

# Show warning at top of page
versionwarning_body_selector = "div.document"
versionwarning_banner_title = ""
# For debugging locally
# versionwarning_project_version = "stable"
