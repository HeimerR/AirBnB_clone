#!/usr/bin/python3
""" engine """
import json
from ..base_model import BaseModel
from ..user import User
from ..place import Place
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    name_classes = {"BaseModel": BaseModel, "User": User,
                    "Place": Place, "State": State, "City": City,
                    "Amenity": Amenity, "Review": Review}

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
            for key, obj in sorted(aux_dict.items()):
                model = key.split(".")[0]
                modelval = FileStorage.name_classes.get(model)
                aux_dict.update({key : modelval(**obj)})
            FileStorage.__objects = aux_dict
        except FileNotFoundError:
            pass
    def delete(self, class_name, ids):
        aux = "{}.{}".format(class_name, ids)
        FileStorage.__objects.pop(aux)
        self.save()


