from Lab_4_CasinoAndGeese.src.classes.player import Player

class PlayerCollection:
    def __init__(self):
        self.players = []

    def __add__(self, player: Player):
        self.players.append(player)

    def __delitem__(self, player: Player):
        if player in self.players:
            self.players.remove(player)

    def __len__(self):
        return len(self.players)

    def __iter__(self):
        return iter(self.players)

    def __getitem__(self, index):
        return self.players[index]
