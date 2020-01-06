import time
from Member import Member
from itertools import cycle

member0 = Member(0)
member0.right = member0
member0.left = member0

def move(num: int, players_score: dict, player: int, current: Member, member_list: list) -> tuple:
    new_member = Member(num)
    if num % 23 == 0:
        players_score[player] += num
        seventh = current.n_neighbor(False, 7)
        players_score[player] += seventh.value
        current = seventh.right
        seventh.remove()
    else:
        current.n_neighbor(True, 2).left = new_member
        new_member.right = current.n_neighbor(True, 2)
        current.n_neighbor(True, 1).right = new_member
        new_member.left = current.right
        current = new_member
        member_list.append(new_member)
    return (players_score, current, member_list)
    
def solution(player_num: int, last_marble: int):
    member0 = Member(0)
    member0.left = member0
    member0.right = member0
    member_list = [member0]
    players = cycle(range(1, player_num + 1))
    next(players)
    players_score = {}
    for each in range(1, player_num + 1):
        players_score[each] = 0
    players_score, current, member_list = move(1, players_score, 1, member0, member_list)
    index = 2
    for player in players:
        if index > last_marble:
            break
        players_score, current, member_list = move(index, players_score, player, current, member_list)
        index += 1
    return (players_score[max(players_score, key=lambda key: players_score[key])])

passed = time.time()
for each in range(0, 400):
    print(solution(477, each))