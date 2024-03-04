#!/usr/bin/python3
""""""

import json
import os

class FileStorage:
	""""""
	__file_path = "file.json"
	__objects = {}

	def __init__(self):
		pass

	def all(self):
		return self.__objects

	def new(self, obj):
		for key, value in obj.items():
			self.__objects[f"{obj.__class__}.{value}"] = value

	def save(self):
		with open(self.__file_path, mode="w", encoding="utf-8") as f:
			f.write(json.dumps(self.__objects))

	def reload(self):
		if os.path.exists(self.__file_path):
			with open(self.__file_path, mode="r", encoding="utf-8") as f:
				self.__objects = json.loads(f.read())
