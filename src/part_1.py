from requests import get, post, delete
from .models import Team
from .utils import __show, __skip_exception


BASE_URL = 'http://localhost:3000'


@__skip_exception
def get_all_teams(teams: list[Team], *, show=False):
    url = f'{BASE_URL}/teams'
    response = get(url)
    body = response.json()

    

    if show:
        __show(body, teams)

    if len(body) == len(teams):
        content_match = all(
            team.is_valid(body[i])
            for i, team in enumerate(teams)
        )

        return content_match

    return False


@__skip_exception
def post_team(team: Team, *, show=False):
    url = f'{BASE_URL}/teams'
    data = team.data()
    response = post(url, json=data)
    body = response.json()

    if show:
        __show(body, team)

    if response.status_code >= 400:
        return False

    if team.is_valid(body, is_new=True):
        team.id = body['id']

        return True

    return False


@__skip_exception
def get_team(team: Team, *, show=False):
    url = f'{BASE_URL}/teams/{team.id}'
    response = get(url)
    body = response.json()

    if show:
        __show(body, team)

    return team.is_valid(body)


@__skip_exception
def delete_team(teams: list[Team], team: Team, *, show=False):
    url = f'{BASE_URL}/teams/{team.id}'
    response = delete(url)
    body = response.json()

    if show:
        __show(body, {})

    if body == {}:
        teams.remove(team)

        return True

    return False


@__skip_exception
def delete_all_teams(*, show=False):
    url = f'{BASE_URL}/teams'
    response = delete(url)
    body = response.json()

    if show:
        __show(body, [])

    return body == []


# @__skip_exception
# def get_city(teams: list[Team], *, show=False):
#     url = f'{BASE_URL}/team/city'
#     response = get(url)
#     body = response.json()


#     if show:
#         __show(body, team.city)

#     if len(body) == len(team.city):
#         content_match = all(
#             team.city[i].is_valid(body[i])
#             for i in range(len(team.city))
#         )

#         return content_match

#     return False
