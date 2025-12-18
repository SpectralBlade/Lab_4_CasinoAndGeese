def test_player_attacks_goose(casino, player, war_goose):
    casino.player_attacks_goose(player, war_goose)
    assert war_goose.hp == 1600

def test_goose_cooking(casino, player, war_goose):
    war_goose.hp = 300
    casino.player_attacks_goose(player, war_goose)
    assert len(casino.geese) == 0

def test_player_attack_damage_scales(casino, player, war_goose):
    player.damage_level = 2
    war_goose.hp = 3000
    casino.player_attacks_goose(player, war_goose)

    assert war_goose.hp == 1400

def test_honkgoose_scream_safe_balance(casino, player, honk_goose, monkeypatch):
    monkeypatch.setattr(honk_goose, "scream", lambda: 1000)
    casino.honkgoose_screams(honk_goose)

    assert player.balance == 4000

def test_healergoose_heals_target(casino, healer_goose, monkeypatch):
    target = list(casino.geese)[0]
    target.hp = 100
    monkeypatch.setattr(healer_goose, "heal", lambda: 200)

    casino.healergoose_heals(healer_goose, target)

    assert target.hp == 300

def test_check_player_balance_triggers_credit(casino, player, monkeypatch):
    player.balance = 0

    called = False

    def fake_credit(p):
        nonlocal called
        called = True

    monkeypatch.setattr(casino, "give_credit_to_player", fake_credit)

    casino.check_player_balance(player)

    assert called is True

def test_give_credit_ejects_player(casino, player, monkeypatch):
    player.balance = 0
    player.credit_count = 3

    ejected = False

    def fake_eject(p):
        nonlocal ejected
        ejected = True

    monkeypatch.setattr(casino, "eject_player", fake_eject)

    casino.give_credit_to_player(player)

    assert ejected is True

def test_take_credit_from_player(casino, player):
    casino.balances[player] = 30000
    player.credit_count = 1

    casino.take_credit_from_player(player)

    assert player.balance == 10000
    assert player.credit_count == 0

def test_regular_goose_attack_dodge(casino, player, war_goose, monkeypatch):
    player.armor = 10
    war_goose.hp = 1000

    monkeypatch.setattr("random.randint", lambda a, b: 1)

    casino.regular_goose_attack(war_goose, player)

    assert war_goose.hp < 1000

def test_regular_goose_attack_hits(casino, player, war_goose, monkeypatch):
    player.armor = 0
    casino.balances[player] = 1000

    monkeypatch.setattr("random.randint", lambda a, b: 10)
    monkeypatch.setattr(war_goose, "attack", lambda: 1.0)

    casino.regular_goose_attack(war_goose, player)

    assert player.balance < 1000


def test_blood_moon_buff(casino, war_goose):
    old_power = war_goose.power

    casino.blood_moon_emit(multiplier=2)

    assert war_goose.power == old_power * 2

def test_all_player_restock(casino, player):
    old_balance = player.balance

    casino.all_player_restock()

    assert player.balance == old_balance + 5000

def test_new_member_adds_player(casino, monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 1)
    monkeypatch.setattr("random.choice", lambda x: x[0])

    old_len = len(casino.players)

    casino.new_member_appearance()

    assert len(casino.players) == old_len + 1

def test_new_member_adds_goose(casino, monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 2)
    monkeypatch.setattr("random.choice", lambda x: x[0])

    old_len = len(casino.geese)

    casino.new_member_appearance()

    assert len(casino.geese) == old_len + 1

def test_win_message_players_lose(casino):
    casino.players.players.clear()

    casino.win_message_check()

    assert casino.game_ended is True

def test_make_a_bid_win_branch(casino, player, monkeypatch):
    casino.balances[player] = 5000

    seq = [200, 9000]  # ставка, winning_coefficient
    monkeypatch.setattr("random.randint", lambda a, b: seq.pop(0))
    monkeypatch.setattr("time.sleep", lambda _: None)

    casino.make_a_bid(player)

    assert player.balance >= 5000

def test_player_attack_goose_survives(casino, player, war_goose):
    war_goose.hp = 10_000
    player.damage_level = 0

    casino.player_attacks_goose(player, war_goose)

    assert war_goose.hp > 0
    assert len(casino.geese) == 1

def test_new_member_appearance_adds_goose(casino, monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 2)
    monkeypatch.setattr("random.choice", lambda x: x[0])

    old_len = len(casino.geese)

    casino.new_member_appearance()

    assert len(casino.geese) == old_len + 1

def test_honkgoose_scream_no_negative_branch(casino, honk_goose, monkeypatch):
    casino.balances[list(casino.players)[0]] = 10_000

    monkeypatch.setattr(honk_goose, "scream", lambda: 100)

    casino.honkgoose_screams(honk_goose)

    assert list(casino.players)[0].balance == 9900

def test_healergoose_heals_logs(casino, healer_goose, monkeypatch):
    target = list(casino.geese)[0]

    monkeypatch.setattr(healer_goose, "heal", lambda: 50)

    casino.healergoose_heals(healer_goose, target)

    assert target.hp > 0

def test_wargoose_bites_player(casino, war_goose, player, monkeypatch):
    casino.balances[player] = 5000
    monkeypatch.setattr(war_goose, "hard_attack", lambda: 500)

    casino.wargoose_bites(war_goose, player)

    assert player.balance == 4500

def test_give_credit_pass_branch(casino, player):
    player.credit_count = 1
    casino.balances[player] = 1000

    casino.give_credit_to_player(player)

    assert player.credit_count == 1

def test_take_credit_logs(casino, player):
    casino.balances[player] = 25000
    player.credit_count = 1

    casino.take_credit_from_player(player)

    assert player.credit_count == 0

def test_player_trains_in_gym(casino, player):
    casino.balances[player] = 10_000

    casino.player_trains_in_gym(player)

    assert player.armor == 1

def test_random_event_blood_moon(casino, monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 101)
    monkeypatch.setattr("random.choice", lambda x: 1.2)

    casino.random_event_choose()

    assert list(casino.geese)[0].power > 0

def test_random_event_restock(casino, player, monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 105)

    old_balance = player.balance
    casino.random_event_choose()

    assert player.balance == old_balance + 5000

def test_random_event_new_member(casino, monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 109)
    monkeypatch.setattr("random.choice", lambda x: x[0])

    old_players = len(casino.players)
    casino.random_event_choose()

    assert len(casino.players) >= old_players
