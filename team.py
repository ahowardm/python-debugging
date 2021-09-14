class Team:
    def __init__(self, name, city, color, players):
        self.name = name
        self.city = city
        self.color = color
        self.players = players

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value
        return self.__players

    def __str__(self):
        return f"Nombre: {self.name}, Ciudad: {self.city}, Color: {self.color}"
        