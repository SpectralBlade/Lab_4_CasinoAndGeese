from Lab_4_CasinoAndGeese.src.classes.goose import WarGoose, HonkGoose, HealerGoose

# Функции для создания гусей определенного типа со словарем

def create_war_goose(name: str, power: int) -> WarGoose:
    return WarGoose(name, power)

def create_healer_goose(name: str, skill: int) -> HealerGoose:
    return HealerGoose(name, skill)

def create_honk_goose(name: str, volume: int) -> HonkGoose:
    return HonkGoose(name, volume)

CMD_TO_GOOSE = {
    "Воюющий": create_war_goose,
    "Лечащий": create_healer_goose,
    "Крикливый": create_honk_goose,
}