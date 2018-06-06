import os
import sys


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'django-registration'
copyright = u'2007-2018, James Bennett'
version = '3.0-dev'
release = '3.0-dev'
exclude_trees = ['_build']
pygments_style = 'sphinx'
html_static_path = ['_static']
htmlhelp_basename = 'django-registrationdoc'
latex_documents = [
    ('index', 'django-registration.tex', u'django-registration Documentation',
     u'James Bennett', 'manual'),
]
if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Spelling check needs an additional module that is not installed by default.
# Add it only if spelling check is requested so docs can be generated without it.
if 'spelling' in sys.argv:
    extensions.append("sphinxcontrib.spelling")
    
# Spelling language.
spelling_lang = 'en_US'

# Location of word list.
spelling_word_list_filename = 'spelling_wordlist.txt'
