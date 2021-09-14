import logging

class Match:
    def __init__(self, team_1, team_2):
        logging.info(f"Starting the creation of a match with teams {team_1} and {team_2}")
        self.team_1 = team_1
        self.team_2 = team_2
        self.set_initial_scores()
        self.__day = None
        logging.info(f"Match created succesfully")

    def set_initial_scores(self):
        self.__score_team_1 = 0
        self.__score_team_2 = 0
        logging.info('Initial scores set')

    @property
    def team_1(self):
        logging.info('Attempting to get team_1')
        return self.__team_1

    @team_1.setter
    def team_1(self, value):
        logging.info('Attempting to set team_1')
        self.__team_1 = value
        logging.info(f"team_1 set to {value}")

    @property
    def team_2(self):
        logging.info('Attempting to get team_2')
        return self.__team_2

    @team_2.setter
    def team_2(self, value):
        logging.info('Attempting to set team_1')
        self.__team_2 = value
        logging.info(f"team_2 set to {value}")

    @property
    def day(self):
        logging.info('Attempting to get day')
        return self.__day

    @day.setter
    def day(self, value):
        logging.info('Attempting to set day')
        if self.day == None:
            self.__day = value
            logging.info(f"day set to {value}")
        else:
            logging.error(f"Day already has a value ({self.day}), and cannot be changed")
            raise ValueError("La fecha ya fue fijada")

    @property
    def score_team_1(self):
        logging.info('Attempting to get the score from team_1')
        return self.__score_team_1

    @property
    def score_team_2(self):
        logging.info('Attempting to get the score from team_2')
        return self.__score_team_2

    def goal(self, team):
        if self.__day == None:
            logging.error('There cannot be goals without specifying a date for the match')
            raise ValueError("No pueden haber goles sin fecha definida")
        if self.team_1 == team:
            logging.info('Adding a goal for team_1')
            self.__score_team_1 += 1
        elif self.team_2 == team:
            logging.info('Adding a goal for team_2')
            self.__score_team_2 += 1

    def print_scores(self):
        logging.info(f"Printing scores for {self}")
        print(f"{self.team_1.name}: {self.score_team_1}\n{self.team_2.name}: {self.score_team_2}")

    def __str__(self):
        return f"{self.day}: {self.team_1.name} v/s {self.team_2.name}"