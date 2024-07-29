import math

# raw_kv = "4#1010111000000000"
raw_kv = "4#0101000111111111"
# raw_kv = "5#00000111000001110000011100000111"


class Block:
    def __init__(self, x1, y1, x2, y2, width, height):
        self.block = [x1, y1, x2, y2]
        self.width = width
        self.height = height

    def __str__(self):
        return str(self.block)

    def get_block(self, index):
        return self.block[index]

    def get_all_vars(self):
        all_vars = []
        x1 = self.block[0]
        y1 = self.block[1]
        x2 = self.block[2]
        y2 = self.block[3]
        block_height = (y2 - y1) % self.height
        block_width = (x2 - x1) % self.width

        if x1 <= x2 and y1 <= y2:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    all_vars.append([x, y])
        elif x1 <= x2 and y1 > y2:
            for x in range(x1, x2 + 1):
                for y in range(y1, y1 + block_height + 1):
                    all_vars.append([x, y % self.height])
        elif x1 > x2 and y1 <= y2:
            for x in range(x1, x1 + block_width + 1):
                for y in range(y1, y2 + 1):
                    all_vars.append([x % self.width, y])
        return all_vars

    def equals(self, blocks):
        equal = False
        for block in blocks:
            if (self.block[0] == block.get_block(0) and self.block[1] == block.get_block(1)
                    and self.block[2] == block.get_block(2) and self.block[3] == block.get_block(3)):
                equal = True
        return equal

    def is_contained(self, block):
        contained = True
        for elements in self.get_all_vars():
            if elements not in block.get_all_vars():
                contained = False
        return contained

    def check_neighbour(self, block):
        decision = False
        if block == self:
            pass
        elif (self.block[0] == block.get_block(0) and self.block[2] == block.get_block(2)
              and self.block[3] == (block.get_block(1) - 1) % self.height):
            decision = True
        elif (self.block[1] == block.get_block(1) and self.block[3] == block.get_block(3)
              and self.block[2] == (block.get_block(0) - 1) % self.width):
            decision = True
        return decision

    def combine_block(self, block):
        return Block(self.block[0], self.block[1], block.get_block(2), block.get_block(3), self.width, self.height)

    def get_func(self, x, y):
        cords = [[], []]  # [[x], [y]]
        for elements in self.get_all_vars():
            if elements[0] not in cords[0]:
                cords[0].append(elements[0])
            if elements[1] not in cords[1]:
                cords[1].append(elements[1])

        max_number = [len(cords[0]), len(cords[1])]
        int_x, int_y = 0, 0

        for elements in cords[0]:
            int_x += int(x[elements])
        for elements in cords[1]:
            int_y += int(y[elements])

        str_x, str_y = (str(int_x).rjust(max_number[0] - len(str(int_x)) + 1, '0'),
                        str(int_y).rjust(max_number[1] - len(str(int_y)) + 1, '0'))
        # TODO if x-1 or 1-x block, fix, that part with 1 is accepted
        clause = []
        for chars in str_y:
            if chars == '0':
                clause.append('0')
            elif chars == str(max_number[1]):
                clause.append('1')
            else:
                clause.append('-')

        for chars in str_x:
            if chars == '0':
                clause.append('0')
            elif chars == str(max_number[0]):
                clause.append('1')
            else:
                clause.append('-')
        return clause

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
    return gray_op, table  # returns horizontal operators, vertical operators, table contents


# validates if the input given for the KV is correct
def table_validation(table):
    for elements in table:
        if elements != '1' and elements != '0' and elements != '*':
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
    kv[0][0].insert(0, 'XX')
    row = kv[0][0]

    print('\nKV-Table:')
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
            if kv[rows][cells] in clause_type:
                block_list.append(Block(cells, rows, cells, rows, width, height))
    return block_list


def get_block_list(block_list):
    next_block_list = []
    for block1 in block_list:
        for block2 in block_list:
            if block1.check_neighbour(block2):
                if not block1.combine_block(block2).equals(next_block_list):
                    next_block_list.append(block1.combine_block(block2))
    return next_block_list


def filter_blocks(block_list):
    reversed_block = []
    for elements in block_list:
        if elements:
            reversed_block.insert(0, elements)
    filtered_block_list = [reversed_block[0][0]]
    for elements in reversed_block:
        for block in elements:
            contained = False
            for filtered in filtered_block_list:
                if block.is_contained(filtered):
                    contained = True
            if not contained:
                filtered_block_list.append(block)
    return filtered_block_list


def get_blox(kv, clause_type):
    block_list = [get_small_blocks(kv, len(kv[0]), len(kv), clause_type)]
    for block_sizes in range(2, (math.floor(math.log2(len(kv) * len(kv[0])))) + 1):
        block_list.append(get_block_list(block_list[-1]))
    block_list = filter_blocks(block_list)
    return block_list


def get_clause(kv):
    clause_type = ['0', '*']
    block_list = get_blox(kv[1], clause_type)

    print('\nBlocks: ')
    for block in block_list:
        print(block, end=' ')

    # TODO calculate clause
    clause = []
    for block in block_list:
        clause.append(block.get_func(kv[0][0], kv[0][1]))

    print('\n\nClauses: ')
    print(clause)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_kv(get_kv(raw_kv))
    get_clause(get_kv(raw_kv))
