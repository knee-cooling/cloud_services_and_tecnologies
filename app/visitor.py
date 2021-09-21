from __future__ import annotations
from abc import ABC, abstractmethod


class Visitor(ABC):
    # Интерфейс Компонента объявляет метод accept,
    # который в качестве аргумента может получать любой объект,
    # реализующий интерфейс посетителя.

    @abstractmethod
    def visit_cpu(self, v: CPUs) -> str:
        pass

    @abstractmethod
    def visit_ram(self, v: RAMs) -> str:
        pass


class Calculator(Visitor):

    # Каждый Конкретный Компонент должен реализовать метод accept таким образом,
    # чтобы он вызывал метод посетителя, соответствующий классу компонента.

    def __init__(self, cost: int = 0):
        self.cost = cost

    def visit_cpu(self, v: CPUs):
        self.cost = self.cost + v.GetPrice()

    def visit_ram(self, v: RAMs):
        self.cost = self.cost + v.GetPrice()

    def GetCost(self) -> int:
        return self.cost


class Visitable(ABC):

    # Интерфейс помещаемого объекта

    @abstractmethod
    def accept(self, v: Visitor):
        pass


class CPUs(Visitable):

    def __init__(self, price: int):
        self.price = price

    def accept(self, v: Visitor):
        v.visit_cpu(self)

    def GetPrice(self):
        return self.price


class RAMs(Visitable):

    def __init__(self, price: int):
        self.price = price

    def accept(self, v: Visitor):
        v.visit_ram(self)

    def GetPrice(self):
        return self.price


# Покупка комплектующих для домашнего использования:
class TestVisitorHome:

    def __init__(self):
        self.shopping_list = [CPUs(12500), RAMs(5400)]
        self.calc = Calculator()

    def setProduct(self):
        for i in self.shopping_list:
            i.accept(self.calc)

    def GetCost(self) -> int:
        return self.calc.GetCost()


# Покупка комплектующих для коммерческого использования:
class TestVisitorCommercial:

    def __init__(self):
        self.shopping_list = [CPUs(15500), RAMs(7100)]
        self.calc = Calculator()

    def setProduct(self):
        for i in self.shopping_list:
            i.accept(self.calc)

    def GetCost(self) -> int:
        return self.calc.GetCost()


if __name__ == "__main__":

    home = TestVisitorHome()
    home.setProduct()
    print(f"Всего к оплате (для домашнего использования): {home.GetCost()}")

    comm = TestVisitorCommercial()
    comm.setProduct()
    print(f"Всего к оплате (для коммерческого использования): {comm.GetCost()}")
