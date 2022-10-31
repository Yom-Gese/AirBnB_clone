#!/usr/bin/python3
"""File storage module"""
import dateutil.parser
import json
import os
from models import *


class FileStorage:
    """Serializes instances to a JSON file\
        and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}		# Store all objects as dictionary

    def __init__(self):
        pass

    def all(self):
        """Returns the dictionary '__objects'"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects (dictionary) the obj with key\
            <obj class name>.id
        """
        FileStorage.__objects[str(type(obj).__name__) + '.' +
                              str(obj.id)] = obj

    def save(self):
        """Serializes __objects to JSON file (path: __file_path"""

        # test values
        # print("\n====> This is the dict\n"); print(FileStorage.__objects)
        # print("\n======>\n")

        store = {}
        # for key in FileStorage.__objects.keys():
        #     if type(FileStorage.__objects[key]) is not dict:
        #         store[key] = FileStorage.__objects[key].to_dict()
        #     else:
        #         store[key] = FileStorage.__objects[key]

        for key, value in FileStorage.__objects.items():
            if type(value) is not dict:
                store[key] = value.to_dict()
            else:
                for val_key in value:
                    if val_key in ['updated_at', 'created_at']:
                        value.update({
                            val_key: str(value[val_key])
                        })
                store[key] = value

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(store))

    def reload(self):
        """Deserializes the JSON file to __objects \
            only if JSON file exists; do nothing otherwise"""

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:

                FileStorage.__objects = {}
                obj_ref = FileStorage.__objects
                temp = json.load(file)
                # test -> what is in temp?
                # print("\n=====> Temp"); print(temp); print("======>\n")

                # print(temp.keys()); print()
                for key, value in temp.items():
                    if type(value) is dict:
                        for val_key in value.copy():
                            if val_key in ['updated_at', 'created_at']:
                                value.update({
                                    val_key: dateutil.parser.isoparse(
                                        value[val_key]
                                    )
                                })
                            if val_key == '__class__':
                                del value[val_key]
                    obj_ref.update({key: temp[key]})
