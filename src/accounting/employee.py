from src.accounting.paymentmethod import PaymentMethod


class Employee:
    def __init__(self, employee, first_name, last_name, weekly_dues, pay_method):
        self.__employee_id = employee
        self.__first_name = first_name
        self.__last_name = last_name
        self.__weekly_dues = weekly_dues
        self.__pay_method = pay_method

    def set_employee(self, employee):
        self.__employee_id = employee

    def set_first(self, first_name):
        self.__first_name = first_name

    def set_last(self, last_name):
        self.__last_name = last_name

    def get_weekly_dues(self):
        return self.__weekly_dues

    def get_pay_method(self):
        return self.__pay_method

    def get_full_name(self):
        print("Employee: " + self.__first_name + ", " + self.__last_name)