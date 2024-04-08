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

from data import TEAMS_A, MATCHES_B, WRONG_MATCHES, WRONG_TEAMS


def test_2C():
    teams = deepcopy(TEAMS_A[0:7])
    bad_teams = deepcopy(WRONG_TEAMS[0:4])
    matches = deepcopy(MATCHES_B[0:6])
    bad_matches = deepcopy(WRONG_MATCHES)

    results = {
        1: delete_all_teams(),
        2: post_team(teams[0]),
        3: post_team(teams[1]),
        4: post_team(teams[2]),
        5: get_all_teams(teams[0:3]),
        6: post_match(teams[0],teams[1], matches[0]),
        7: post_match(teams[0], teams[2], matches[1]),
        8: post_match(teams[1], teams[2], matches[2]),
        9: post_match(teams[1], teams[2], matches[3]),
        10: post_match(teams[2], teams[0], matches[4]),
        11: post_match(teams[2], teams[1], matches[5]),
        12: get_team_matches(teams[0]),
        13: get_team_matches(teams[1]),
        14: get_team_matches(teams[2]),
        15: get_matches_by_team(matches, teams[0]),
        16: get_matches_by_team(matches, teams[1]),
        17: delete_team(teams, teams[0]),
        18: not post_match(teams[1], teams[5], bad_matches[0]),
        19: not patch_match(matches[4], {'match': {'state': True, 'result': '4-0'}}),
        20: not patch_match(matches[0], {'match': {'teamB': teams[5]}}),
        21: not get_all_teams(bad_teams),
        22: not get_team(bad_teams[0]),
        23: not post_match(bad_teams[0], bad_teams[3], bad_matches[0]),
        24: not get_team_matches(bad_teams[0]),
        25: not get_matches_by_team(bad_matches, ''),
        26: not delete_team(bad_teams, bad_teams[0]),
        27: not patch_match(bad_matches[0], {'match': {'teamA': bad_teams[0]}}),
        28: not patch_match(bad_matches[0], {'match': {'teamB': bad_teams[2]}}),
        29: delete_team(teams, teams[1]),
        30: not get_all_teams(teams),
    }

    return results


if __name__ == '__main__':
    results = test_2C()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
