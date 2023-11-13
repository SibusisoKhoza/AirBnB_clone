#!/usr/bin/python3
import sys
import os
import unittest
from models.base_model import BaseModel
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_str_representation(self):
        self.n = self.model.__dict__
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, n)
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        """Test that the save method updates the created_at attribute."""
        original_created_at = self.model.created_at
        self.model.save()
        new_created_at = self.model.created_at
        self.assertEqual(original_created_at, new_created_at)
        #To still debug function

    def test_to_dict_method(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(
            model_dict['created_at'],
            self.model.created_at.isoformat()
        )
        self.assertEqual(
            model_dict['updated_at'],
            self.model.updated_at.isoformat()
        )


if __name__ == '__main__':
    unittest.main()
