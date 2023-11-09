"""The Console Module"""
import cmd

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class, sub class of the CMD instance """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Type quit to exit the program """
        exit()

    def do_EOF(self, arg):
        """ Type EOF to quit the program """
        print('')
        exit()

    def emptyline(self):
        """ Ignores empty lines entered by a user """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
