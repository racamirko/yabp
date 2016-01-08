"""
Markdown lightbox2 gallery extension for Python-Markdown
=========================================

Extends python-markdown library to incude lightbox2-annotated images.

The extension should be provided with a vector of image paths (to be served by
the web server).

Example syntax usage:

    Single image
      !![1:text for the image]

    Gallery
      !![1:note for the image][2:second image][3][4][5][6:again with notes]

    Gallery for a reange of images
      !![1]...[20]

copyright @2015 Mirko Raca <mirko@analog.computer>

Resources:
    https://pythonhosted.org/Markdown/extensions/api.html
    https://pythonhosted.org/Markdown/extensions/api.html#integrating_into_markdown

    Stopped at trying to find out what's the md.match object and etree output

"""


# from __future__ import absolute_import
# from __future__ import unicode_literals
import markdown
# from markdown import Extension
# from markdown.preprocessors import Preprocessor
from markdown.inlinepatterns import Pattern
from markdown.util import etree
import re


SINGLE_IMG_RE = r'[!]{2}(\[(?P<img_index>\d+?)(?P<alt_text>\:.+?)?\])+'

class LighthouseExtension(Pattern):
    """
        !![1:alt_text] individual images
        !![2:alt_text][3][5] gallery of several images with optional titles
    """

    def __init__(self, mapping):
        self.mapping = mapping

    def getCompiledRegExp():
        global SINGLE_IMG_RE
        return re.compile(SINGLE_IMG_RE)

    def handleMatch(m):
        # assert( isinstance(m, ) )
        pass



# def makeExtension(configs=None):
#     return LighthouseExtension(configs)