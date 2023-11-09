import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class sub class of the CMD instance"""
    prompt = '(hbnb) '


if __name__ == '__main__':
    HBNBCommand().cmdloop()
