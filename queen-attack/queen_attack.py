class Queen(object):
    def __init__(self, row, column):
        if row>=8 or row<=-1 or column>=8 or column<=-1:
            raise ValueError(".+")
        self.row=row
        self.column=column

    def can_attack(self, another_queen):
        if self.row==another_queen.row and self.column==another_queen.column:
            raise ValueError(".+")
        if self.row==another_queen.row or self.column==another_queen.column:
            return True
        row_diff=abs(self.row-another_queen.row)
        column_diff=abs(self.column-another_queen.column)
        if row_diff==column_diff:
            return True
        return False