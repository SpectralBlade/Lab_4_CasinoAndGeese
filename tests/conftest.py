import pytest
from Lab_4_CasinoAndGeese.src.classes.player import Player
from Lab_4_CasinoAndGeese.src.classes.goose import WarGoose, HealerGoose, HonkGoose
from Lab_4_CasinoAndGeese.src.custom_collections.player_collection import PlayerCollection
from Lab_4_CasinoAndGeese.src.custom_collections.goose_collection import GooseCollection
from Lab_4_CasinoAndGeese.src.classes.casino import Casino

@pytest.fixture
def player():
    return Player("GawrGura", 25, 5000, 0)

@pytest.fixture
def war_goose():
    return WarGoose("WarGoose", 300)

@pytest.fixture
def healer_goose():
    return HealerGoose("HealGoose", 200)

@pytest.fixture
def honk_goose():
    return HonkGoose("HonkGoose", 150)

@pytest.fixture
def casino(player, war_goose):
    players = PlayerCollection()
    geese = GooseCollection()
    players + player
    geese + war_goose

    casino = Casino(players, geese)
    casino.balances + player
    return casino
