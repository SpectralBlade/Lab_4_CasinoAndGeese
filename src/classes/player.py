class Player:

    _id = 1

    def __init__(self, name: str, age: int, balance: int, credit_count: int, armor: int = 0, damage: int = 400):
        """
        Создаёт нового игрока.
        :param name: имя игрока
        :param age: возраст игрока
        :param balance: начальный баланс игрока
        :param credit_count: количество взятых кредитов
        :param armor: уровень ловкости (шанс уклонения, всегда 0 в начале)
        :param damage: базовый урон игрока (всегда 400 в начале)
        """
        self.name = name
        self.age = age
        self.balance = balance
        self.credit_count = credit_count
        self.ingameid = Player._id
        self.armor = armor
        self.train_cost = armor*1000
        self.damage = damage
        self.damage_level = 0
        Player._id += 1

    # Два строковых представления
    def __str__(self) -> str:
        return f'Игрок №{self.ingameid} {self.name} {self.age} лет с балансом {self.balance} и {self.credit_count} кредитами'

    def repr(self) -> str:
        return f'№{self.ingameid} {self.name}'

    # Проверки для случайных событий
    def can_take_credit(self) -> bool:
        return self.credit_count <= 2

    def can_pay_credit(self) -> bool:
        return self.balance >= 20000 and self.credit_count != 0

    def can_train_in_gym(self, armor: int) -> bool:
        return self.balance >= (1000*(armor+1)) and armor < 10

    def can_train_damage(self) -> bool:
        cost = 2000 * (self.damage_level + 1)
        return self.balance >= cost
