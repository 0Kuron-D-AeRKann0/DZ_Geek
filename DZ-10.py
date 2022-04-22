#Задание 1

""" Matrix """
__data: dict


def __init__(self, *elems, rows=1) -> None:
    # test split elems

    self.__data = {}

    if len(elems) % rows != 0:
        raise ValueError("Can't split len(elems) / rows")

    columns = len(elems) // rows

    if len(elems) > 0:
        self.__data["size"] = (rows, columns)

    for column in range(rows):
        for row in range(columns):
            self.__data[(row, column)] = elems[column + row * rows]


def get_size(self) -> tuple:
    """ return size of matrix (rows, columns) """
    return self.__data.get("size", (0, 0))


def get_elem(self, row_index, column_index):
    """ return elems of pos(row, column) """

    value = self.__data[(row_index, column_index)]

    if value is not None:
        return value

    raise ValueError(f"Unknow index {(row_index, column_index)}")


def __arifm_func(self, func, other: 'Matrix') -> list:
    (rows, columns) = self.get_size()

    return [func(self.get_elem(x, y), other.get_elem(x, y))
            for y in range(rows) for x in range(columns)]


def __add__(self, other: 'Matrix') -> 'Matrix':
    """ operator + for matrix. return a new matrix """
    if self.get_size() != other.get_size():
        raise ValueError("Matrix's sizies must be eq")

    return Matrix(self.__arifm_func(lambda x, y: x + y, other), rows=self.get_size()[0])


def __sub__(self, other: 'Matrix') -> 'Matrix':
    """ operator - for matrix. return a new matrix """

    if self.get_size() != other.get_size():
        raise ValueError("Matrix's sizies must be eq")

    return Matrix(self.__arifm_func(lambda x, y: x - y, other), rows=self.get_size()[0])


def __str__(self) -> str:
    (rows, columns) = self.get_size()

    if rows * columns == 0:
        return "Empty Matrix"

    output = ""
    for j, row in enumerate(range(rows)):

        for i, column in enumerate(range(columns)):
            output += f"{self.get_elem(column, row)}"

            if i != columns - 1:
                output += " "

        if j != rows - 1:
            output += "\n"

    return output

#Задание 2

from enum import Enum
from abc import ABC, abstractmethod


class ClothType(Enum):
    """ type of Cloth """
    COAT = 0
    COSTUME = 1


class ACloth(ABC):
    """ Abstract class """
    __name: str
    __type: 'ClothType'

    def __init__(self, name: str, cloth_type: 'ClothType') -> None:
        self.__name = name
        self.__type = cloth_type

    @abstractmethod
    def calc_cloth(self) -> float:
        """ calc how mutch cloth need """


class Coat(ACloth):
    __size: float

    def __init__(self, name: str, size: float) -> None:
        super().__init__(name, ClothType.COAT)
        self.__size = size

    def calc_cloth(self) -> float:
        return self.__size / 6.5 + 0.5


class Costume(ACloth):
    __height: float

    def __init__(self, name: str, height) -> None:
        super().__init__(name, ClothType.COSTUME)
        self.__height = height

    def calc_cloth(self) -> float:
        return 2 * self.__height + 0.3

# Задание 3

class Cell:
    __cells: int

    def __init__(self, cells: int) -> None:
        self.__cells = cells

    def __add__(self, other: 'Cell'):
        return Cell(self._get_size() + other._get_size())

    def __sub__(self, other: 'Cell'):
        if self._get_size() < other._get_size():
            raise ValueError("cells can't be < 0")

        return Cell(self._get_size() - other._get_size())

    def __mul__(self, other: 'Cell'):
        return Cell(self._get_size() * other._get_size())

    def __floordiv__(self, other: 'Cell'):
        return Cell(self._get_size() // other._get_size())

    def _get_cells(self) -> str:
        return str(self).replace("Cell(", "").replace(")", "")

    def _get_size(self) -> int:
        return self._get_cells().count("*")

    def __str__(self) -> str:
        return f"Cell({'*'*self.__cells})"

    def make_order(self, split_cell) -> str:
        """ ordering cells to cube the size eq split_cell*split_cell """

        if split_cell == 0:
            raise ValueError("can't split cells by 0")

        if split_cell >= self._get_size():
            return self._get_cells()

        size = self._get_size()

        return "".join([f"{x}\n" if i % split_cell == 0 and i != size  else x
                        for i, x in enumerate(self._get_cells(), start=1)])