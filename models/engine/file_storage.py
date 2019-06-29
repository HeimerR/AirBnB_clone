#!/usr/bin/python3
""" engine """
import json
from ..base_model import BaseModel


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
            aux_dict = {}
            for key, obj in FileStorage.__objects.items():
                aux_dict.update({key : obj.to_dict()})
            file.write(json.dumps(aux_dict))
    def reload(self):
        try:
            with open(FileStorage.__file_path) as file:
               aux_dict = json.loads(file.read())
            for key, obj in aux_dict.items():
                aux_dict.update({key : BaseModel(**obj)})
            FileStorage.__objects = aux_dict
        except:
            pass



