from project_development.utils import load_operations, five_operations, sort_by_data, masc_and_split
from project_development.main import main


def test_load_operations():
    assert load_operations('test.json') == [{},
      {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
          "amount": "31957.58",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
      }
    ]


def test_five_operations():
    assert five_operations([
        {
          "id": 441945886,
          "state": "EXECUTED",
          "date": "2019-08-26T10:50:58.294041",
          "operationAmount": {
            "amount": "31957.58",
            "currency": {
              "name": "руб.",
              "code": "RUB"
            }
          },
          "description": "Перевод организации",
          "from": "Maestro 1596837868705199",
          "to": "Счет 64686473678894779589"
        }
      ]) == [
        {
          "id": 441945886,
          "state": "EXECUTED",
          "date": "2019-08-26T10:50:58.294041",
          "operationAmount": {
            "amount": "31957.58",
            "currency": {
              "name": "руб.",
              "code": "RUB"
            }
          },
          "description": "Перевод организации",
          "from": "Maestro 1596837868705199",
          "to": "Счет 64686473678894779589"
        }
      ]


def test_sort_by_data():
    date_list = [{}, {"date": "2019-08-26T10:50:58.294041"}]
    assert sort_by_data(date_list) == [{"date": "26.08.2019"}]


def test_mask_and_spit():
    assert masc_and_split('Maestro 1596837868705199') == 'Maestro  1596 83** **** 5199'
    assert masc_and_split('Счет 64686473678894779589') == 'Счет **9589'


# def test_main():
#     assert main('test.json') == '26.08.2019 Перевод организации\nMaestro  1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n'


