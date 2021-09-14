import logging

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
    logging.info(f"Creating team with players {players}")
    team = Team("el colo", "Santiago", "blanco", players)
    logging.info(f"Team created succesfully with players {players}")
    return team

def create_team_2(players):
    logging.info(f"Creating team with players {players}")
    team = Team("la chile", "Santiago", "azul", players)
    logging.info(f"Team created succesfully with players {players}")
    return team

def create_match():
    logging.info('Starting to create a match')
    team_1 = create_team_1(players_colo())
    team_2 = create_team_2(players_u())
    match =  Match(team_1, team_2)
    logging.info('Match created succesfully')
    return match

def change_in_team(players):
    i = random.randint(0, len(players) - 1)
    players[i] = Player('Marcelo', 'Salas')

def print_match_overview(match):
    logging.info('Printing match overview')
    print('*** Descripción del partido ***')
    print(match)
    logging.info('Match overview printed succesfully')

def print_match_details(match):
    logging.info('Printing match details')
    print('\n*** Detalles del partido ***')
    print(match.team_1)
    print(match.team_2)
    print(f"Fecha: {match.day}")
    logging.info('Match details printed succesfully')

def print_score(match):
    logging.info('Printing match score')
    print('\n *** Marcador ***')
    match.print_scores()
    match.day = "Hoydía"
    match.goal(match.team_1)
    match.print_scores()
    logging.info('Match score printed succesfully')

def print_players(match):
    logging.info('Printing match players')
    print('\n*** Jugadores ***')
    print(match.team_1.players)
    change_in_team(match.team_1.players)
    print(match.team_1.players)
    logging.info('Match players printed succesfully')

def logger_config():
    logging.basicConfig(filename='soccer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


if __name__ == '__main__':
    logger_config()
    logging.info('Program Started')
    match = create_match()
    print_match_overview(match)
    print_match_details(match)
    print_score(match)
    print_players(match)
    logging.info('Program Finished')