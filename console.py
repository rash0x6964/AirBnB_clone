#!/usr/bin/python3
"""A module that contains the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models import storage
import re

def validCls(cls):
    return cls in HBNBCommand.allowedObjs

class HBNBCommand(cmd.Cmd):
    """This class handle all the CMD interpreter"""

    prompt = "(hbnb) "
    allowedObjs = storage.supportedClss.keys()

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        elif not validCls(line):
            print("** class doesn't exist **")
        else:
            obj = storage.supportedClss[line]()
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
            if not validCls(args[0]):
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
            if not validCls(args[0]):
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
        elif not validCls(line):
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
            if not validCls(args[0]):
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

    def onecmd(self, s):
        """implement a specific cmd"""

        matchAll = re.match(r"^(.*?).all\(\)$", s)
        matchCount = re.match(r"^(.*?).count\(\)$", s)
        matchShow = re.match(r"^(.*?).show\((.*?)\)$", s)
        matchDestory = re.match(r"^(.*?).destroy\((.*?)\)$", s)
        matchUpdate = re.match(r"^(.*?).update\((.*?), (.*?), (.*?)\)$", s)

        if matchAll and validCls(matchAll.group(1)):
                self.do_all(matchAll.group(1))
        elif matchCount and validCls(matchCount.group(1)):
            l = []
            for obj in storage.all().values():
                if obj.__class__.__name__ == matchCount.group(1):
                    l.append(obj)
            print(len(l))
        elif matchShow and validCls(matchShow.group(1)):
            id = matchShow.group(2).strip('"') or ""
            argFormat = f"{matchShow.group(1)} " + id
            self.do_show(argFormat)
        elif matchDestory and validCls(matchDestory.group(1)):
            id = matchDestory.group(2).strip('"') or ""
            argFormat = f"{matchDestory.group(1)} {id}"
            self.do_destroy(argFormat)
        elif matchUpdate and validCls(matchUpdate.group(1)):
            id = matchUpdate.group(2).strip('"') or ""
            key = matchUpdate.group(3).strip('"') or ""
            value = matchUpdate.group(4).strip('"') or ""
            argFormat = f"{matchUpdate.group(1)} {id} {key} {value}"
            self.do_update(argFormat)
        else:
            return cmd.Cmd.onecmd(self, s)

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
