import pandas as pd
import json
from typing import Protocol

class Converter:

    @classmethod
    def save_and_get_file_path(cls, data: dict, type: str, path: str):
        converter: TypeFile = cls._get_file_converter(type)
        converter.write_and_save_file(data, path)

    def _get_file_converter(type: str):
        types = {
            'csv': Csv,
            'json': Json,
            'xlsx': Excel
        }
        class_type: TypeFile = types.get(type, None)

        if class_type:
            return class_type
        raise ValueError(format)



class TypeFile(Protocol):
    @classmethod
    def write_and_save_file(cls, data: dict, path: str):
        pass 

class Excel:
    @classmethod
    def write_and_save_file(cls, data: dict, path: str):
        df = pd.DataFrame(data) 
        df.to_excel(path, index=False) 

class Json:
    @classmethod
    def write_and_save_file(cls, data: dict, path: str):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

class Csv:
    @classmethod
    def write_and_save_file(cls, data: dict, path: str):
        df = pd.DataFrame(data)
        df.to_csv(path, encoding='utf-8', index=False)
