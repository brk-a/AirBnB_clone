#!/usr/bin/python3

'''FileStorage mod'''

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''class FileStorage '''
    __file_path = 'file.json'
    __objects = {}


    def all(self):
        '''all method returns dict of objs'''
        return self.__objects

    def new(self, obj):
        '''new method adds obj to __objects dict'''
        if obj:
            key = f'{type(obj).__name__}.{obj.id}'
            self.__objects[key] = obj
    def save(self):
        '''save method serialises __objects to JSON file at __filepath'''
        obj_dict = {k:v.to_dict() for (k, v) in self.__objects.items()}
        json_str = json.dumps(obj_dict)

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        '''reload method deserialises JSON file to __objects'''
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval(f'{cls}({"**obj_dict"})'))
        except FileNotFoundError:
            pass
