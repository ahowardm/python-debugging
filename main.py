from numpy import random

from match import Match
from player import Player
from team import Team

def players_colo():
    players = []
    players.append(Player('Pablo', 'Solari'))
    players.append(Player('Luciano', 'Arriagada'))
    players.append(Player('Maximiliano', 'Falcon'))
    players.append(Player('Pablo', 'Solari'))
    return players

def players_u():
    players = []
    players.append(Player('Junior', 'Fernandez'))
    players.append(Player('Pablo', 'Aranguiz'))
    players.append(Player('Gonzalo', 'Espinoza'))
    players.append(Player('Anderson', 'Contreras'))
    return players

def create_team_1(players):
    return Team("el colo", "Santiago", "blanco", players)

def create_team_2(players):
    return Team("la chile", "Santiago", "azul", players)

def create_match():
    # players_colo = players_colo()
    # players_u = players_u()
    team_1 = create_team_1(players_colo())
    team_2 = create_team_2(players_u())
    return Match(team_1, team_2)

def change_in_team(players):
    i = random.randint(0, len(players) - 1)
    players[i] = Player('Marcelo', 'Salas')

def print_match_overview(match):
    print('*** Descripción del partido ***')
    print(match)

def print_match_details(match):
    print('\n*** Detalles del partido ***')
    print(match.team_1)
    print(match.team_2)
    print(f"Fecha: {match.day}")

def print_score(match):
    print('\n *** Marcador ***')
    match.print_scores()
    match.day = "Hoydía"
    match.goal(match.team_1)
    match.print_scores()

def print_players(match):
    print('\n*** Jugadores ***')
    print(match.team_1.players)
    change_in_team(match.team_1.players)
    print(match.team_1.players)


match = create_match()
print_match_overview(match)
print_match_details(match)
print_score(match)
print_players(match)