import random

def gen():
    return random.randint(1, len(zones_id))

def valid(x):
    try:
        if float(x) == int(x) and 0 < int(x) <= len(zones_id):
            return True
        else:
            0 / 0
    except:
        return False

def libvalid(x):
    try:
        if float(x) == int(x):
            return True
        else:
            0 / 0
    except:
        return False

allok = False
try:
    import settings_lib
    lib = settings_lib
    ln = lib.lib_name
    enemy_name = lib.enemy_name
    zones_id = lib.zones_id
    damage = lib.damage
    vampire = lib.vampire
    player_turn = lib.player_turn
    hp = lib.hp
    print('-------------------------------------------------------------------------------------------------------')
    print('Сценарий "{}".'.format(ln))
    print('Имя врага: {}'.format(enemy_name))
    print('Здоровье: {}'.format(hp))
    print('Урон: {} hp.'.format(damage))
    if vampire <= 0:
        print('Вампиризм: отсутствует')
    else:
        print('Вампиризм: {} hp.'.format(vampire))
    if player_turn:
        print('Вы нападаете первый.')
    else:
        print('Враг нападает первый.')
    print('-------------------------------------------------------------------------------------------------------')
    if libvalid(damage) and libvalid(vampire) and libvalid(player_turn):
        allok = True
    
except:
    pass

class Player:
    def __init__(self):
        self.hp = hp

if allok:
    enemy = Player()
    player = Player()
    # game loop
    while True:
        print('Игрок ({} hp) vs {} ({} hp)'.format(player.hp, enemy_name, enemy.hp))
        if player_turn:
            print('Вы атакуете. Выберите, что бить:')
        else:
            print('Вы защищаетесь. Выберите, что защищать:')
        for i in range(1, len(zones_id) + 1):
            print('{}. {}'.format(i, zones_id[i]))
        choice = input()
        if valid(choice):
            choice = int(choice)
            bot = gen()
            if player_turn:
                print('Вы попытались ударить врага в {}, он попытался защитить {}, а это значит, что '.format(zones_id[choice], zones_id[bot]), end='')
                if choice == bot:
                    print('удар был блокирован.')
                else:
                    print('вы нанесли урон (-{} hp).'.format(damage))
                    enemy.hp -= damage
                    if vampire > 0:
                        print('Вы подлечились на {} hp.'.format(vampire))
                        player.hp += vampire
            else:
                print('Вы попытались защитить {}, ваш противник попытался ударить в {}, а это значит, что '.format(zones_id[choice], zones_id[bot]), end='')
                if choice == bot:
                    print('удар был блокирован.')
                else:
                    print('вам нанесли урон (-{} hp).'.format(damage))
                    player.hp -= damage
                    if vampire > 0:
                        print('Враг подлечился на {} hp.'.format(vampire))
                        enemy.hp += vampire
                
            print('-------------------------------------------------------------------------------------------------------')
            player_turn = not player_turn
        else:
            print('Неверный ввод.')
            print('-------------------------------------------------------------------------------------------------------')
    
        if player.hp <= 0 or enemy.hp <= 0:
            break

    print()
    if player.hp <= 0:
        print('Вы умерли. У вашего врага осталось {} hp.'.format(enemy.hp))
    else:
        print('Враг повержен. У вас осталось {} hp.'.format(player.hp))
else:
    print('Ошибка импортирования сценария. Возможно, он повреждён или находится в неверной директории.')