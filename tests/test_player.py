from Lab_4_CasinoAndGeese.src.classes.player import Player

def test_player_credit_logic():
    player = Player("Гавр Гура", 20, 0, 0)
    assert player.can_take_credit() is True

    player.balance = 100
    assert player.can_take_credit() is False


def test_player_can_pay_credit():
    player = Player("Амелия Ватсон", 20, 20000, 1)
    assert player.can_pay_credit() is True

    player.balance = 10000
    assert player.can_pay_credit() is False
