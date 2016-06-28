import tkinter
import src.accounting


class TopGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('300x250+500+200')

        self.frame = tkinter.Frame(self.main_window)

        self.labelspace = tkinter.Label(self.frame, text='')
        self.label = tkinter.Label(self.frame, text='Main Menu')
        self.labelspace2 = tkinter.Label(self.frame, text='')

        self.new_emp_button = tkinter.Button(self.frame, width='25', bg='white', text='New employee')
        self.view_timecards_button = tkinter.Button(self.frame, width='25', bg='white', text='View timecards')
        self.view_pay_rate_button = tkinter.Button(self.frame, width='25', bg='white', text='View salary info')
        self.view_sales_data_button = tkinter.Button(self.frame, width='25', bg='white', text='View sales info')
        self.change_pay_meth_button = tkinter.Button(self.frame, width='25', bg='white', text='Change payment method')
        self.process_payroll_button = tkinter.Button(self.frame, width='25', bg='white', text='Process payroll',
                                                     command=self.process_payroll_gui)

        self.frame.pack()
        self.labelspace.pack()
        self.label.pack()
        self.labelspace2.pack()
        self.new_emp_button.pack()
        self.view_timecards_button.pack()
        self.view_pay_rate_button.pack()
        self.view_sales_data_button.pack()
        self.change_pay_meth_button.pack()
        self.process_payroll_button.pack()

        tkinter.mainloop()

    def process_payroll_gui(self):
        self.additional_window = tkinter.Toplevel()
        self.additional_window.geometry('300x250+500+200')

        self.run_payroll_button = tkinter.Button(self.additional_window, width='25', bg='white', text='Run payroll',
                                                 command=src.accounting.runpayroll.run_payroll)
        self.run_payroll_button.pack()
        self.run_payroll_button.place(x=60, y=80)


topgui = TopGUI()