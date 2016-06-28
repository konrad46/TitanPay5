class TimeCard:
    def __init__(self, date, start, end):
        self.__date = date
        self.__start_time = start
        self.__end_time = end

    def set_date(self, date):
        self.__date = date

    def set_start_time(self, start):
        self.__start_time = start

    def set_end_time(self, end):
        self.__end_time = end

    def calculate_daily_pay(self, rate):
        hours = self.__end_time - self.__start_time

        if hours <= 8:
            return hours * rate
        if hours > 8:
            return (rate * 8) + (1.5*rate * (hours - 8))