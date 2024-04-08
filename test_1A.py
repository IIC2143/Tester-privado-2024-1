from copy import deepcopy

from src.part_1 import (
    get_all_teams,
    post_team,
    get_team,
    delete_team,
    delete_all_teams,
)

from data import TEAMS_A


def test_1A():
    teams = deepcopy(TEAMS_A[0:3])

    results = {
        1: delete_all_teams(),
        2: post_team(teams[0]),
        3: post_team(teams[1]),
        4: post_team(teams[2]),
        5: get_all_teams(teams),
        6: get_team(teams[0]),
        7: get_team(teams[1]),
        8: get_team(teams[2]),
        9: delete_team(teams, teams[0]),
        10: get_all_teams(teams),
    }

    return results


if __name__ == '__main__':
    results = test_1A()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
