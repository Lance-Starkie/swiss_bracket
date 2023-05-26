import random as ran
from copy import deepcopy 

player_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
player_count = 0
player_scores = [[]]
new_player_scores = [[]]
game_history = set()

for i in player_list:
    player_scores[0].append(i)
    player_count += 1
for round_i in range(max(5,len(player_list)-10)):
    print("Round "+str(round_i+1))
    new_player_scores.append([])
    top_three = [0]
    for j in range(int(player_count/2)):
        battle = ['','']
        while len(player_scores[-1]) == 0:
            del player_scores[-1]
        battle_scores = [len(player_scores)-1,0]
        battle[0] = player_scores[-1].pop(0)
        #print(list(''.join([''.join(player_i) for player_i in player_scores])))
        #print(list(''.join([''.join([str(score_i) for i in players_i]) for players_i, score_i in zip(player_scores,range(len(player_scores)))])))
        e = list(zip(
            list(range(len(player_scores))),
            list([''.join(player_i) for player_i in player_scores])))
        e = sorted(e,key=lambda a: a[0])
        found_player = False
        for score_j,players in e[::-1]:
            if (score_j > min(top_three) or len(top_three) < min(round_i,2)) and not score_j in top_three and len(players) != 0:
                if top_three == [0]:
                    top_three = []
                top_three.append(score_j)
                top_three.sort()
                top_three = top_three[0:3]
                print(top_three)
        for score_j,players in e[::-1]:
            #print(player_scores)
            #print("--")
            #print("Checking " + player_j+score_j)

            for player_j in players:
                battle[1] = player_j
                battle_scores[1] = (int(score_j))
                if ''.join(sorted(battle)) in game_history:
                    pass
                elif battle[1] in player_scores[battle_scores[1]]:# and abs(battle_scores[0]-battle_scores[1]) < 3:
                    found_player = True
                    player_scores[battle_scores[1]].remove(battle[1][-1])
                    game_history.add(''.join(sorted(battle)))
                    if complete := max(battle_scores) > min(top_three) and min(top_three) != 0:
                        result = ran.randint(-1,ran.randint(0,ran.randint(2,4)))
                    else:
                        result = ran.randint(0,ran.randint(1,ran.randint(2,3)))
                    if ''.join(sorted(battle)) != ''.join(battle):
                        result = 3 - result
                    #print(battle_scores)
                    battle_scores[0] += 3 - result
                    battle_scores[1] += result
                    for i in range(max(0,max(battle_scores)+1-len(new_player_scores))):
                        new_player_scores.append([])
                    new_player_scores[battle_scores[0]].append(battle[0][-1])
                    new_player_scores[battle_scores[1]].append(battle[1][-1])
                    if complete:
                        print(battle[0][-1]+" vs. "+battle[1][-1]+" "+["3-0","3-1","3-2","2-3","1-3","0-3"][result+1])
                    else:
                        print(battle[0][-1]+" vs. "+battle[1][-1]+" "+["2-0","2-1","1-2","0-2"][result])
                if found_player:
                    break
            if found_player:
                break
        if not found_player:
            while len(player_scores[-1]) == 0:
                del player_scores[-1]
            battle_scores[1] = len(player_scores) -1
            battle[1] = player_scores[-1].pop(0)
            if complete := max(battle_scores) > min(top_three) and min(top_three) != 0:
                result = ran.randint(-1,ran.randint(0,ran.randint(2,4)))
            else:
                result = ran.randint(0,ran.randint(1,ran.randint(2,3)))
            #print(battle_scores)
            if complete := max(battle_scores) > min(top_three) and min(top_three) != 0:
                result = ran.randint(-1,ran.randint(0,ran.randint(2,4)))
            else:
                result = ran.randint(0,ran.randint(1,ran.randint(2,3)))
            if ''.join(sorted(battle)) != ''.join(battle):
                result = 3 - result
            #print(battle_scores)
            battle_scores[0] += 3 - result
            battle_scores[1] += result
            for i in range(max(0,max(battle_scores)+1-len(new_player_scores))):
                new_player_scores.append([])
            new_player_scores[battle_scores[0]].append(battle[0])
            new_player_scores[battle_scores[1]].append(battle[1])
            if complete:
                print(battle[0][-1]+" vs. "+battle[1][-1]+" "+["3-0","3-1","3-2","2-3","1-3","0-3"][result+1]+[""," Rematch"][int(''.join(sorted(battle)) in game_history)])
            else:
                print(battle[0][-1]+" vs. "+battle[1][-1]+" "+["2-0","2-1","1-2","0-2"][result]+[""," Rematch"][int(''.join(sorted(battle)) in game_history)])
            game_history.add(''.join(sorted(battle)))
    player_scores = deepcopy(new_player_scores)
    new_player_scores = deepcopy(list([([]) for i in new_player_scores]))
    for i in player_scores[::-1]:
        if len(i) > 0:
            print(", ".join(i))
        #s = ''.join(sorted(s))
input()
    
