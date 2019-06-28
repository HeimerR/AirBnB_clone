#!/usr/bin/python3
"""base model"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ class base model """
    def __init__(self, *args, **kwargs):
        if (kwargs):
                for key, value in kwargs.items():
                    if key != "__class__":
                        if key == "created_at" or key == "updated_at":
                            val = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                            setattr(self, key, val)
                        else:
                            setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    def __str__(self):
        cls = type(self).__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        dictionary  =  self.__dict__
        dictionary.update({'__class__' : type(self).__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
