from enum import Enum
from random import randint, choice


class Ability(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    STAP = 5
    LAKES = 6


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} HEALTH: {self.__health} DAMAGE: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if hero.ability == Ability.BLOCK_DAMAGE_AND_REVERT and self.defence != Ability.BLOCK_DAMAGE_AND_REVERT:
                    hero.blocked_damage = int(self.damage / 5)
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if type(ability) == Ability:
            self.__ability = ability
        else:
            raise ValueError('Wrong data type for attribute ability')

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = randint(2, 6)
        boss.health -= self.damage * coeff
        print(f'Warrior {self.name} hits critically {self.damage * coeff}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOST)

    def apply_super_power(self, boss, heroes):
        boost_point = randint(7, 10)
        print(f"Boost: {boost_point}")
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.damage += boost_point


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, Ability.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted blocked damage {self.blocked_damage}')


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.STAP)

    def apply_super_power(self, boss, heroes):
        stun = [1, 2, 3]
        b = choice(stun)
        if b == 1:
            boss.damage = 0
            print("STAP BOSS")
        else:
            boss.damage = 50


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.LAKES)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health <= 0 and boss.health > 0:
                hero.health += self.health
                self.health = 0
                print(f"{self.name} sacrificed himself and was revived {hero.name}")


round_number = 0


def start_game():
    warrior_1 = Warrior('Viking', 280, 20)
    warrior_2 = Warrior('Warrio', 270, 15)
    doc = Medic('Hendolf', 250, 5, 15)
    assistant = Medic('Herrold', 300, 5, 5)
    berserk = Berserk('Olaf', 260, 10)
    magic = Magic('Potter', 290, 15)

    heroes_list = [warrior_1, warrior_2, magic, doc, berserk, assistant]

    boss = Boss('Baron Nashor', 1000, 50)

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


def show_statistics(boss, heroes):
    print(f'ROUND {round_number} --------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print('Boss won!!!')

    return all_heroes_dead


start_game()
