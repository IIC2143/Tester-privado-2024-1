from copy import deepcopy

from src.part_1 import (
    get_all_teams,
    post_team,
    get_team,
    delete_team,
    delete_all_teams,
)

from src.part_2 import (
    get_team_matches,
    post_match,
    patch_match,
    get_matches_by_team,
)

from src.part_3 import (
    post_player,
    get_team_player,
    get_player_top_goals,
    get_player_top_assists,
    get_player_top_cards,
    get_players_from_team,
    delete_worst_team,
)

from data import TEAMS_A, MATCHES_A, PLAYERS_A


def test_3A():
    teams = deepcopy(TEAMS_A[0:4])
    matches = deepcopy(MATCHES_A[0:6])
    players = deepcopy(PLAYERS_A[0:9])

    results = {
        1: delete_all_teams(),
        2: post_team(teams[0]),
        3: post_team(teams[1]),
        4: post_team(teams[2]),
        5: post_team(teams[3]),
        6: post_match(teams[0],teams[2] , matches[1]),
        7: post_match(teams[1], teams[2], matches[2]),
        8: post_match(teams[1], teams[0], matches[3]),
        9: post_match(teams[2], teams[0], matches[4]),
        10: post_match(teams[2], teams[3], matches[5]),
        11: post_player(teams[0], players[0]),
        12: post_player(teams[0], players[1]),
        13: post_player(teams[0], players[2]),
        14: post_player(teams[1], players[3]),
        15: post_player(teams[1], players[4]),
        16: post_player(teams[1], players[5]),
        17: post_player(teams[2], players[6]),
        18: post_player(teams[2], players[7]),
        19: post_player(teams[2], players[8]),
        20: get_team_player(players[0]),
        21: get_team_player(players[3]),
        22: get_team_player(players[6]),
        23: get_player_top_goals(players, 3),
        24: get_player_top_assists(players, 3),
        25: get_player_top_cards(players, 4),
        26: get_players_from_team(teams[0]),
        27: get_players_from_team(teams[1]),
        28: get_players_from_team(teams[2]),
        29: delete_worst_team(teams,matches, players),
        30: get_all_teams(teams),
    }

    return results


if __name__ == '__main__':
    results = test_3A()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
