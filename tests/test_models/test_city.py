#!/usr/bin/python3
""" Unit tests City class """
from models.city import City
from models.state import State
import unittest
from datetime import datetime


class TestCity(unittest.TestCase):
    """ Unit tests City class """

    def setUp(self):
        """ Initialization """
        self.city_1 = City()
        self.city_1.name = "San Francisco"
        self.state = State()
        self.state.name = "California"
        self.city_1.state_id = self.state.id

    def test_attr_base(self):
        """ Test attribut BaseModel """
        self.assertIsNotNone(self.city_1.id)
        self.assertIsNotNone(self.city_1.created_at)
        self.assertIsNotNone(self.city_1.updated_at)
        self.assertIsNotNone(self.city_1.name)
        self.assertIsNotNone(self.city_1.state_id)

    def test_type_attr_base(self):
        """ Test type attribut BaseModel """
        self.assertEqual(type(self.city_1.id), str)
        self.assertEqual(type(self.city_1.created_at), datetime)
        self.assertEqual(type(self.city_1.updated_at), datetime)

    def test_attr(self):
        """ Test attribut City class """
        self.assertEqual(self.city_1.name, "San Francisco")
        self.assertEqual(self.city_1.state_id, self.state.id)

    def test_type_args(self):
        """ Test type attribut City """
        self.assertEqual(type(self.city_1.name), str)
        self.assertEqual(type(self.city_1.state_id), str)
