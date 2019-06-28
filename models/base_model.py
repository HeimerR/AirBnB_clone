#!/usr/bin/python3
"""base model"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ class base model """
    def __init__(self, *args, **kwargs):
        if (kwargs):
                for key, value in kwargs.items():
                    setattr(self, key, value)
                    print(self.__dict__)
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
