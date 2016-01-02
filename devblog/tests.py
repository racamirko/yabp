from django.test import TestCase

from offline_logic import *
from mdx_lightbox_gallery import SINGLE_IMG_RE
import re

# Create your tests here.
def test_is_image_good():
	assert(is_image("balbla.png") == True)
	assert(is_image("balbla.jpg") == True)
	assert(is_image("balbla.bmp") == True)
	assert(is_image("balbla.PNG") == True)
	assert(is_image("balbla.JpG") == True)
	assert(is_image("balbla.BMP") == True)

def test_is_image_good_with_paths():
	assert(is_image("/hehe/kuku/balbla.png") == True)

def test_is_image_bad():
	assert(is_image("/hehe/kuku/balbla.txt") == False)
	assert(is_image("/hehe/kuku/balbla.jiff") == False)
	assert(is_image("/hehe/kuku/balbla.cvs") == False)

def test_re_good_single_image():
	test_text = 'some text !![alt text][1] and some more text'
	regex = re.compile(SINGLE_IMG_RE)
	search_rez = regex.search(test_text)
	
	