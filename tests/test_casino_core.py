def test_make_a_bid_reduces_balance_deterministic(casino, player, monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: a)
    monkeypatch.setattr("time.sleep", lambda _: None)

    start_balance = player.balance
    casino.make_a_bid(player)

    assert player.balance < start_balance
    assert player.balance >= 0

def test_make_a_bid_triggers_credit(casino, player, monkeypatch):
    player.balance = 0

    called = False

    def fake_credit(p):
        nonlocal called
        called = True
        p.balance = 15000

    monkeypatch.setattr(casino, "give_credit_to_player", fake_credit)

    casino.make_a_bid(player)

    assert called is True
    assert player.balance == 15000
