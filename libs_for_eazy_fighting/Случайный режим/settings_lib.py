import random
r = random.randint
c = random.choice
k = [i for i in range(65, 91)] +  [i for i in range(97, 123)]
lib_name = 'Случайный режим'
vampire = r(-100, 100)
enemy_name = ''.join([chr(c(k)) for i in range(r(9, 21))])
zones_id = {i: ''.join([chr(c(k)) for i in range(r(9, 21))]) for i in range(1, r(3, 6))}
damage = r(1, 500)
player_turn = c([True, False])
hp = r(damage, damage * 10)