from Lab_4_CasinoAndGeese.src.classes.player import Player

class CasinoCollection:
    def __init__(self):
        self.players_balances: dict[int, int] = {}

    def __add__(self, player: Player):
        self.players_balances[player.ingameid] = player.balance

    def __getitem__(self, player: Player) -> int:
        return self.players_balances[player.ingameid]

    def __setitem__(self, player: Player, new_balance: int):
        self.players_balances[player.ingameid] = new_balance
        player.balance = new_balance

