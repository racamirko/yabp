"""
Markdown lightbox2 gallery extension for Python-Markdown
=========================================

Extends python-markdown library to incude lightbox2-annotated images.

The extension should be provided with 

copyright @2015 Mirko Raca <mirko@analog.computer>
"""


from __future__ import absolute_import
from __future__ import unicode_literals
import markdown
from markdown import Extension
from markdown.preprocessors import Preprocessor
from markdown.inlinepatterns import Pattern


CUSTOM_CLS_RE = r'[!]{2}(?P<class>.+)[|](?P<text>.+)[!]{2}'

class LighthouseExtension(Extension):
    """
        [img:1] individual images
        [gallery:4-19] a gallery is created with the python array handling rules
    """

