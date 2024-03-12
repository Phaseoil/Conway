"""file containing the ConwaysGameOfLife class.
"""
from time import sleep
from os import system
from copy import deepcopy
from cell import Cell


class ConwaysGameOfLife:
    """Conways Game of life.
    """
    _field = []

    def __init__(self, width=10, height=5):
        self._field = [[Cell(False) for j in range(width)] for i in range(height)]

    def print_field(self):
        """prints the field for conways game of live.

        Args:
            l (list): two-dimensional list of cells.
        """
        for line in self._field:
            print("".join([str(line[i]) for i in range(len(line))]))

    def next_generation(self):
        new_field = deepcopy(self._field)
        for i, line in enumerate(self._field):
            for j, cell in enumerate(line):
                neighbors = self.get_neighbors(j, i)
                if cell.is_alive:
                    if self.rules_alive(cell, neighbors):
                        new_field[i][j].death()
                else:
                    if self.rules_dead(cell, neighbors):
                        new_field[i][j].ressurect()
        self._field = new_field

    def rules_alive(self, cell, neighbors):
        if not cell.is_alive:
            raise ValueError
        count = 0
        for i in range(len(neighbors)):
            if neighbors[i].is_alive:
                count += 1
        if count > 3 or count < 2:
            return True
        return False

    def rules_dead(self, cell, neighbors):
        if cell.is_alive:
            raise ValueError
        count = 0
        for i in range(len(neighbors)):
            if neighbors[i].is_alive:
                count += 1
        if count == 3:
            return True
        return False

    def run(self):
        system('cls')
        while True:
            self.print_field()
            self.next_generation()
            sleep(2)
            system('cls')

    def set_cell(self, x, y):
        self._field[y][x].ressurect()

    def get_neighbors(self, x, y):
        l = []
        if x > 0:
            l.append(self._field[y][x - 1])

        if y > 0:
            l.append(self._field[y - 1][x])

        if x > 0 and y > 0:
            l.append(self._field[y - 1][x - 1])

        if x < len(self._field[0]) - 1:
            l.append(self._field[y][x + 1])

        if y < len(self._field) - 1:
            l.append(self._field[y + 1][x])

        if x < len(self._field[0]) - 1 and y < len(self._field) - 1:
            l.append(self._field[y + 1][x + 1])

        if x > 0 and y < len(self._field) - 1:
            l.append(self._field[y + 1][x - 1])

        if x < len(self._field[0]) - 1 and y > 0:
            l.append(self._field[y - 1][x + 1])

        return l

    def get_neighbors_coordinates(self, x, y):
        l = []
        if x > 0:
            l.append((y, x - 1))

        if y > 0:
            l.append((y - 1, x))

        if x > 0 and y > 0:
            l.append((y - 1, x - 1))

        if x < len(self._field[0]) - 1:
            l.append((y, x + 1))

        if y < len(self._field) - 1:
            l.append((y + 1, x))

        if x < len(self._field[0]) - 1 and y < len(self._field) - 1:
            l.append((y + 1, x + 1))

        if x > 0 and y < len(self._field) - 1:
            l.append((y + 1, x - 1))

        if x < len(self._field[0]) - 1 and y > 0:
            l.append((y - 1, x + 1))

        return l

    def get_neighbors_as_string_list(self, x, y):
        l = []
        if x > 0:
            l.append(str(self._field[y][x - 1]))

        if y > 0:
            l.append(str(self._field[y - 1][x]))

        if x > 0 and y > 0:
            l.append(str(self._field[y - 1][x - 1]))

        if x < len(self._field[0]) - 1:
            l.append(str(self._field[y][x + 1]))

        if y < len(self._field) - 1:
            l.append(str(self._field[y + 1][x]))

        if x < len(self._field[0]) - 1 and y < len(self._field) - 1:
            l.append(str(self._field[y + 1][x + 1]))

        if x > 0 and y < len(self._field) - 1:
            l.append(str(self._field[y + 1][x - 1]))

        if x < len(self._field[0]) - 1 and y > 0:
            l.append(str(self._field[y - 1][x + 1]))

        return l
