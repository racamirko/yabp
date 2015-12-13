import markdown as md
import os
from os.path import join, exists

from models import *

PATH_TO_TEXTS = '/home/raca/tmp/blog_texts'


def get_meta_data(filename):
	hnd_in = open(filename)
	title = ''
	tags = []
	for line in hnd_in.readlines():
		parts = line.split(":")
		if parts[0].lower() == 'title':
			title = parts[1].strip()
		elif parts[0].lower() == 'tags':
			tags = parts[1].strip().split(",")
			tags = map( lambda x : x.strip(), tags)
	return title, tags

def process_new_folder(folder_path):
	full_text = []
	title = ''
	story_tags = []
	for _, _, files in os.walk(folder_path):
		files.sort()
		for f_name in files:
			print("Processing: %s" % f_name)
			if f_name == '00_meta.txt':
				title, story_tags = get_meta_data(join(folder_path, f_name))
			else:
				hnd_in = open(join(folder_path, f_name))
				## TODO: expand MD processing here
				full_text.append(md.markdown(''.join(hnd_in.readlines())))
				hnd_in.close()
	whole_text = ''.join(full_text)
	print("I would add:")
	print(whole_text)
	# ORM
	tmp_story = Story(title=title, body=whole_text)
	tmp_story.save()
	# tags
	for t in story_tags:
		query = Tag.objects.filter(name=t)
		if query.exists():
			tag_object = query[0]
		else:
			tag_object = Tag(name=t)
			tag_object.save()
		tmp_story.tag.add(tag_object)
	tmp_story.save()

def process_texts():
	global PATH_TO_TEXTS
	for root, subfolders, files in os.walk(PATH_TO_TEXTS):
		for subf in subfolders:
			if not exists(join(root, subf, '.folder.imported')):
				process_new_folder(join(root, subf))
			else:
				print("Skipping: %s" % subf)

if __name__ == '__main__':
	# TODO: add some protection against random execution
	process_texts()
