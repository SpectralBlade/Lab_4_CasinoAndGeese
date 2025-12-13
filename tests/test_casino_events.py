def test_player_attacks_goose(casino, player, war_goose):
    casino.player_attacks_goose(player, war_goose)
    assert war_goose.hp == 1600

def test_goose_cooking(casino, player, war_goose):
    war_goose.hp = 300
    casino.player_attacks_goose(player, war_goose)
    assert len(casino.geese) == 0
