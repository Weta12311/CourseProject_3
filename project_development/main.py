
import project_development.utils as utils


def main(path_to_json):
    list_operations = utils.load_operations(path_to_json)
    five_operations = utils.five_operations(list_operations)
    sorted_operations = utils.sort_by_data(five_operations)
    for operations in sorted_operations:
        if operations.get('from') is not None:
            masked_number_from = utils.masc_and_split(operations['from'])
            masked_number_to = utils.masc_and_split(operations['to'])
            print(f"{operations['date']} {operations['description']}\n"
                  f"{masked_number_from} -> {masked_number_to}\n"
                  f"{operations['operationAmount']['amount']} {operations['operationAmount']['currency']['name']}\n"
                  )
        else:
            print(f"{operations['date']} {operations['description']}\n"
                  f"**** -> {masked_number_to}\n"
                  f"{operations['operationAmount']['amount']} {operations['operationAmount']['currency']['name']}\n"
                  )


main('..//operations.json')
#main("..//tests//test.json")

