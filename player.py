class Player:
    def __init__(self, first_name, last_name):
        self.create_attributes()
        self.first_name = first_name
        self.last_name = last_name

    def create_attributes(self):
        self.__first_name = None
        self.__last_name = None

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if self.first_name == None:
            self.__first_name = value
            return self.__first_name
        else:
            raise ValueError("No se puede cambiar el nombre")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if self.last_name == None:
            self.__last_name = value
            return self.__last_name
        else:
            raise ValueError("No se puede cambiar el apellido")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return self.__str__()