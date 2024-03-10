#!/usr/bin/python3
""" console """
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models import User


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb)"
    classes = ['BaseModel', 'User']
    
    def do_quit(self, arg):
        """
        """
        return True
    def help_quit(self):
        """
        """
        print ("Quit command to exit the program")

    def do_EOF(self, line):
        """
        """
        print ()
        return True
    def do_empty_line(self):
        pass
    
    def do_creat (self, arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(f"{cmds[0]}.()")
            storage.save()
            print(new_obj.id)
            
    
    def do_show (self, arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(cmds[0], cmds[1])
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")
            
        
    def do_destroy (self, arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(cmds[0], cmds[1])
            if key in objs:
                del objs[key]
            else:
                print("** no instance found **")
          
    def do_all (self, arg):
        objs = storage.all()
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            for key, value in objs.items():
                print(str(value))
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in objs.items():
                if key.split('.')[0] == cmds[0]:
                    print(str(value))
                            
    def do_update (self, arg):
        cmds = shlex.split(arg)
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(cmds[0], cmds[1])
            if key not in objs:
                print("** no instance found **")
            elif len(cmds) < 3:
                print("** attribute name missing **")
            elif len(cmds) < 4:
                print("** value missing **")
            else:
                obj = objs[key]
                attr_name = cmds[2]
                attr_val = cmds[3]
                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()
                    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()