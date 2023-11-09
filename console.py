#!/usr/bin/python3
"""The Console Module"""
import cmd

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class, sub class of the CMD instance """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Type <quit> to exit the program """
        exit()

    def do_EOF(self, arg):
        """ Type <EOF> to quit the program """
        print('')
        exit()

    def emptyline(self):
        """ Ignores empty lines entered by a user """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a valid Class, saves it (to the JSON file) and prints the id.
        Valid classes are: BaseModel, User, State, City, Amenity, Place, Review.
        Usage:	create <class name>
        """

        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
