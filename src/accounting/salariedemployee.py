from src.accounting.employee import Employee
from src.accounting.receipt import Receipt


class SalariedEmployee(Employee):

    def __init__(self, employee_id, first_name, last_name, salary, commission_rate, weekly_dues):
        Employee.__init__(employee_id, first_name, last_name, weekly_dues)
        self.__salary = salary
        self.__commission_rate = commission_rate
        self.__receipts = []

    def make_sale(self, date, amt):
        sale_amt = Receipt(self, date, amt)
        self.__receipts.append(sale_amt)

    def pay(self, start_time, end_time, commission_rate):
        total_amt = 0
        for amt in self.__receipts:
            total_amt += amt
        commission = total_amt * commission_rate
        return commission
