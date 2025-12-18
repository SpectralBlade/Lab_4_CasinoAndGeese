from Lab_4_CasinoAndGeese.src.custom_collections.player_collection import PlayerCollection
from Lab_4_CasinoAndGeese.src.custom_collections.goose_collection import GooseCollection
from Lab_4_CasinoAndGeese.src.custom_collections.casino_collection import CasinoCollection
from Lab_4_CasinoAndGeese.src.classes.player import Player
from Lab_4_CasinoAndGeese.src.classes.goose import WarGoose

def test_player_collection_add_remove():
    pc = PlayerCollection()
    p = Player("Гавр Гура", 20, 1000, 0)

    pc + p
    assert len(pc) == 1

    pc.__delitem__(p)
    assert len(pc) == 0

def test_goose_collection_by_type():
    gc = GooseCollection()
    g = WarGoose("КОНТЕСТ", 100)
    gc + g

    result = gc.get_by_type(type(g))
    assert result == [g]

def test_casino_collection_sync():
    p = Player("Амелия Ватсон", 20, 1000, 0)
    cc = CasinoCollection()
    cc + p

    cc[p] = 500
    assert p.balance == 500
