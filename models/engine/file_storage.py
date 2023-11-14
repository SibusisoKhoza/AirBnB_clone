from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    classes = {
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
        # Add other classes as needed
    }

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(json_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for key, value in data.items():
                class_name = key.split('.')[0]
                instance = FileStorage.classes[class_name](**value)
                FileStorage.__objects[key] = instance
            FileStorage.classes = {k: eval(k) for k in data.keys()}
        except Exception:
            pass

    def count(self, class_name):
        count = 0
        for key in self.__objects:
            if class_name in key:
                count += 1
        return count

    def all_by_class(self, cls):
        """Returns a dictionary of instances of a specific class"""
        class_objects = {}
        for key, value in self.__objects.items():
            if type(value).__name__ == cls:
                class_objects[key] = value
        return class_objects

    @staticmethod
    def get_classes():
        return FileStorage.classes
