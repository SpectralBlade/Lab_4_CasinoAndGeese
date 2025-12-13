class Player:

    _id = 1

    def __init__(self, name: str, age: int, balance: int, credit_count: int, armor: int = 0):
        self.name = name
        self.age = age
        self.balance = balance
        self.credit_count = credit_count
        self.ingameid = Player._id
        self.armor = armor
        self.train_cost = armor*1000
        Player._id += 1

    def __str__(self):
        return f'Игрок №{self.ingameid} {self.name} {self.age} лет с балансом {self.balance} и {self.credit_count} кредитами'

    def repr(self):
        return f'№{self.ingameid} {self.name}'

    def can_take_credit(self):
        return self.credit_count <= 2 and self.balance == 0

    def can_pay_credit(self):
        return self.balance >= 20000 and self.credit_count != 0

    def can_train_in_gym(self, armor: int):
        return self.balance >= 1000*(armor+1)