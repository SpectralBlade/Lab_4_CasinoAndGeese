def test_random_event_trains_damage(casino, player, monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 30)
    monkeypatch.setattr("random.choice", lambda x: x[0])
    player.balance = 10000
    old_level = player.damage_level
    casino.random_event_choose()

    assert player.damage_level == old_level + 1

def test_random_event_trains_armor(casino, player, monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 20)
    monkeypatch.setattr("random.choice", lambda x: x[0])
    old_armor = player.armor
    player.balance = 5000

    casino.random_event_choose()
    assert player.armor == old_armor + 1

def test_random_event_stops_when_game_ended(casino, monkeypatch):
    casino.game_ended = True
    called = False
    def fake_event(*args, **kwargs):
        nonlocal called
        called = True

    monkeypatch.setattr(casino, "make_a_bid", fake_event)
    casino.random_event_choose()

    assert called is False

