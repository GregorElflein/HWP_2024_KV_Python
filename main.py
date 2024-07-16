#raw_kv = "3,0,1,1,1,1,0,*,*"
#raw_kv = "4,0,*,0,*,0,*,0,*,1,*,1,*,1,*,0,*"
raw_kv = "5,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1"


def xor_c(a, b):
    return '0' if (a == b) else '1'


def flip(c):
    return '1' if (c == '0') else '0'


def binary_to_gray(binary):
    gray = binary[0]
    for i in range(1, len(binary)):
        gray += xor_c(binary[i - 1], binary[i])
    return gray


# TODO why do we need this?
def gray_to_binary(gray):
    binary = gray[0]
    for i in range(1, len(gray)):
        if gray[i] == '0':
            binary += binary[i - 1]
        else:
            binary += flip(binary[i - 1])
    return binary


def binary_to_int(binary):
    return int(binary, 2)


def int_to_binary(integer, length):
    return format(integer, '0' + str(length) + 'b')


# TODO
def opal_to_gray(opal):
    gray = []
    return gray


# TODO why do we need this?
def gray_to_int(gray):
    return binary_to_int(gray_to_binary(gray))


# converts raw KV input into table form
def get_kv(raw_input):
    raw_operators = int(raw_input.split(',')[0])
    operators = [raw_operators // 2 + raw_operators % 2, raw_operators // 2]    # Operators x and Operators y
    table_content = raw_input.split(',', 1)[1].split(',')
    table_validation(table_content)
    gray_op = get_graycode(operators)

    table = []
    for elements2 in gray_op[1]:
        helper = []
        for elements in gray_op[0]:
            value = table_content[binary_to_int(elements2 + elements)]
            helper.append(value)
        table.append(helper)

    gray_op[0].insert(0, 'XX')
    return gray_op, table     # returns horizontal operators, vertical operators, table contents


# validates if the input given for the KV is correct
def table_validation(table):
    for elements in table:
        if elements != "1" and elements != "0" and elements != "*":
            print('invalid input with: ' + elements)
            exit()


# takes count of operators and returns specific combinations [[[x], [x], ..], [[y], [y], ...]]
def get_graycode(op_counts):
    operators = [[], []]
    for elements in range(2**op_counts[0]):
        operators[0].append(binary_to_gray((int_to_binary(elements, op_counts[0]))))
    for elements in range(2**op_counts[1]):
        operators[1].append(binary_to_gray(int_to_binary(elements, op_counts[1])))

    print(operators)
    return operators


# prints table as pretty table
def print_kv(kv):
    print(kv)
    row = kv[0][0]
    for cell in row:
        print('| {0:^{width}}'.format(cell, width=4 * (len(kv[0][0][0])-1)), end='')
    print("|")

    for rows in range(len(kv[1])):
        row = kv[1][rows]
        row.insert(0, kv[0][1][rows])
        for cell in row:
            print('| {0:^{width}}'.format(cell, width=4 * (len(kv[0][0][0])-1)), end='')
        print("|")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_kv(get_kv(raw_kv))
