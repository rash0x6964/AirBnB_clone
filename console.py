#!/usr/bin/python3
"""A module that contains the entry point of the command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """This class handle all the CMD interpreter"""

    prompt = "(hbnb) "

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
