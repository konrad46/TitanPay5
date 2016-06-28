class Address:

    def __init__(self, street_address, city, state, zip_code):
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code

    def set_street_address(self, street_address):
        self.__street_address = street_address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def get_address(self):
        return self.__street_address + ' ' + self.__city + ', ' + self.__state + ' ' + self.__zip_code