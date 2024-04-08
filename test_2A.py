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

from data import TEAMS_A, MATCHES_A


def test_2A():
    teams = deepcopy(TEAMS_A[0:4])
    matches = deepcopy(MATCHES_A[0:6])

    results = {
        1: delete_all_teams(),
        2: post_team(teams[0]),
        3: post_team(teams[1]),
        4: post_team(teams[2]),
        5: post_team(teams[3]),
        6: get_all_teams(teams),
        7: post_match(teams[0], teams[1], matches[0]),
        8: post_match(teams[0],teams[2], matches[1]),
        9: post_match(teams[1], teams[0], matches[2]),
        10: post_match(teams[1], teams[3], matches[3]),
        11: post_match(teams[2], teams[0], matches[4]),
        12: post_match(teams[2], teams[3], matches[5]),
        13: get_team_matches(teams[0]),
        14: get_team_matches(teams[1]),
        15: get_team_matches(teams[2]),
        16: patch_match(matches[0], {'match': {'state': True, 'result': "3-0"}}),
        17: get_team(teams[0]),
        18: get_team(teams[1]),
        19: get_team(teams[2]),
        20: get_team(teams[3]),
    }

    return results


if __name__ == '__main__':
    results = test_2A()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
