#!/usr/bin/python3
""" console module for Airbnb  """
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State



class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'Place', 'City', 'Review', 'Amenity', 'State']
    
    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True
    def help_quit(self):
        """
        help quite prints the usage and exits the program
        """
        print ("Quit command to exit the program")

    def do_EOF(self, line):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        return True
    def empty_line(self):
        """
        Do nothing when an empty line is entered.
        """
        pass
    
    def do_creat (self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
        cmds = shlex.split(arg)
        
        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(f"{cmds[0]}()")
            storage.save()
            print(new_obj.id)
            
    
    def do_show (self, arg):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
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
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
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
        """
        Print the string representation of all instances or a specific class.
        Usage: <User>.all()
                <User>.show()
        """
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
     
    def default(self, arg):
        """
        Default behavior for cmd 
        """
        
        arglist = arg.split('.')
        class_incm_name = arglist[0]
        cmd = arglist[1].split("(")
        method_incm = cmd[0]
        more_arg = cmd[1].split(")")[0]
        method_dict = {
             'all': self.do_all,
             'destroy': self.do_destroy,
             'update': self.do_update,
             'show': self.do_show,
             'count': self.do_count
        }
         
        if method_incm in method_dict.keys():
            return method_dict[method_incm]("{} {}".format(class_incm_name, more_arg))
        print("*** Uknown syntax: {}".format(arg))
        return False
                               
    def do_update (self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        """
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
                attr_value = cmds[3]
                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()
                
    def do_count(self, arg):
        """
        Counts and retrieves the number of instances of a class
        usage: <class name>.count()
        """
        objs = storage.all()
        
        cmds = shlex.split(arg)
        
        if arg:
            incoming_class_name = cmds[0]
            
        count = 0
        if cmds:
            if incoming_class_name in self.classes:
                for obj in objs.values():
                    if obj.__class__.__name__ == incoming_class_name:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")    
        else:
            print("** class name missing **")
            
                    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()