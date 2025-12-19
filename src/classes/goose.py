from typing import Literal
import random

class Goose:
    _id = 1

    def __init__(self, name: str, hp: int, type: Literal['Воюющий', 'Лечащий', 'Крикливый']):
        """
        Инициализация базового гуся.
        :param name: имя гуся
        :param hp: количество здоровья гуся
        :param type: тип гуся
        """
        self.name = name
        self.hp = hp
        self.type = type

        self.ingameid = Goose._id
        Goose._id += 1

    def repr(self) -> str:
        """
        Возвращает краткое строковое представление гуся.
        Используется в логах и сообщениях.
        :return: строка с идентификатором и именем гуся
        """
        return f'№{self.ingameid} {self.name}'

    def attack(self) -> float:
        """
        Выполняет стандартную атаку гуся.
        Возвращает множитель урона.
        :return: коэффициент атаки
        """
        money_stolen = random.choice([0.7, 0.8, 1.1, 1.2])
        return money_stolen

class WarGoose(Goose):
    def __init__(self, name: str, power: int):
        """
        Создаёт воюющего гуся.
        :param name: имя гуся
        :param power: сила атаки гуся
        """
        super().__init__(name, 2000, "Воюющий")
        self.power = power

    def __str__(self) -> str:
        """
        Строковое представление воюющего гуся.
        :return: строка с информацией о гусе
        """
        return f'{self.type} гусь {self.name} №{self.ingameid} со здоровьем {self.hp} и силой атаки {self.power}'

    def hard_attack(self) -> int:
        """
        Выполняет усиленную атаку воюющего гуся.
        :return: количество украденных денег
        """
        money_stolen_hard = self.power*7
        return money_stolen_hard

class HealerGoose(Goose):
    def __init__(self, name: str, power: int):
        """
        Создаёт лечащего гуся.
        :param name: имя гуся
        :param power: сила лечения гуся
        """
        super().__init__(name, 1500,"Лечащий")
        self.power = power

    def __str__(self) -> str:
        """
        Строковое представление гуся-доктора.
        :return: строка с информацией о гусе
        """
        return f'{self.type} гусь {self.name} №{self.ingameid} со здоровьем {self.hp} и силой лечения {self.power}'

    def heal(self) -> int:
        """
        Выполняет лечение другого гуся.
        :return: количество восстановленного здоровья
        """
        healed_hp = self.power
        return healed_hp

class HonkGoose(Goose):
    def __init__(self, name: str, power: int):
        """
        Создаёт крикливого гуся.
        :param name: имя гуся
        :param power: сила массового воздействия на разумы (РенТВ?)
        """
        super().__init__(name, 1000,"Крикливый")
        self.power = power

    def __str__(self) -> str:
        """
        Строковое представление крикливого гуся.
        :return: строка с информацией о гусе
        """
        return f'{self.type} гусь {self.name} №{self.ingameid} со здоровьем {self.hp} и массовой атакой {self.power}'

    def scream(self) -> int:
        """
        Выполняет массовую атаку крикливого гуся.
        Все игроки теряют часть денег.
        :return: количество украденных денег у каждого игрока
        """
        money_stolen_massive = self.power
        return money_stolen_massive

