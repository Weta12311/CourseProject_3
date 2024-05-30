import utils


def main():
    sorted_operations = utils.sort_by_data()
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

main()

