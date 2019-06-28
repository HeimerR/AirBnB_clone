#!/usr/bin/python3
""" engine """
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    def new(self, obj):
        cls = type(obj).__name__
        FileStorage.__objects.update({'{}.{}'.format(cls, obj.id) : obj})
    def save(self):
        with open(FileStorage.__file_path, mode="w") as file:
            for obj in FileStorage.__objects.values():
                file.write(json.dumps(obj.to_dict()))
    def reload(self):
        try:
            with open(FileStorage.__file_path) as file:
               FileStorage.__objects = json.loads(file.read())
        except:
            pass



