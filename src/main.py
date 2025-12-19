from Lab_4_CasinoAndGeese.src.create_simulation import run_simulation

def main() -> None:
    try:
        player_count = int(input("Введите начальное кол-во игроков: "))
        goose_count = int(input("Введите начальное кол-во гусей: "))

        seed_input = input("Введите seed (или оставьте пустым для случайного): ").strip()
        seed = int(seed_input) if seed_input else None

        steps_input = input("Введите количество ходов (по умолчанию 50): ").strip()
        steps = int(steps_input) if steps_input else 50

        time_mode = int(input(
            "Выберите режим времени:\n"
            "0 — задержка 2 сек после каждого хода\n"
            "1 — задержка 3 сек на 9, 19, 29... ходах\n"
            "2 — без задержек\n"
        ))

        if time_mode not in (0, 1, 2):
            raise ValueError

    except ValueError:
        print("Ошибка ввода: необходимо вводить целые числа.")
        return

    run_simulation(
        player_count=player_count,
        goose_count=goose_count,
        steps=steps,
        seed=seed,
        time_mode=time_mode
    )

if __name__ == "__main__":
    main()
