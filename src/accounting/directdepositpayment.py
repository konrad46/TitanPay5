from src.accounting.paymentmethod import PaymentMethod


class DirectDepositPayment(PaymentMethod):
    def __init__(self, pay):
        self.__pay = pay

    def pay(self, val, employee):
        print('$', format(val, ',.2f'), 'is being directly deposited in ', employee.get_full_name(),"'s account.")