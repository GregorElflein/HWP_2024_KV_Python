raw_kgv = "5,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1"


def print_hi(name):
    print(f'Hi, {name}')


def get_kv(raw_input):
    raw_operators = int(raw_input.split(',')[0])
    operators = [raw_operators // 2 + raw_operators % 2, raw_operators // 2]    # Operators x and Operators y
    table_content = raw_input.split(',', 1)[1].split(',')

    table = []
    for elements in range(2 ** operators[1]):   # y
        row = []
        for elements2 in range(2 ** operators[0]):  # x
            row.append(table_content[elements * 2 ** operators[0] + elements2])
        table.append(row)

    return operators, table     # returns horizontal operators, vertical operators, table contents


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_kv(raw_kgv))
    print_hi('Dev')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
