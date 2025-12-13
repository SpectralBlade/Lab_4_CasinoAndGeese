from Lab_4_CasinoAndGeese.src.classes.goose import WarGoose, HonkGoose, HealerGoose

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

RANDOM_EVENTS = [
    'heal',
    'heavy_attack',
    'honk',
    'deposit',
    'take_credit',
    'pay_credit',
    'train_in_gym',
]