#!/usr/bin/python3
"""
Tests for the BaseModel
"""


import unittest
import datetime

# import base_models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def setUp(self):
        '''Tests for the BaseModel'''
        self.base_model = BaseModel()
        self.base_model1 = BaseModel()

    def tearDown(self):
        """_summary_
        """
        del self.base_model
        del self.base_model1

    def test_instances(self):
        """_summary_
        """        
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model1, BaseModel)

    def test_uuid(self):
        """_summary_
        """        
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model1, "id"))
        self.assertNotEqual(self.base_model.id, self.base_model1.id)

    def test_datetime(self):
        """_summary_
        """        
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

        datenow = datetime.datetime.now()
        self.testmodel = BaseModel()
        self.assertNotEqual(self.testmodel.created_at, datenow)
        self.assertNotEqual(self.testmodel.created_at,
                            self.testmodel.updated_at)
        self.testmodel.save()
        self.assertNotEqual(self.testmodel.created_at,
                            self.testmodel.updated_at)

    def test_str(self):
        """_summary_
        """        

    def test_todict(self):
        """_summary_
        """
        model_dict = self.base_model.to_dict()
        self.assertTrue(type(model_dict), dict)
        for key in model_dict:
            # check if the keys contain strings
            self.assertTrue(type(key), str)
            self.assertNotEqual(key, None)

if __name__ == '__main__':
    unittest.main()
