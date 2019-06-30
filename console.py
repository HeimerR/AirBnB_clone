#!/usr/bin/python3
""" commenst """
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    name_classes = {"BaseModel": BaseModel}
    
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
        if cls == "":
            print("** class name missing **")
        elif cls in HBNBCommand.name_classes:
            aux = HBNBCommand.name_classes.get(cls)() 
            aux.save()
            print(aux.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        list_arg = line.split(" ")
        if list_arg[0] == "":
            print("** class name missing **")
        elif (list_arg[0] != "BaseModel"):
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        else:
            dict_objs = storage.all()
            aux = "BaseModel.{}".format(list_arg[1])
            if aux in dict_objs.keys():
                print(dict_objs[aux])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
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
        if (line == ""):
            list_obj = list(storage.all().values())
            print(list(map(lambda x: str(x), list_obj)))
        elif (line == "BaseModel"):
            list_obj = list(storage.all().values())
            list_obj = filter(lambda x: type(x) is BaseModel, list_obj)
            print(list(map(lambda x: str(x), list_obj)))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        list_arg = line.split(" ")
        if list_arg[0] == "":
            print("** class name missing **")
        elif (list_arg[0] != "BaseModel"):
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif "BaseModel.{}".format(list_arg[1]) not in storage.all().keys():
            print("** no instance found **")
        elif len(list_arg) == 2:
            print("** attribute name missing **")
        elif len(list_arg) == 3:
            print("** value missing **")
        else:
            dict_objs = storage.all()
            aux = "BaseModel.{}".format(list_arg[1])
            if aux in dict_objs.keys():
                attr = getattr(dict_objs[aux], list_arg[2], "")
                setattr(dict_objs[aux], list_arg[2], type(attr)(list_arg[3]))



if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
