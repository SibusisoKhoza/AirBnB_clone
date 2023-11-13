#!/usr/bin/python3
"""
Command interpreter module
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
import shlex


classes = {"BaseModel": BaseModel, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review, "User": User}


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Handles empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it to JSON file"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            else:
                print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            else:
                del all_objects[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        all_objects = storage.all()
        if not args:
            print([str(obj) for obj in all_objects.values()])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in classes[args[0]].all()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(all_objects[key], args[2], args[3])
                storage.save()
    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        instance_count = storage.count(classes[class_name])
        print(instance_count)


    def do_User(self, line):
        """Handles commands related to the User class"""
        args = line.split()
        if args and args[0] == 'count':
            print(storage.count('User'))
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
