raw_kv = "5,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1"


# converts raw KV input into table form
def get_kv(raw_input):
    raw_operators = int(raw_input.split(',')[0])
    operators = [raw_operators // 2 + raw_operators % 2, raw_operators // 2]    # Operators x and Operators y
    table_content = raw_input.split(',', 1)[1].split(',')
    table_validation(table_content)

    table = []
    for columns in range(2 ** operators[1]):   # y
        row = []
        for rows in range(2 ** operators[0]):  # x
            row.append(table_content[columns * 2 ** operators[0] + rows])
        table.append(row)
    return get_operators(operators), table     # returns horizontal operators, vertical operators, table contents


# validates if the input given for the KV is correct
def table_validation(table):
    for elements in table:
        if elements != "1" and elements != "0" and elements != "*":
            print('invalid input with: ' + elements)
            exit()


# takes count of operators and returns specific combinations [[[x], [x], ..], [[y], [y], ...]]
def get_operators(operators):
    letters = [[], []]
    for x_operators in range(operators[0]):
        letters[0].append([chr(97 + x_operators), "not(" + chr(97 + x_operators) + ")"])     # x are small letters
    for y_operators in range(operators[1]):
        letters[1].append([chr(65 + y_operators), "not(" + chr(65 + y_operators) + ")"])     # y are large letters
    letters[0] = combine_letters(letters[0])
    letters[1] = combine_letters(letters[1])
    return letters


# TODO maybe fix how the letter-combinations are sorted (make grey code)
# combine different letters
def combine_letters(letter_list):

    while len(letter_list) > 1:
        letter_list[0].append(letter_list[0][1]), letter_list[0].append(letter_list[0][0])
        for elements_x0 in range(len(letter_list[0]) // 2):
            letter_list[0][elements_x0 * 2] = letter_list[0][elements_x0 * 2] + " " + letter_list[1][0]
            letter_list[0][elements_x0 * 2 + 1] = letter_list[0][elements_x0 * 2 + 1] + " " + letter_list[1][1]
        letter_list.pop(1)
    print(letter_list[0])
    return letter_list[0]


# prints table as pretty table
def print_kv(kv):
    
    row = kv[0][0]
    for cell in row:
        print('| {0:^{width}}'.format(cell, width=7 * (len(kv[0][0][0]) - 2)), end='')
    print("| \n")
    
    for rows in range(len(kv[1])):
        row = kv[1][rows]
        row.insert(0, kv[0][1][rows])
        for cell in row:
            print('| {0:^{width}}'.format(cell, width=7 * (len(kv[0][0][0]) - 2)), end='')
        print("| \n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_kv(get_kv(raw_kv))
