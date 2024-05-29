from operator import itemgetter
from datetime import datetime
import json as js
import os


def load_operations():
    """
     Фунция получает список операций из operations.json
    """
    path_operations = os.path.abspath('..//operations.json')
    with open(path_operations, 'r', encoding='utf-8') as file:
        list_operations = js.loads(file.read())
        sorted_operations = sorted(list_operations, key=lambda x: x.get('date', '0'))
        five_operations = sorted_operations[:6]
        return (five_operations)


def sort_by_data():
    five_operations = load_operations()
    del five_operations[0]
    for operations in five_operations:
        operations['date'] = datetime.fromisoformat(operations['date']).strftime('%d.%m.%Y')
    print(five_operations)
    return five_operations

def masc_and_split(card):
    card_number = card.split()[-1]
    private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    print(" ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)]))


sort_by_data()
masc_and_split('Visa Classic 8906171742833215')
