from Lab_4_CasinoAndGeese.src.classes.goose import WarGoose, HealerGoose, HonkGoose

T = [WarGoose, HonkGoose, HealerGoose]

class GooseCollection:
    def __init__(self):
        self.geese = []

    def __add__(self, goose: WarGoose | HealerGoose | HonkGoose):
        self.geese.append(goose)

    def __delitem__(self, goose: WarGoose | HealerGoose | HonkGoose):
        if goose in self.geese:
            self.geese.remove(goose)

    def __len__(self):
        return len(self.geese)

    def __iter__(self):
        return iter(self.geese)

    def __getitem__(self, index):
        return self.geese[index]

    def get_by_type(self, goose_type: type[T]) -> list:
        return [goose for goose in self.geese if type(goose) is goose_type]