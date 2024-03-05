#!/usr/bin/python3
"""A module that contains the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class handle all the CMD interpreter"""

    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation
            of an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            dict = storage.all()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in dict.keys():
                print("** no instance found **")
            else:
                print(dict[f"{args[0]}.{args[1]}"])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            dict = storage.all()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in dict.keys():
                print("** no instance found **")
            else:
                del dict[f"{args[0]}.{args[1]}"]
                storage.save()

    def do_all(self, line):
        """ Prints all string representation of
            all instances based or not on the class name.
        """
        dict = storage.all()
        if not line:
            print([str(obj) for obj in dict.values()])
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            tmpList = []
            for v in dict.values():
                if (v.__class__.__name__ == line):
                    tmpList.append(str(v))
            print(tmpList)

    def do_update(self, line):
        """ Updates an instance based on the class name
            and id by adding or updating attribute
        """
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            dict = storage.all()
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in dict.keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                cls, id, attr, val = args[:4]
                obj = dict[f"{cls}.{id}"]
                setattr(obj, attr, val)
                storage.save()

    def do_EOF(self, line):
        """typing Ctrl-D will drop us out of the interpreter."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
