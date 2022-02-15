from typing import List, Union

class Matrix:
    __mat:List[List[str]]
    __string:str 

    def __init__(self, element: str,
                 row: int, col: int, matrix_type: str = 'bmatrix') -> None:
        
        if not matrix_type in ['pmatrix', 'bmatrix', 'vmatrix', 'Bmatrix', 'Vmatrix']:
            raise ValueError('matrix_type must be a valid LaTeX qualifier.')

        self.__mat = [[f"{element}_{{{i},{j}}}" for i in range(1, col+1)]
                                                for j in range(1, row+1)]

        self.__string = ' \\\\ \n'.join(f"\t {' & '.join(i)}" for i in self.__mat)
        
        self.__type:str = matrix_type

    def __str__(self) -> str: 
        return f"\\begin{{{self.__type}}} \n{self.__string} \n\\end{{{self.__type}}}"

    def __repr__(self) -> str: 
        return self.__str__()

class ConcreteMatrix:
    __mat: List[List[str]]
    __string: str

    def __init__(self, element: List[List[str]],
                 row: int, col: int, matrix_type: str = 'bmatrix') -> None:

        if not matrix_type in ['pmatrix', 'bmatrix', 'vmatrix', 'Bmatrix', 'Vmatrix']:
            raise ValueError('matrix_type must be a valid LaTeX qualifier.')

        if not all(len(i) == row for i in element): 
            raise ValueError(f'size of list of element must be equal to row: {row}')
        
        if len(element) != col:
            raise ValueError(f'size of list of element must be equal to m: {col}')

        self.__mat = [[j for j in i] for i in element]

        self.__string = ' \\\\ \n'.join(
            f"\t {' & '.join(i)}" for i in self.__mat)

        self.__type: str = matrix_type

    def __str__(self) -> str:
        return f"\\begin{{{self.__type}}} \n{self.__string} \n\\end{{{self.__type}}}"

    def __repr__(self) -> str:
        return self.__str__()


def matrix_factory(entry: List[List[Union[float, int]]], 
                    row:int, col:int, matrix_type:str = 'bmatrix') -> ConcreteMatrix:
    return ConcreteMatrix([[str(i) for i in j] for j in entry], row, col, matrix_type)


def equation() -> str: ...

if __name__ == '__main__':
    A = Matrix('A',5,5, 'pmatrix')
    B = matrix_factory([[1,2,3],[4,5,6],[7,8,9]],3,3)

    print(A)
    print(B)
