from Lab_4_CasinoAndGeese.src.custom_collections.goose_collection import GooseCollection
from Lab_4_CasinoAndGeese.src.custom_collections.player_collection import PlayerCollection
from Lab_4_CasinoAndGeese.src.custom_collections.casino_collection import CasinoCollection
from Lab_4_CasinoAndGeese.src.classes.goose import WarGoose, HonkGoose, HealerGoose
from Lab_4_CasinoAndGeese.src.classes.player import Player
from Lab_4_CasinoAndGeese.src.logger import Logger
from Lab_4_CasinoAndGeese.src.func_to_goose import CMD_TO_GOOSE
from Lab_4_CasinoAndGeese.src.name_choices import PLAYER_NAMES, GOOSE_NAMES

import random
from typing import Literal

class Casino:
    def __init__(self, players: PlayerCollection, geese: GooseCollection) -> None:
        """
        Функция инициализации казино.
        :param players: пользовательская коллекция с классами игроков.
        :param geese: пользовательская коллекция с классами гусей.
        :return: Данная функция ничего не возвращает
        """
        self.players = players
        self.geese = geese
        self.logger = Logger()
        self.balances = CasinoCollection()
        self.current_step = 0
        self.minimal_bid = 200
        self.game_ended = False

    def check_player_balance(self, player: Player) -> None:
        """
        Проверяет баланс игрока и при необходимости отправляет его за кредитом.
        Если баланс игрока равен нулю - вызывается процедура выдачи кредита.
        :param player: объект игрока, баланс которого проверяется.
        :return: Данная функция ничего не возвращает
        """
        if player.balance <= 0:
            self.logger.logging_message(
                f'Игрок {player.repr()} - банкрот! ({player.balance}$). Ему придется идти в Т-Банк за кредитом. :('
            )
            self.give_credit_to_player(player)

    def new_player_add(self, name: str, age: int, balance: int, credit_count: int, armor: int = 0) -> None:
        """
        Добавляет нового игрока в казино.
        Создаёт объект игрока, добавляет его в коллекцию игроков и регистрирует баланс.
        :param name: имя игрока
        :param age: возраст игрока
        :param balance: начальный баланс игрока
        :param credit_count: количество уже взятых кредитов
        :param armor: уровень ловкости игрока
        :return: Данная функция ничего не возвращает
        """
        dummy = Player(name, age, balance, credit_count, armor)
        self.players + dummy
        self.balances + dummy
        self.logger.logging_message(f'{dummy} вошел в игорный дом!')

    def new_goose_add(self, name: str, type: Literal['Воюющий', 'Лечащий', 'Крикливый'], power: int) -> None:
        """
        Добавляет нового гуся в казино.
        Создаёт объект гуся выбранного типа и добавляет его в коллекцию гусей.
        :param name: имя гуся
        :param type: тип гуся (Воюющий, Лечащий или Крикливый)
        :param power: сила гуся
        :return: Данная функция ничего не возвращает
        """
        honker = CMD_TO_GOOSE[type](name, power)
        self.geese + honker
        self.logger.logging_message(f'{honker} вылупился из яйца!')

    def make_a_bid(self, player: Player):
        """
        Позволяет игроку сделать ставку в игровом автомате.
        Размер ставки и выигрыш определяются случайным образом.
        При недостатке средств игроку предлагается взять кредит (его отправляют за ним насильно).
        :param player: объект игрока, делающего ставку
        :return: Данная функция ничего не возвращает
        """
        if player.balance < self.minimal_bid:
            self.logger.logging_message(
                f'Игрок {player.repr()} не может сделать ставку — недостаточно средств! :(.'
            )
            self.give_credit_to_player(player)
            return

        max_bid = max(self.minimal_bid, (int(player.balance/1.5) - 200))

        ruletka_bid = random.randint(self.minimal_bid, max_bid)
        self.balances[player] -= ruletka_bid
        self.logger.logging_message(f'Игрок {player.repr()} сделал ставку {ruletka_bid}$ в игровом автомате!\nКрутим слоты...')
        winning_coefficient = random.randint(1, 10000)
        if winning_coefficient in range(1, 5000):
            cash_won = 0
            self.logger.logging_message(
                f'Какая неудача! Игрок {player.repr()} потерял всю ставку!')
        elif winning_coefficient in range(5000, 7500):
            cash_won = int(ruletka_bid*0.5)
            self.logger.logging_message(
                f'Аутсайдер... Игрок {player.repr()} выиграл всего лишь {cash_won}$!')
        elif winning_coefficient in range(7500, 8750):
            cash_won = ruletka_bid
            self.logger.logging_message(
                f'Не повезло... Игрок {player.repr()} выиграл свою ставку {cash_won}$!')
        elif winning_coefficient in range(8750, 9375):
            cash_won = ruletka_bid*2
            self.logger.logging_message(
                f'Удача! Игрок {player.repr()} выиграл {cash_won}$!')
        elif winning_coefficient in range(9375, 9675):
            cash_won = ruletka_bid*5
            self.logger.logging_message(
                f'Крупная удача! Игрок {player.repr()} выиграл {cash_won}$!')
        elif winning_coefficient in range(9675, 9975):
            cash_won = ruletka_bid*10
            self.logger.logging_message(
                f'Огромная удача! Игрок {player.repr()} выиграл {cash_won}$!')
        else:
            cash_won = ruletka_bid*100
            self.logger.logging_message(
                f'АБСОЛЮТНЫЙ ДЖЕКПОТ!!! Игрок {player.repr()} выиграл {cash_won}$!!!')
        self.balances[player] += cash_won
        self.check_player_balance(player)

    def eject_player(self, player: Player) -> None:
        """
        Удаляет игрока из казино.
        Используется при отказе в кредите или полном банкротстве игрока.
        :param player: объект игрока, подлежащего удалению
        :return: Данная функция ничего не возвращает
        """
        self.players.__delitem__(player)
        self.logger.logging_message(f'Игрок {player.repr()} сослан в лес на вечное заточение!')

    def cook_goose(self, goose: WarGoose | HealerGoose | HonkGoose) -> None:
        """
        Удаляет гуся из казино.
        Вызывается при нокауте гуся в результате атаки.
        :param goose: объект гуся, который будет удалён
        :return: Данная функция ничего не возвращает
        """
        self.geese.__delitem__(goose)
        self.logger.logging_message(f'Гусь {goose.repr()} был зажарен на костре и подан в качестве ужина!')

    def all_goose_buff(self, multiplier: float) -> None:
        """
        Увеличивает силу всех гусей в казино.
        Используется во время специальных случайных событий (планировалось много где,
        но пока используется только в Кровавой луне).
        :param multiplier: множитель увеличения силы гусей
        :return: Данная функция ничего не возвращает
        """
        self.logger.logging_message(f'Сила всех гусей была увеличена в {multiplier} раз!')
        for goose in self.geese:
            goose.power = int(goose.power * multiplier)

    def all_player_restock(self) -> None:
        """
        Пополняет баланс всех игроков на фиксированную сумму.
        Используется как случайное событие (приход степухи).
        :return: Данная функция ничего не возвращает
        """
        surplus = 5000
        self.logger.logging_message(f'СЛУЧАЙНОЕ СОБЫТИЕ: СТЕПУХА ПРИШЛА!\nСидя за игровым столом, молодые люди даже и не '
                                    f'заметили, как на телефонах всех из них прозвучало уведомление... \nТолько после окончания'
                                    f' круга, под счастливый визг и звон бокалов, они отпраздновали приход стипендии...\n'
                                    f'Кошельки всех игроков пополнены на 5000$!')
        for player in self.players:
            self.balances[player] += surplus

    def player_attacks_goose(self, player: Player, goose: WarGoose | HealerGoose | HonkGoose) -> None:
        """
        Позволяет игроку атаковать гуся.
        Урон зависит от уровня силы игрока.
        При снижении здоровья гуся до нуля гусь удаляется из казино.
        :param player: объект атакующего игрока
        :param goose: объект гуся, подвергшегося атаке
        :return: Данная функция ничего не возвращает
        """
        damage = (400*int(1.5*player.damage_level+1))
        goose.hp -= damage

        self.logger.logging_message(
            f'Игрок {player.repr()} в ярости напал на гуся {goose.repr()}, желая прогнать, и нанёс ему {damage} урона!\n'
            f'Текущее здоровье гуся: {max(goose.hp, 0)} HP'
        )

        if goose.hp <= 0:
            self.logger.logging_message(
                f'Увы! Гусь {goose.repr()} пал в неравном бою!'
            )
            self.cook_goose(goose)

    def new_member_appearance(self) -> None:
        """
        Добавляет нового участника в казино.
        Случайным образом выбирается, появится ли новый игрок или новый гусь.
        :return: Данная функция ничего не возвращает
        """
        i = random.randint(1, 2)
        self.logger.logging_message(f'Кажется... в нашем казино пополнение!')
        if i == 1:
            name = random.choice(PLAYER_NAMES)
            age = random.randint(16, 45)
            balance = random.randint(1000, 5000)
            credit_count = random.randint(0, 2)
            self.new_player_add(name, age, balance, credit_count)
        elif i == 2:
            name = random.choice(GOOSE_NAMES)
            type = random.choice(['Воюющий', 'Лечащий', 'Крикливый'])
            stat = random.randint(250, 500)
            self.new_goose_add(name, type, stat)

    def honkgoose_screams(self, goose: HonkGoose) -> None:
        """
        Обрабатывает крик крикливого гуся.
        Все игроки теряют часть денег из-за испуга.
        Баланс игроков не может стать отрицательным.
        :param goose: объект крикливого гуся
        :return: Данная функция ничего не возвращает
        """
        dropped_money = goose.scream()

        for player in self.players:
            loss = min(dropped_money, player.balance)
            self.balances[player] -= loss

        self.logger.logging_message(f'Гусь {goose.repr()} кричит, и от испуга все игроки выронили по {dropped_money}$!')
        for player in self.players:
            if player.balance < 0:
                self.balances[player] = 0
                self.check_player_balance(player)

    def healergoose_heals(self, goose: HealerGoose, target: HealerGoose | WarGoose | HonkGoose) -> None:
        """
        Позволяет лечащему гусю восстановить здоровье другому гусю.
        :param goose: объект лечащего гуся
        :param target: объект гуся, которому восстанавливается здоровье
        :return: Данная функция ничего не возвращает
        """
        refill_health = goose.heal()
        target.hp += refill_health
        self.logger.logging_message(f'Гусь {goose.repr()} своими магическими силами длинного клюва исцелил гуся {target.repr()} на {refill_health} HP!\nТекущее здоровье гуся: {target.hp} HP')

    def wargoose_bites(self, goose: WarGoose, target: Player) -> None:
        """
        Обрабатывает атаку воюющего гуся на игрока.
        У игрока отнимается часть денег.
        :param goose: объект воюющего гуся
        :param target: объект игрока, подвергшегося атаке
        :return: Данная функция ничего не возвращает
        """
        money_stolen = goose.hard_attack()
        money_stolen = min(money_stolen, target.balance)
        self.balances[target] -= money_stolen
        self.logger.logging_message(f'Наглый гусь {goose.repr()} больно укусил игрока {target.repr()} за ногу! Игрок теряет выпавшие у него из рук {money_stolen}$.')
        self.check_player_balance(target)

    def give_credit_to_player(self, player: Player):
        """
        Выдаёт игроку кредит при соблюдении условий.
        Если лимит кредитов исчерпан, игрок удаляется из казино.
        :param player: объект игрока
        :return: Данная функция ничего не возвращает
        """
        if player.can_take_credit():
            self.balances[player] += 15000
            player.credit_count += 1
            self.logger.logging_message(f'Из-за долговой ямы игрок {player.repr()} '
                                        f'принял решение взять 15000$ в кредит! Сможет ли он отыграться?\nОсталось доступно в кредитной истории: {3-player.credit_count} займа(ов).')
        elif player.credit_count <= 2:
            pass
        else:
            self.logger.logging_message(f'Игроку {player.repr()} было отказано в кредите...')
            self.eject_player(player)

    def take_credit_from_player(self, player: Player) -> None:
        """
        Пытается списать долг по кредиту с игрока.
        Уменьшает количество кредитов при успешной оплате.
        :param player: объект игрока
        :return: Данная функция ничего не возвращает
        """
        if player.can_pay_credit() == 1:
            self.balances[player] -= 20000
            player.credit_count -= 1
            self.logger.logging_message(f'Поздравим игрока {player.repr()}! Он смог выплатить долг по кредиту '
                                        f'№{player.credit_count+1}!\nТекущее количество кредитов у игрока: {player.credit_count}.')

    def regular_goose_attack(self, goose: WarGoose | HealerGoose | HonkGoose, player: Player) -> None:
        """
        Обрабатывает обычную атаку гуся на игрока.
        Игрок может уклониться в зависимости от уровня ловкости.
        :param goose: объект гуся
        :param player: объект игрока
        :return: Данная функция ничего не возвращает
        """
        stolen_money = int(goose.power*goose.attack())
        dnd_chance = random.randint(1, 10)
        self.logger.logging_message(f'Гусь {goose.repr()} внезапно кусает игрока {player.repr()}!')
        if dnd_chance <= player.armor:
            lost_hp = int(goose.hp*0.3)
            goose.hp -= lost_hp
            self.logger.logging_message(f'Гусь промахнулся и упал! Он ушибся и потерял {lost_hp} здоровья!\nТекущее здоровье гуся: {goose.hp}')
            if goose.hp <= 0:
                self.cook_goose(goose)
        else:
            self.balances[player] -= min(stolen_money, player.balance)
            self.logger.logging_message(f'Успех! От неожиданности игрок выронил {stolen_money}$!\nТекущий баланс игрока: {player.balance}$')
            self.check_player_balance(player)

    def player_trains_in_gym(self, player: Player) -> None:
        """
        Позволяет игроку тренироваться в зале.
        Повышает ловкость игрока (максимум - 10) и уменьшает его баланс.
        :param player: объект игрока
        :return: Данная функция ничего не возвращает
        """
        if player.can_train_in_gym:
            player.armor += 1
            player.balance -= player.armor*1000
            self.logger.logging_message(f'Игрок {player.repr()} посетил подвальную качалку и повысил свою ловкость!\nТекущее значение: {player.armor}/10.')

    def player_trains_damage(self, player: Player) -> None:
        """
        Позволяет игроку увеличить уровень наносимого урона.
        Стоимость тренировки растёт с каждым уровнем.
        :param player: объект игрока
        :return: Данная функция ничего не возвращает
        """
        cost = 2000 * (player.damage_level + 1)

        if player.can_train_damage():
            self.balances[player] -= cost
            player.damage_level += 1

            self.logger.logging_message(
                f'Игрок {player.repr()} посетил гаражные соревнования по боксу и повысил свою силу!\n'
                f'Текущий урон: {400*int(1.5*player.damage_level+1)}\n'
            )
        
    def blood_moon_emit(self, multiplier: float) -> None:
        """
        Активирует событие «Кровавая луна».
        Увеличивает силу всех гусей в казино.
        :param multiplier: множитель увеличения силы
        :return: Данная функция ничего не возвращает
        """
        self.logger.logging_message(f'СЛУЧАЙНОЕ СОБЫТИЕ: КРОВАВАЯ ЛУНА!\nВ темную ночь, когда все игроки спокойно раскладывают покер...\n'
                                    f'Никто не смотрит за окно, а там - пробуждается кровавая луна... Гуси бурлят гневом, и их глаза наливаются яростью...')
        self.all_goose_buff(multiplier)

    def list_all_members(self) -> None:
        """
        Выводит список всех игроков и гусей в казино.
        Используется для отображения текущего состояния симуляции.
        :return: Данная функция ничего не возвращает
        """
        self.logger.logging_message('Игроки и гуси на текущем ходе:')
        for player in self.players:
            self.logger.logging_message(player, with_step=False)
        for goose in self.geese:
            self.logger.logging_message(goose, with_step=False)

    def win_message_check(self) -> None:
        """
        Проверяет условия завершения симуляции.
        Игра завершается, если в казино не осталось игроков или гусей.
        :return: Данная функция ничего не возвращает
        """
        if not self.players.players:
            self.logger.logging_message(f'\nКОНЕЦ СИМУЛЯЦИИ! Гуси сослали всех игроков в лес!\nТекущие гуси:\n')
            for goose in self.geese:
                self.logger.logging_message(goose, with_step=False)
            self.game_ended = True
        elif not self.geese.geese:
            self.logger.logging_message(f'\nКОНЕЦ СИМУЛЯЦИИ! Игроки поджарили на вертеле всех гусей!\nТекущие игроки:\n')
            for player in self.players:
                self.logger.logging_message(player, with_step=False)
            self.game_ended = True

    def new_game_message(self) -> None:
        """
        Мини-функция для вывода стартового сообщения (больше полезна в логах).
        :return: Данная функция ничего не возвращает
        """
        self.logger.logging_message('############### НАЧАЛО НОВОЙ СИМУЛЯЦИИ ###############')

    def random_event_choose(self) -> None:
        """
        Выбирает и выполняет случайное событие в казино.
        Событие определяется случайным числом и может влиять
        на игроков, гусей или общее состояние игры.
        :return: Данная функция ничего не возвращает
        """
        roll = random.randint(1, 110)

        self.win_message_check()
        if self.game_ended:
            return
        random_player = random.choice(self.players)
        random_goose = random.choice(self.geese)

        healer_geese = self.geese.get_by_type(HealerGoose)
        war_geese = self.geese.get_by_type(WarGoose)
        honk_geese = self.geese.get_by_type(HonkGoose)

        if roll <= 15:
            self.make_a_bid(random_player)

        elif roll <= 25:
            self.player_trains_in_gym(random_player)

        elif roll <= 35:
            self.player_trains_damage(random_player)

        elif roll <= 40:
            self.regular_goose_attack(random_goose, random_player)

        elif roll <= 50:
            self.take_credit_from_player(random_player)

        elif roll <= 60:
            self.give_credit_to_player(random_player)

        elif roll <= 70 and honk_geese:
            self.honkgoose_screams(random.choice(honk_geese))

        elif roll <= 80 and healer_geese and len(self.geese) > 1:
            healer = random.choice(healer_geese)
            target = random.choice([g for g in self.geese if g != healer])
            self.healergoose_heals(healer, target)

        elif roll <= 90 and war_geese:
            self.wargoose_bites(random.choice(war_geese), random_player)

        elif roll <= 100:
            self.player_attacks_goose(random_player, random_goose)

        elif roll <= 102:
            self.blood_moon_emit(multiplier=random.choice([1.2, 1.3, 1.4]))

        elif roll <= 107:
            self.all_player_restock()

        elif roll <= 110:
            self.new_member_appearance()

        else:
            self.random_event_choose()