from operator import itemgetter
import datetime
import json as js
import os
def load_operations():
    """
     Фунция получает список операций из operations.json
    """
    path_operations = os.path.abspath('..//operations.json')
    with open(path_operations, 'r', encoding='utf-8') as file:
        list_operations = js.loads(file.read())
        print(list_operations)
        return (list_operations)


load_operations()