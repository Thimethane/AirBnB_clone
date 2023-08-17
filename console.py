#!/usr/bin/python3
"""Command Interpreter Module"""
import cmd
import shlex
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = ["Amenity", "BaseModel", "City", "Place", "Review", "State", "User"]

    def do_create(self, args):
        """Create a new instance, save it, and print its ID.
        Usage: create <class name>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0] + "()")
            models.storage.save()
            print(new_instance.id)

    def do_show(self, args):
        """Print the string representation of a specific instance.
        Usage: show <class name> <id>
        """
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            obj_dict = models.storage.all()
            key = strings[0] + "." + strings[1]
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance.
        Usage: destroy <class name> <id>
        """
        args = args.split()
        objects = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in objects:
                objects.pop(key, None)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Print string representations of all instances.
        Usage: all <class name>
        """
        args = args.split()
        objects = models.storage.all()
        instances_list = []

        if len(args) == 0:
            for obj in objects.values():
                instances_list.append(obj.__str__())
            print(instances_list)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    instances_list.append(obj.__str__())
            print(instances_list)

    def do_update(self, args):
        """Update an instance.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        objects = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            obj = objects.get(key, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        """Check if a class name is provided."""
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Check if class ID is provided."""
        if len(name.split(" ")) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """Find the class name."""
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + "." + args[1]
                    return key
                else:
                    print("** class doesn't exist **")
                    return None

    def do_quit(self, args):
        """Exit the program"""
        return True

    def do_EOF(self, args):
        """Handle end of file"""
        return True

    def emptyline(self):
        """Do nothing when user presses enter on an empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
