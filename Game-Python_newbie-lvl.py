player = {'name': input('PlayerName: '), 'attack': int(input('attack: ')), 'heal': int(input('heal: ')),
'health': int(input('health: '))}
monster = {'name':input('MonsterName: '),'attack':int(input('attack: ')),'health':int(input('health: '))}
game_running = True

while game_running == True:

    print ('1) attack turn') 
    print('2) heal')
    print('3) exit game')
    player_choose = input()

    if player_choose == '1':
        print('ROUND ATTACK!!')
        monster['health'] -= player['attack']
        if monster['health']<=0:
            print('YOU WIN!!! THE MONSTER IS ALREAD DEAD!!!')
            game_running = False
        player['health'] -= monster['attack']
        if player['health']<=0:
            print('OH, NO!!! YOU DIED!!!')
            game_running = False
        print('Now the',monster['name'],' has', monster['health'],'health points')
        print('Now,',player['name'],' has', player['health'],'health points')

    elif player_choose == '2':
        print ('EXURA!!!')
        if player['health'] + player['heal'] < 100:
            player['health'] += player['heal']
            print('now you have',player['health'],'health points')
        else : 
            player['health'] = 100
            print('now you have',player['health'],'hps')

    elif player_choose == '3':
        game_running = False