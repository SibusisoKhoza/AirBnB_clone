#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models import base_model
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review




class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review,
    }

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                for key, value in json_data.items():
                    class_name, obj_id = key.split('.')
                    obj_cls = getattr(base_model, class_name)
                    obj = obj_cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
