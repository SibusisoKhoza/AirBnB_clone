from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    classes = {
        'BaseModel': BaseModel,
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
        """Reloads objects from JSON file"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for key, value in data.items():
                class_name = key.split('.')[0]
                instance = eval(class_name)(**value)
                self.__objects[key] = instance
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
        all_objects = self.all()
        return {k: v for k, v in all_objects.items() if isinstance(v, cls)}

    @staticmethod
    def get_classes():
        """Returns a dictionary of all available classes."""
        return FileStorage.classes
