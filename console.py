#!/usr/bin/python3
"""
    This module has the HBNBCommand class that
    implements the cmd module which provides a simple framework
    for writing line-oriented command interpreters.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
import sys


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    classes = [
        "BaseModel",
        "User",
        "Place",
        "Review",
        "State",
        "City",
        "Amenity"
    ]

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Closes the console and returns True\n")

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        pass

    def do_create(self, arg):
        try:
            inst = getattr(sys.modules[__name__], arg)()
            print(inst.id)
            inst.save()
        except Exception:
            if not arg:
                print("** class name missing **")
            else:
                print("** class doesn't exist **")

    def help_create(self):
        print("Creates a new instace of an object\n")

    def do_show(self, arg):
        arguments = arg.split()
        if not arg:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            key = f"{arguments[0]}.{arguments[1]}"
            inst = storage.all()
            if key in inst:
                print(inst[key])
            else:
                print("** no instance found **")

    def help_show(self):
        print("Prints the string representation of an instance based on\
 the class name and id\n")

    def do_destroy(self, arg):
        arguments = arg.split()
        if not arg:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            key = f"{arguments[0]}.{arguments[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def help_destroy(self):
        print("Deletes an instance based on the class name and id\n")

    def do_all(self, arg):
        arguments = arg.split()
        if len(arg) < 1:
            inst = storage.all()
            the_list = []
            for key, value in inst.items():
                the_list.append(str(value))
            print(the_list)
        elif arguments[0] in self.classes:
            inst = storage.all()
            the_list = []
            for key, value in inst.items():
                if key.split(".")[0] == arguments[0]:
                    the_list.append(str(value))
            print(the_list)
        else:
            print("** class doesn't exist **")

    def help_all(self):
        print("Prints all string representation of all instances based\
 or not on the class name\n")

    def do_update(self, arg):
        arguments = arg.split()
        if not arg:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            key = f"{arguments[0]}.{arguments[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
            elif len(arguments) < 3:
                print("** attribute name missing **")
            elif len(arguments) < 4:
                print("** value missing **")
            else:
                content = arguments[3]

                element = storage.all()[key]
                element.__setattr__(arguments[2], content)
                element.save()

    def help_update(self):
        print("Updates an instance based on the class name and id by\
 adding or updating attribute\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
