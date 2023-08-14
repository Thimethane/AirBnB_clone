#!/usr/bin/python3
"""Defines the entry point of the HBnB console."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User"]

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file."""
        args = arg.split()
        if not arg:
            print("** class name missig **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist")
            return
        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key in storage.all():
            print(storage.all()[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key in storage.all():
            del storage.all()[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        if not arg:
            objs = storage.all().values()
        elif arg in self.valid_classes:
            objs = [
                obj for obj in storage.all()
                .values() if type(obj).__name__ == arg
                ]
        else:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objs])

    def do_update(self, arg):
        """Update an instance attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[obj_key]
        attr_name = args[2]
        attr_value = args[3]
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
