#!/usr/bin/python3
"""
This is the console for the Airbnb project.
"""
import cmd
from models import storage
from models.base_model import BaseModel


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
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        class_name, _, obj_id = arg.partition(" ")
        if class_name not in storage.get_classes():
            print("** class doesn't exist **")
            return

        if not obj_id:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

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
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        instances = []
        if not args:
            for key, value in storage.all().items():
                instances.append(str(value))
            print(instances)
        elif args[0] not in storage.get_classes():
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if args[0] == key.split('.')[0]:
                    instances.append(str(value))
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and ID"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.get_classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        instance = storage.all()[key]
        attribute = args[3]
        value = args[4]

        # Update instance with attribute and value from dictionary
        instance_dict = instance.to_dict()
        instance_dict[attribute] = value

        # Update instance attributes and save to JSON file
        for k, v in instance_dict.items():
            setattr(instance, k, v)
        instance.save()

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                count = storage.count(class_name)
                print(count)
            except Exception as e:
                print(e)

    def do_all_with_method(self, arg):
        """Prints all instances of a class using <class name>.all() syntax"""
        args = arg.split()

        if len(args) != 1:
            print("** Unknown syntax: {}.all()".format(args[0]))
            return

        class_name = args[0]
        if class_name not in storage.get_classes():
            print("** class doesn't exist **")
        else:
            instances = storage.all_by_class(class_name)
            print(instances)

    def default(self, line):
        """Called on an input line when the command
        prefix is not recognized.
        """
        parts = line.split(".")
        if len(parts) == 2 and parts[1] == "all()":
            self.do_all_with_method(parts[0])
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
