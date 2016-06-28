from src.accounting.employee import Employee
from src.accounting.timecard import TimeCard
from src.accounting.paymentmethod import PaymentMethod

HOURS = 8
OVERTIME = 1.5


class HourlyEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, rate, weekly_dues):
        Employee.__init__(employee_id, first_name, last_name, weekly_dues)
        self.__rate = rate
        self.__time_card = []

    def get_hourly_rate(self, rate):
        return self.__rate

    def clock_in(self, date, start_time):
        time_start = TimeCard(self, date, start_time)
        self.__time_card.append(time_start)

    def clock_out(self, date):
        time_card = TimeCard(date)
        time_card.get_date()
        time_card.set_end_time()
        for x in self.__time_card:
            if time_card.get_date == time_card.set_date:
                time_card.set_end_time()

    def pay(self, start_time, end_time, rate):
        val = 0
        for x in self.__time_card:
            if (x.getDate() >= start_time and x.getDate() <= end_time):
                val += x.calculate_daily_pay(self.__rate)
        self.__payment_method(val)
        self.calculate_daily_pay(self, rate)