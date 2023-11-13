from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    @classmethod
    def count(cls):
        """Returns the number of instances of User"""
        return sum(1 for obj in storage.all().values() if isinstance(obj, cls))

