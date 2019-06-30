#!/usr/bin/python3
"""
Entry point of the command interpreter
Use: ./console.py
(hbnb) <command>

"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Use of cmd class as an interpreter

    Class Attributes:
        prompt (str): custom prompt
        name_classes: dictionay of classes

    """
    prompt = "(hbnb) "
    name_classes = {"BaseModel": BaseModel, "User": User,
                    "Place": Place, "State": State, "City": City,
                    "Amenity": Amenity, "Review": Review}

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'Ctr + D to exit the program\n'
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, cls):
        'Creates a new instance: Usage \'create <class name>\'\n'
        if cls == "":
            print("** class name missing **")
        elif cls in HBNBCommand.name_classes:
            aux = HBNBCommand.name_classes.get(cls)()
            aux.save()
            print(aux.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        '''Shows an instance: Usage \'show <class name> <id>\'\n'''
        list_arg = line.split(" ")
        if list_arg[0] == "":
            print("** class name missing **")
        elif not list_arg[0] in HBNBCommand.name_classes:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        else:
            dict_objs = storage.all()
            aux = "{}.{}".format(list_arg[0], list_arg[1])
            if aux in dict_objs.keys():
                print(dict_objs[aux])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        'Deletes an instance: Usage \'destroy <class name> <id>\'\n'
        list_arg = line.split(" ")
        if list_arg[0] == "":
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.name_classes:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        else:
            dict_objs = storage.all()
            aux = "{}.{}".format(list_arg[0], list_arg[1])
            if aux in dict_objs.keys():
                storage.delete(list_arg[0], list_arg[1])
            else:
                print("** no instance found **")

    def do_all(self, line):
        'Shows all the instances: Usage \'all [<class name>]\'\n'
        if (line == ""):
            list_obj = list(storage.all().values())
            print(list(map(lambda x: str(x), list_obj)))
        elif line in HBNBCommand.name_classes:
            list_obj = list(storage.all().values())
            list_obj = filter(lambda x: type(x) is
                              HBNBCommand.name_classes.get(line), list_obj)
            print(list(map(lambda x: str(x), list_obj)))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        '''Updates an instance:
        Usage \'update <class name> <id> <attribute name> "<attribute value>"\'
        '''
        list_arg = shlex.split(line)
        if list_arg[0] == "":
            print("** class name missing **")
        elif not list_arg[0] in HBNBCommand.name_classes:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(list_arg[0], list_arg[1])
              not in storage.all().keys()):
            print("** no instance found **")
        elif len(list_arg) == 2:
            print("** attribute name missing **")
        elif len(list_arg) == 3:
            print("** value missing **")
        else:
            dict_objs = storage.all()
            aux = "{}.{}".format(list_arg[0], list_arg[1])
            if aux in dict_objs.keys():
                attr = getattr(dict_objs[aux], list_arg[2], "")
                setattr(dict_objs[aux], list_arg[2], type(attr)(list_arg[3]))
                dict_objs[aux].save()

    def do_User(selfi, line):
        '''functions for User:

        '''


if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
