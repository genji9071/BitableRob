from abc import abstractmethod
from typing import List


class FilterOperation:

    def __init__(self):
        self.operation_type = self.get_operation_type()

    @abstractmethod
    def get_operation_type(self):
        pass

    @abstractmethod
    def encode(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class FilterSymbol(FilterOperation):
    TYPE_SYMBOL = 'symbol'

    SYMBOL_EQUALS = '='
    SYMBOL_NOT_EQUALS = '!='
    SYMBOL_GREATER = '>'
    SYMBOL_LESS = '<'
    SYMBOL_GREATER_EQUAL = '>='
    SYMBOL_LESS_EQUAL = '<='
    SYMBOL_CONTAINS = 'contains'

    def get_operation_type(self):
        return FilterSymbol.TYPE_SYMBOL

    def __init__(self, symbol: str, target: List):
        super().__init__()
        self.symbol = symbol
        self.target = target

    def __str__(self):
        if self.symbol == FilterSymbol.SYMBOL_CONTAINS:
            return f'{self.target[0]}.contains({self.target[1]})'
        else:
            return f'{self.target[0]} {self.symbol} {self.target[1]}'


class FilterOperator(FilterOperation):
    TYPE_OPERATOR = 'operator'

    OPERATOR_AND = 'AND'
    OPERATOR_OR = 'OR'
    OPERATOR_NOT = 'NOT'

    def get_operation_type(self):
        return FilterOperator.TYPE_OPERATOR

    def __init__(self, operator, target):
        super().__init__()
        self.operator = operator
        self.target = target

    def __str__(self):
        return f'{self.operator}({",".join([ str(x) for x in self.target])})'


if __name__ == "__main__":
    operation = FilterOperator(FilterOperator.OPERATOR_AND,
                               [FilterSymbol(FilterSymbol.SYMBOL_CONTAINS, ["CurrentValue.[订单号]", '"004"']),
                                FilterSymbol(FilterSymbol.SYMBOL_EQUALS, ["CurrentValue.[订单日期]", "TODAY()"])])
    print(operation)
