#!/usr/bin/python3
"""
This is the console for the Airbnb project.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program at the end of file"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + "." + instance_id
                print(storage.all()[key])
            except IndexError:
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                elif len(args) < 2:
                    print("** instance id missing **")
                elif key not in storage.all():
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + "." + instance_id
                del storage.all()[key]
                storage.save()
            except IndexError:
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                elif len(args) < 2:
                    print("** instance id missing **")
                elif key not in storage.all():
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        instances = []
        if not args:
            for key, value in storage.all().items():
                instances.append(str(value))
            print(instances)
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                instance_id = args[1]
                attribute_name = args[2]
                attribute_value = args[3]
                key = class_name + "." + instance_id
                instance = storage.all().get(key)
                if instance:
                    setattr(instance, attribute_name, attribute_value)
                    storage.save()
                else:
                    print("** no instance found **")
            except IndexError:
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                elif len(args) < 2:
                    print("** instance id missing **")
                elif key not in storage.all():
                    print("** no instance found **")
                elif len(args) < 4:
                    print("** attribute name missing **")
                elif len(args) < 5:
                    print("** value missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
