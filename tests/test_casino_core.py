def test_make_a_bid_reduces_balance(casino, player, monkeypatch):
    def fake_randint(a, b):
        return a

    monkeypatch.setattr("random.randint", fake_randint)
    monkeypatch.setattr("time.sleep", lambda _: None)

    old_balance = player.balance
    casino.make_a_bid(player)

    assert player.balance <= old_balance
