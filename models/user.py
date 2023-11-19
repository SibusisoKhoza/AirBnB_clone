from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    @classmethod
    def count(cls):
        """Returns the number of instances of User"""
        arr = [obj for obj in storage.all().values() if isinstance(obj, cls)]
        user_instances = arr
        return len(user_instances)
