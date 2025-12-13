from typing import Literal
import random

class Goose:
    _id = 1

    def __init__(self, name: str, hp: int, type: Literal['Воюющий', 'Лечащий', 'Крикливый']):
        self.name = name
        self.hp = hp
        self.type = type

        self.ingameid = Goose._id
        Goose._id += 1

    def repr(self):
        return f'№{self.ingameid} {self.name}'

    def attack(self):
        money_stolen = random.randint(250, 500)
        return money_stolen

class WarGoose(Goose):
    def __init__(self, name: str, power: int):
        super().__init__(name, 2000, "Воюющий")
        self.power = power

    def __str__(self):
        return f'{self.type} гусь {self.name} №{self.ingameid} со здоровьем {self.hp} и силой атаки {self.power}'

    def hard_attack(self):
        money_stolen_hard = self.power*7
        return money_stolen_hard

class HealerGoose(Goose):
    def __init__(self, name: str, power: int):
        super().__init__(name, 1500,"Лечащий")
        self.power = power

    def __str__(self):
        return f'{self.type} гусь {self.name} №{self.ingameid} со здоровьем {self.hp} и силой лечения {self.power}'

    def heal(self):
        healed_hp = self.power
        return healed_hp

class HonkGoose(Goose):
    def __init__(self, name: str, power: int):
        super().__init__(name, 1000,"Крикливый")
        self.power = power

    def __str__(self):
        return f'{self.type} гусь {self.name} №{self.ingameid} со здоровьем {self.hp} и массовой атакой {self.power}'

    def scream(self):
        money_stolen_massive = self.power
        return money_stolen_massive

