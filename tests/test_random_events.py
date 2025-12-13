def test_random_event_make_bid(casino, player, monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 10)
    monkeypatch.setattr("random.choice", lambda x: x[0])
    monkeypatch.setattr("time.sleep", lambda _: None)

    casino.random_event_choose()
    assert player.balance >= 0
