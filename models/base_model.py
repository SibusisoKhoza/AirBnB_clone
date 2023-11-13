#!/usr/bin/python3
""" Defines the class: BaseModel """
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        md = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                        setattr(self, key, md)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        Returns:
            str: A formatted string.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Saves the current instance to the storage.
        """
        from models.engine.file_storage import FileStorage  # Import here to avoid circular import
        storage = FileStorage()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        Returns:
            dict: A dictionary containing all attributes of the instance.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
