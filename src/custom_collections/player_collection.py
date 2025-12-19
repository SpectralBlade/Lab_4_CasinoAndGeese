from Lab_4_CasinoAndGeese.src.classes.player import Player

class PlayerCollection:
    def __init__(self):
        """Инициализация пустого списка игроков."""
        self.players = []

    def __add__(self, player: Player):
        """Добавление игрока в список."""
        self.players.append(player)

    def __delitem__(self, player: Player):
        """Изгнание игрока в лес (удаление из коллекции)."""
        if player in self.players:
            self.players.remove(player)

    def __len__(self):
        """Получение длины списка игроков."""
        return len(self.players)

    def __iter__(self):
        """Итерация списка с игроками."""
        return iter(self.players)

    def __getitem__(self, index):
        """Получение игрока по индексу."""
        return self.players[index]
