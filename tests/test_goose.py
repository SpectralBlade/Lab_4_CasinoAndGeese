from Lab_4_CasinoAndGeese.src.classes.goose import WarGoose, HealerGoose, HonkGoose

def test_wargoose_attack():
    goose = WarGoose("КОЛЛОКВИУМ ПО ФУНДАМ", 100)
    assert goose.hard_attack() == 700

def test_healer_heal():
    goose = HealerGoose("КОЛЛОКВИУМ ПО ИПР", 200)
    assert goose.heal() == 200

def test_honk_scream():
    goose = HonkGoose("КОЛЛОКВИУМ ПО ПИТОНУ", 150)
    assert goose.scream() == 150
