from Lab_4_CasinoAndGeese.src.classes.player import Player

class CasinoCollection:
    def __init__(self):
        """Создание пустого словаря вида игрок-баланс."""
        self.players_balances: dict[int, int] = {}

    def __add__(self, player: Player) -> None:
        """Добавление нового игрока в словарь казино."""
        self.players_balances[player.ingameid] = player.balance

    def __getitem__(self, player: Player) -> int:
        """Получение баланса игрока."""
        return self.players_balances[player.ingameid]

    def __setitem__(self, player: Player, new_balance: int) -> None:
        """Установление баланса игрока на новое значение."""
        self.players_balances[player.ingameid] = new_balance
        player.balance = new_balance

