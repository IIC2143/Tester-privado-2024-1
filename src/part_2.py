from requests import get, post, patch
from .utils import __show, __skip_exception
from copy import deepcopy


BASE_URL = 'http://localhost:3000'


@__skip_exception
def get_team_matches(team, *, show=False):
    url = f'{BASE_URL}/teams/{team.id}/matches'
    response = get(url)
    body = response.json()

    if show:
        __show(body, team.matches)

    if len(body) == len(team.matches):
        content_match = all(
            match.is_valid(body[i])
            for i, match in enumerate(team.matches)
        )

        return content_match

    return False


@__skip_exception
def post_match(teamA, teamB, match, *, show=False):
    url = f'{BASE_URL}/matches'
    match.teamA = teamA.id
    match.teamB = teamB.id
    data = match.data()
    response = post(url, json=data)
    body = response.json()

    if show:
        __show(body, match)

    if response.status_code >= 400:
        return False
    

    if match.is_valid(body, is_new=True):
        teamA.matches.append(match)
        teamB.matches.append(match)
        match.id = body['id']
        match.teamA = body['teamA']
        match.teamB = body['teamB']
        match.state = body['state']
        match.result = body['result']

        return True

    return False


@__skip_exception
def patch_match(match, new_match_data, *, show=False):
    url = f'{BASE_URL}/matches/{match.id}'
    data = new_match_data

    response = patch(url, json=data)
    

    body = response.json()

    if response.status_code >= 400:
        return False

    match_copy = deepcopy(match)
    match_copy.update(new_match_data)

    if show:
        __show(body, match_copy)


    if match_copy.is_valid(body):
        match.update(new_match_data)

        return True

    return False


@__skip_exception
def get_matches_by_team(matches, team, *, show=False):
    url = f'{BASE_URL}/matches/{team.name}'
    
    response = get(url)
    body = response.json()

    filtered_matches = [
        match
        for match in matches
        if team.id == match.teamA or team.id == match.teamB
    ]


    if show:
        __show(body, filtered_matches)
    if len(body) == len(filtered_matches):
        content_match = all(
            match.is_valid(body[i])
            for i, match in enumerate(filtered_matches)
        )

        return content_match

    return False
