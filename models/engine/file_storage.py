#!/usr/bin/python3
""" engine """
import json
from ..models.base_model import BaseModel


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
               print("read from file:")
               print(aux_dict)
               aux_dict2 = {}
            for key, obj in aux_dict.items():
                print("hola")
                aux_dict2.update({key : BaseModel(**obj)})
            print(aux_dict2)
            FileStorage.__objects = aux_dict2
        except:
            pass



