from src.accounting.paymentmethod import PaymentMethod
from src.accounting.timecard import TimeCard


class PickupPayment:
    def pay(self, employee):
        amt = TimeCard.calculate_daily_pay()
        print("A check for " + amt + "is waiting for " + employee.get_full_name() + "at the PostMaster.")