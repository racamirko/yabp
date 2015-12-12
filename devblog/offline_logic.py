import markdown as md
import os
from os.path import join, exists

from ..u02_blog import PATH_TO_TEXTS

from models import *


def process_new_folder(folder_path):
	full_text = []
	for _, _, files in os.walk(folder_path):
		for f_name in files:
			hnd_in = open(join(folder_path, f_name))
			full_text.append(md.markdown(''.join(hnd_in.readlines())))
			hnd_in.close()
	whole_text = ''.join(full_text)
	print("I would add:")
	print(whole_text)
	# TODO: add data logic here
	tmp_story = Story(title='', body=whole_text)


def process_texts():
	global PATH_TO_TEXTS
	for root, subfolders, files in os.walk(PATH_TO_TEXTS):
		for subf in subfolders:
			if not exists(join(root, subf, '.folder.imported')):
				process_new_folder(join(root, subf))

if __name__ == '__main__':
	# TODO: add some protection against random execution
	process_texts()