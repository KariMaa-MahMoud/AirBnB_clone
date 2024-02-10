#!/usr/bin/python3
""" Command Line Interpreter"""
import cmd
import re
import sys
from models import *


class HBNBCommand(cmd.Cmd):
    """
    Customize console class
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Quits command interpreter with ctrl+d

        Args:
           line(args): input argument for quiting
           the terminal

        """
        return True

    def do_quit(self, line):
        """Handles the 'quit' command

        Args:
            line(args): input argument for quiting
            the terminal

        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
