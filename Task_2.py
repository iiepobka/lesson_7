# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда , которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм . У этих типов одежды существуют
# параметры: размер (для пальто ) и рост (для костюма ). Это могут быть обычные числа: V и
# H , соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.
from abc import ABC
from abc import abstractmethod


class Clothes(ABC):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    @abstractmethod
    def consumption_coat(self):
        pass

    @abstractmethod
    def consumption_suit(self):
        pass


class Consumption(Clothes):
    @property
    def consumption_coat(self):
        if self.name == 'польто':
            return f'Расход ткани на изготовления пальто {self.number} размера: {round((self.number / 6.5) + 0.5, 2)}'

    @property
    def consumption_suit(self):
        if self.name == 'костюм':
            return f'Расход ткани на изготовления костюма на рост {self.number} м: {round((self.number * 2) + 0.3, 2)}'

    def __add__(self, other):
        return f'Рассход ткани на изготовление пальто {self.number} размера и костюма на рост \
{other.number} м: {round(((self.number / 6.5) + 0.5) + ((other.number * 2) + 0.3), 2)}'


coat = Consumption('польто', 48)
suit = Consumption('костюм', 1.75)
print(coat.consumption_coat)
print(suit.consumption_suit)
print(coat + suit)
