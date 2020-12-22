"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма) . Это могут быть обычные числа:
V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property .
"""
from abc import ABC


class Clothes(ABC):  # Одежда
    order_number = 1

    def __init__(self, name):
        self.name = name
        self.order_number = Clothes.order_number
        Clothes.order_number += 1

    @property
    def get_material(self):
        return self._material_consumption


class Coat(Clothes):  # Пальто, размер V = size
    summary_material = 0.0

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
        self._material_consumption = round(self.size / 6.5 + 0.5, 2)
        Coat.summary_material += self._material_consumption

    def __str__(self):
        return f'Заказ {self.order_number} - [{self.name}], размер {self.size}, ' + \
               f'расход мат-ла {self.get_material}.'


class Suit(Clothes):  # Костюм, рост H = height
    summary_material = 0.0

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
        self._material_consumption = round(2 * self.height + 0.3, 2)
        Suit.summary_material += self._material_consumption

    def __str__(self):
        return f'Заказ {self.order_number} - [ {self.name} ], рост {self.height}, ' + \
               f'расход мат-ла {self.get_material}.'


d = [
    Coat('Пальто1', size=10),
    Coat('Пальто2', size=20),
    Coat('Пальто3', size=30),
    Suit('Костюм1', height=160),
    Suit('Костюм2', height=180)
]

for i in d:
    print(i)

print('---')
print(f'Итого материала: ПАЛЬТО - {Coat.summary_material}, КОСТЮМЫ - {Suit.summary_material}')
