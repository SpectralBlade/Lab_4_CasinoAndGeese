from Lab_4_CasinoAndGeese.src.classes.goose import WarGoose, HealerGoose, HonkGoose

T = [WarGoose, HonkGoose, HealerGoose]

class GooseCollection:
    def __init__(self):
        """Инициализация пустого списка гусей."""
        self.geese = []

    def __add__(self, goose: WarGoose | HealerGoose | HonkGoose):
        """Добавление гуся одного из типов."""
        self.geese.append(goose)

    def __delitem__(self, goose: WarGoose | HealerGoose | HonkGoose):
        """Жарка гуся на костре (удаление из списка)."""
        if goose in self.geese:
            self.geese.remove(goose)

    def __len__(self):
        """Получение длины списка гусей."""
        return len(self.geese)

    def __iter__(self):
        """Итерация списка гусей."""
        return iter(self.geese)

    def __getitem__(self, index):
        """Получение гуся по индексу."""
        return self.geese[index]

    def get_by_type(self, goose_type: type[T]) -> list:
        """Вспомогательный метод для возвращения списка с гусями определенного типа."""
        return [goose for goose in self.geese if type(goose) is goose_type]