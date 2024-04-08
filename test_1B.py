from copy import deepcopy

from src.part_1 import (
    get_all_teams,
    post_team,
    get_team,
    delete_team,
    delete_all_teams,
)

from data import TEAMS_B, WRONG_TEAMS


def test_1B():
    teams = deepcopy(TEAMS_B[0:3])
    bad_teams = deepcopy(WRONG_TEAMS[0:2])

    results = {
        1: delete_all_teams(),
        2: post_team(teams[0]),
        3: post_team(teams[1]),
        4: not post_team(bad_teams[0]),
        5: post_team(teams[2]),
        6: not post_team(bad_teams[1]),
        7: get_team(teams[1]),
        8: get_team(teams[2]),
        9: delete_team(teams, teams[0]),
        10: get_all_teams(teams),
    }

    return results


if __name__ == '__main__':
    results = test_1B()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
