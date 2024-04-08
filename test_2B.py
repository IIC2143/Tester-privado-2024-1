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

from data import TEAMS_B, MATCHES_B, WRONG_MATCHES


def test_2B():
    teams = deepcopy(TEAMS_B[0:3])
    matches = deepcopy(MATCHES_B[0:6])
    bad_matchs = deepcopy(WRONG_MATCHES)

    results = {
        1: delete_all_teams(),
        2: post_team(teams[0]),
        3: post_team(teams[1]),
        4: post_team(teams[2]),
        5: get_all_teams(teams),
        6: post_match(teams[0],teams[1], matches[0]),
        7: post_match(teams[0],teams[2], matches[1]),
        8: post_match(teams[1], teams[0], matches[2]),
        9: post_match(teams[1],teams[2], matches[3]),
        10: post_match(teams[2], teams[1], matches[4]),
        11: post_match(teams[2],teams[0], matches[5]),
        12: get_team_matches(teams[0]),
        13: get_team_matches(teams[1]),
        14: get_team_matches(teams[2]),
        15: get_matches_by_team(matches, teams[0]),
        16: get_matches_by_team(matches, teams[1]),
        17: get_matches_by_team(matches, teams[2]),
        18: patch_match(matches[0], {'match': {'state': True, 'result': "3-0"}}),
        19: get_team(teams[0]),
        20: get_team(teams[1]),
    }

    return results


if __name__ == '__main__':
    results = test_2B()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
