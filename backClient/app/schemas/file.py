from enum import Enum


class FileType(str, Enum):
    csv = "csv"
    json = "json"
    excel = "excel"