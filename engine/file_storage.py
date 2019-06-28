#!/usr/bin/python3
""" engine """


class FileStorage:
    __file_path = None
    __objects = {}

    def all(self):
        return self.__ojects
    def new(self, obj):
        cls = type(obj).__name__
        self.__objects.update({'{}.{}'.format(cls, obj.id) : obj})
    def save(self):
        with open(self.__file_path, mode="w") as file:
            file.write(json.dumps(self.__objects)
    def reload(self):
        try:
            with open(self.__file_path) as file:
               self.__objects = json.loads(file.read)
        except:
            pass



