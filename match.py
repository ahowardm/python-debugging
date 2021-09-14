class Match:
    def __init__(self, team_1, team_2):
        self.team_1 = team_1
        self.team_2 = team_2
        self.set_initial_scores()
        self.__day = None

    def set_initial_scores(self):
        self.__score_team_1 = 0
        self.__score_team_2 = 0

    @property
    def team_1(self):
        return self.__team_1

    @team_1.setter
    def team_1(self, value):
        self.__team_1 = value

    @property
    def team_2(self):
        return self.__team_2

    @team_2.setter
    def team_2(self, value):
        self.__team_2 = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if self.day == None:
            self.__day = value
        else:
            raise ValueError("La fecha ya fue fijada")

    @property
    def score_team_1(self):
        return self.__score_team_1

    @property
    def score_team_2(self):
        return self.__score_team_2

    def goal(self, team):
        if self.__day == None:
            raise ValueError("No pueden haber goles sin fecha definida")
        if self.team_1 == team:
            self.__score_team_1 += 1
        elif self.team_2 == team:
            self.__score_team_2 += 1

    def print_scores(self):
        print(f"{self.team_1.name}: {self.score_team_1}\n{self.team_2.name}: {self.score_team_2}")

    def __str__(self):
        return f"{self.day}: {self.team_1.name} v/s {self.team_2.name}"