from Lab_4_CasinoAndGeese.src.custom_collections.player_collection import PlayerCollection
from Lab_4_CasinoAndGeese.src.custom_collections.goose_collection import GooseCollection
from name_choices import PLAYER_NAMES, GOOSE_NAMES
from Lab_4_CasinoAndGeese.src.classes.casino import Casino
import time
import os
import random

def run_simulation(player_count: int, goose_count: int, steps: int, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)

    player_collection = PlayerCollection()
    goose_collection = GooseCollection()
    casino_777_banana = Casino(player_collection, goose_collection)

    for _ in range(player_count):
        age = random.randint(16, 45)
        balance = random.randint(1000, 5000)
        credit_count = random.randint(0, 2)
        casino_777_banana.new_player_add(random.choice(PLAYER_NAMES), age, balance, credit_count)

    for _ in range(goose_count):
        type = random.choice(['Воюющий', 'Лечащий', 'Крикливый'])
        stat = random.randint(250, 500)
        casino_777_banana.new_goose_add(random.choice(GOOSE_NAMES), type, stat)

    for i in range(1, steps+1):
        if casino_777_banana.game_ended:
            break
        casino_777_banana.current_step = i
        casino_777_banana.logger.set_step(i)
        casino_777_banana.random_event_choose()
        if i % 10 == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            casino_777_banana.list_all_members()



