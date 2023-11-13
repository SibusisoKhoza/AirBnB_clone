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
        user_instances = [obj for obj in storage.all().values() if isinstance(obj, cls)]
        return len(user_instances)
