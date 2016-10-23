# -*- coding: utf-8 -*-

import json
import codecs


class OkCorpPipeline(object):
	def __init__(self):
		self.file = codecs.open('ok_data.json', mode='wb', encoding='utf-8')
	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + '\n'
		self.file.write(line.decode("unicode_escape"))
		return item
