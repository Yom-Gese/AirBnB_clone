#!/usr/bin/python3
"""
Defines the entry point to out command interpreter
Our command interpreter manages the objects of our project
(i.e: create new objects, retrieve an object, update and do operations on them,
destroy an object)
"""
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import os
import shlex


class HBNBCommand(cmd.Cmd):
    """Entry point of our command interpreter.
    Defines the commands that can be used with our command interpreter to
    navigate it as well as manage the objects of our project"""

    prompt = "(hbnb) "
    intro = "Welcome to the console!\nPlease input help or ? to diplay the\
 commands available."
    valid_classes = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }

    def do_create(self, line):
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return False
        new_object = HBNBCommand.valid_classes[args[0]]()
        print(new_object.id)
        new_object.save()

    def help_create(self):
        print("\n".join([
            "Usage: create <class name>",
            "Creates a new instance of the class specified",
            "and prints its id."
        ]))

    def do_show(self, line):
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.valid_classes:
            if len(args) > 1:
                all_objs = storage.all()
                key = f"{args[0]}.{args[1]}"
                if key in all_objs:
                    print(all_objs[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("class doesn't exist **")

    def help_show(self):
        print("\n".join([
            "Usage: show <class name> <instance id>",
            "Prints the string representation of an instance",
            "based on the class name and id"
        ]))

    def do_destroy(self, line):
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.valid_classes:
            if len(args) > 1:
                all_objs = storage.all()
                key = f"{args[0]}.{args[1]}"
                if key in all_objs:
                    all_objs.pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def help_destroy(self):
        print("\n".join([
            "Usage: destroy <class name> <instance id>",
            "Deletes an instance based on the class name and id",
            "Changes are saved to the file storage"
        ]))

    def do_all(self, line):
        args = shlex.split(line)
        all_objs = storage.all()
        my_list = []
        if len(args) == 0:
            for obj in all_objs.values():
                my_list.append(str(obj))
            print(my_list)
        elif args[0] in HBNBCommand.valid_classes:
            for key, value in all_objs.items():
                if key.startswith(args[0]):
                    my_list.append(str(value))
            print(my_list)
        else:
            print("** class doesn't exist **")

    def help_all(self):
        print("\n".join([
            "Usage: all / all <class name>",
            "Prints string representations of all the instances",
            "Based on the class name",
            "If no class name is specified, all instances are printed"
        ]))

    def do_update(self, line):
        args = shlex.split(line)
        int_values = [
            'number_rooms',
            'number_bathrooms',
            'max_guest',
            'price_by_night'
        ]
        float_values = [
            'latitude',
            'longitude'
        ]

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.valid_classes:
            if len(args) > 1:
                all_objs = storage.all()
                key = f"{args[0]}.{args[1]}"
                if key in all_objs:
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in int_values:
                                    try:
                                        args[3] = int(args[3])
                                    except Exception:
                                        args[3] = 0
                                elif args[2] in float_values:
                                    try:
                                        args[3] = float(args[3])
                                    except Exception:
                                        args[3] = 0
                            setattr(all_objs[key], args[2], args[3])
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def help_update(self):
        print("\n".join([
            "Usage: update <class name> <instance id> <attribute name>\
'<attribute value>'",
            "Updates an insatance based on the class name and id",
            "Adds or updates an attribute"
        ]))

    def do_shell(self, line):
        """Run a shell command"""

        print("Running the shell command: ", line)
        output = os.popen(line).read()
        print(output)

    def emptyline(self):
        """An empty line + ENTER in our command interpreter should not
        execute anything"""
        pass

    def do_EOF(self, line):
        """End of file: exit the program"""

        return True

    def do_quit(self, line):
        """Exit the program"""

        quit()

    def postloop(self):
        """Executed when cmd is about to return"""

        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
