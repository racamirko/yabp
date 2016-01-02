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
"""


from __future__ import absolute_import
from __future__ import unicode_literals
import markdown
from markdown import Extension
from markdown.preprocessors import Preprocessor
from markdown.inlinepatterns import Pattern


SINGLE_IMG_RE = r'[!]{2}(\[(?P<img_index>\d+?)(?P<alt_text>\:.+?)?\])+'

class LighthouseExtension(Extension):
    """
        [img:1] individual images
        [gallery:4-19] a gallery is created with the python array handling rules
    """

