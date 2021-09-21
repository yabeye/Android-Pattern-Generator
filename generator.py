class Generator:
    MATRIX_ORDER = 3

    def __init__(self) -> None:
        self.sub_total = 0
        self.count_combination = 0
        self.file = open('all_patterns.txt', 'w')

    def generate_all_combs(self, current_pattern):
        # patterns could not exceed length above 10
        # so, it will be our base case to terminate the recursion(DFS)
        if len(current_pattern) == 10:
            return

        if 4 <= len(current_pattern) <= 9:
            # because min = 4 and max = 9 node must be touched
            self.sub_total += 1
            self.count_combination += 1
            self.file.writelines(f'{current_pattern} \n')

        # check next node validity(reachability) and continue searching in the tree(pattern)
        for i in range(9):
            len_pattern = len(current_pattern)

            # not necessary just to inform the user
            if len_pattern == 0:
                # len at 0 because it is the starting stage
                print(f'Starting from " NODE {i} ", Calculating ...')
            # end not necessary

            if i in current_pattern:
                continue
            if len_pattern == 0:
                pass
            elif not self.is_reachable(current_pattern, current_pattern[len(current_pattern) - 1], i):
                continue

            current_pattern.append(i)
            self.generate_all_combs(current_pattern)
            current_pattern.pop()

            # not necessary just to inform the user
            if len_pattern == 0:
                print(f'Calculation ended for start " NODE {i} ", sub-total= {self.sub_total} \n')
                self.sub_total = 0
            # end not necessary

        return

    def is_reachable(self, pattern, point1, point2) -> bool:

        # this method will require two points
        # point1 = the last node touched in the pattern
        # point2 = the current node that we are checking the reachability from point1
        # and return True if it is possible to reach from point1 to point2 else False

        row1 = int(point1 / self.MATRIX_ORDER)
        row2 = int(point2 / self.MATRIX_ORDER)
        row_diff = abs(row1 - row2)
        if row_diff == 1:
            return True

        col1 = int(point1 % self.MATRIX_ORDER)
        col2 = int(point2 % self.MATRIX_ORDER)
        col_diff = abs(col1 - col2)
        if col_diff == 1:
            return True

        # Note: It is possible to reach from point1 to point2 even if
        # there is a middle node between If it is already touched
        if row_diff == 0 or col_diff == 0 or row_diff == col_diff:
            mid_point = int((point1 + point2) / 2)
            if mid_point not in pattern:
                return False

        return True

# end of the class Generate
