from requests import get, post, delete
from copy import deepcopy
from .utils import __show, __skip_exception


BASE_URL = 'http://localhost:3000'


@__skip_exception
def post_player(team, player, *, show=False):
    url = f'{BASE_URL}/players/{team.id}'
    data = player.data()
    response = post(url, json=data)
    body = response.json()

    if show:
        __show(body, player)
    

    if player.is_valid(body, is_new=True):
        team.players.append(player)
        player.id = body['id']
        player.name = body['name']
        player.goal = body['goal']
        player.assist = body['assist']
        player.card = body['card']
        player.team = team
        player.team_id = team.id

        return True

    return False


@__skip_exception
def get_team_player(player, *, show=False):
    url = f'{BASE_URL}/players/{player.id}/team'
    response = get(url)
    body = response.json()

    if show:
        __show(body, player.team)


    if body['id'] == player.team.id:
        content_match = player.team.is_valid(body)

        return content_match

    return False


@__skip_exception
def get_player_top_goals(player, quantity, *, show=False):
    url = f'{BASE_URL}/players/topGoals/{quantity}'
    response = get(url)
    body = response.json()

    players_copy = deepcopy(player)

    sorted_player = sorted(players_copy, key=lambda player: player.goal, reverse=True)
    selected = sorted_player[:quantity]

    if show:
        __show(body, selected)

    if len(selected) == len(body) == quantity:
        return all(
            player.is_valid(body[i])
            for i, player in enumerate(selected)
        )

    return False

@__skip_exception
def get_player_top_cards(player, quantity, *, show=False):
    url = f'{BASE_URL}/players/topCards/{quantity}'
    response = get(url)
    body = response.json()
    players_copy = deepcopy(player)

    sorted_player = sorted(players_copy, key=lambda player: player.card, reverse=False)

    selected = sorted_player[:quantity]

    if show:
        __show(body, selected)

    if len(selected) == len(body) == quantity:
    
        return all(
            player.is_valid(body[i])
            for i, player in enumerate(selected)
        )

    return False

@__skip_exception
def get_player_top_assists(player, quantity, *, show=False):
    url = f'{BASE_URL}/players/topAssists/{quantity}'
    response = get(url)
    body = response.json()

    players_copy = deepcopy(player)

    sorted_player = sorted(players_copy, key=lambda player: player.assist/(player.assist+player.goal), reverse=True)
    selected = sorted_player[:quantity]

    if show:
        __show(body, selected)

    if len(selected) == len(body) == quantity:
        return all(
            player.is_valid(body[i])
            for i, player in enumerate(selected)
        )

    return False

#esto lo podriamos hacer con matches pero tendriamos que especificar si es el team A o B
@__skip_exception
def get_players_from_team(team, *, show=False): 
    url = f'{BASE_URL}/teams/{team.id}/players'
    response = get(url)
    body = response.json()

    if show:
        __show(body, team.players)

    if len(body) == len(team.players):
        content_match = all(
            player.is_valid(body[i])
            for i, player in enumerate(team.players)
        )

        return content_match
    
    return False


@__skip_exception
def delete_worst_team(teams, matches, players, *, show=False): #B
    url = f'{BASE_URL}/teams/matches/low'
    response = delete(url)
    body = response.json()


    lowest_team = min(teams, key=lambda team: (team.calculate_points(), 1 - len(team.matches)))


    if show:
        __show(body, lowest_team)

    if lowest_team.is_valid(body):

        for match in lowest_team.matches:
            # delete the match in the  other team that is playing
 
            if match.teamA == lowest_team.id:

                for team in teams:
                    if team.id == match.teamB:
                        team.matches.remove(match)

            if match.teamB == lowest_team.id:
  
                for team in teams:

                    if team.id == match.teamA:
                        team.matches.remove(match)

            matches.remove(match)

        for player in lowest_team.players:
            # ranking.destroy()
            players.remove(player)


        lowest_team.destroy()

        teams.remove(lowest_team)


        return True

    return False
        

#en caso de hacer una request de tabla de posicion
def create_table_of_positions(teams):
    table = sorted(teams, key=lambda team: team.points, reverse=True)