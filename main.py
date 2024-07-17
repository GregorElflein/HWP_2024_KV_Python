import math

raw_kv = "5#00000111000001110000011100000111"


class Block:
    def __init__(self, x1, y1, x2, y2, width, height):
        self.block = [x1, y1, x2, y2]
        self.width = width
        self.height = height

    def __str__(self):
        return str(self.block)

    def get_block(self, index):
        return self.block[index]

    def check_neighbour(self, block):
        decision = False
        if block == self:
            pass
        elif (self.get_block(0) == block[0] and self.get_block(2) == block[2]
              and self.get_block(3) == (block[1] - 1) % self.height):
            decision = True
        elif (self.get_block(1) == block[1] and self.get_block(3) == block[3]
              and self.get_block(2) == (block[0] - 1) % self.width):
            decision = True
        return decision

    def combine_block(self, block):
        return Block(self.get_block(0), self.get_block(1), block[2], block[3], self.width, self.height)


# XOR function
def xor_c(a, b):
    return '0' if (a == b) else '1'


# flip Bit function
def flip(c):
    return '1' if (c == '0') else '0'


# convert Binary input via XOR to Gray code
def binary_to_gray(binary):
    gray = binary[0]
    for i in range(1, len(binary)):
        gray += xor_c(binary[i - 1], binary[i])
    return gray


# convert Integer to Binary
def int_to_binary(integer, length):
    return format(integer, '0' + str(length) + 'b')


# converts raw KV input into table form
def get_kv(raw_input):
    raw_operators = int(raw_input.split('#')[0])
    operators = [raw_operators // 2 + raw_operators % 2, raw_operators // 2]  # Operators x and Operators y
    table_content = [*raw_input.split('#', 1)[1]]
    table_validation(table_content)
    gray_op = get_graycode(operators)

    table = []
    for elements2 in gray_op[1]:
        helper = []
        for elements in gray_op[0]:
            value = table_content[int(elements2 + elements, 2)]
            helper.append(value)
        table.append(helper)

    gray_op[0].insert(0, 'XX')
    return gray_op, table  # returns horizontal operators, vertical operators, table contents


# validates if the input given for the KV is correct
def table_validation(table):
    for elements in table:
        if elements != '1' and elements != '0' and elements != '0':
            print('invalid input with: ' + elements)
            exit()


# takes count of operators and returns specific combinations [[[x], [x], ..], [[y], [y], ...]]
def get_graycode(op_counts):
    operators = [[], []]
    for elements in range(2 ** op_counts[0]):
        operators[0].append(binary_to_gray((int_to_binary(elements, op_counts[0]))))
    for elements in range(2 ** op_counts[1]):
        operators[1].append(binary_to_gray(int_to_binary(elements, op_counts[1])))
    return operators


# prints table as pretty table
def print_kv(kv):
    row = kv[0][0]
    for cell in row:
        print('| {0:^{width}}'.format(cell, width=4 * (len(kv[0][0][0]) - 1)), end='')  # TODO fix width scaling
    print("|")

    for rows in range(len(kv[1])):
        row = kv[1][rows]
        row.insert(0, kv[0][1][rows])
        for cell in row:
            print('| {0:^{width}}'.format(cell, width=4 * (len(kv[0][0][0]) - 1)), end='')
        print("|")


def get_small_blocks(kv, width, height, clause_type):
    block_list = []
    for rows in range(height):
        for cells in range(len(kv[rows])):
            if kv[rows][cells] == clause_type or kv[rows][cells] == '*':
                print(Block(cells, rows, cells, rows, width, height))
                block_list.append(Block(cells, rows, cells, rows, width, height))
    return block_list


def get_block_list(block_list, block_size, width, height):
    pass
    # TODO
    # check neighbour
    # combine block
    # return das


def get_blox(kv, clause_type):
    for block_sizes in range(2, (math.floor(math.log2(len(kv) * len(kv[0])))) + 1):
        pass
        # TODO add for block sizes 2+
        get_block_list(get_small_blocks(kv, len(kv[0]), len(kv), clause_type), 2 ** block_sizes, len(kv[0]), len(kv))
    print(kv)


def get_clause(kv):
    # TODO fix this
    clause_type = '1'
    get_blox(kv, clause_type)
    # clause_type = '0'
    # get_blox(kv, clause_type)
    clause = []
    return clause


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_kv(get_kv(raw_kv))
    get_clause(get_kv(raw_kv)[1])
    print
