from src.accounting import hourlyemployee
from src.accounting import salariedemployee


def run_payroll():
    hr_emp_hand = open('hourly_employees.csv', 'r')
    count = 0
    hr_employee_dict = {}
    for line in hr_emp_hand:

        if count != 0:
            emp = line.split(',')
            emp[4] = emp[4].strip()
            emp[5] = emp[5].strip()
            if emp[4] == '-':
                emp[4] = 0
            employee = hourlyemployee.HourlyEmployee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], '25 Waterview Dr', 'Westford', 'MA', '01886')
            hr_employee_dict[emp[0]] = employee

        count += 1

    hr_emp_hand.close()

    tc_hand = open('timecards.csv', 'r')
    count = 0
    for line in tc_hand:

        if count != 0:
            tc = line.split(',')
            tc[3] = tc[3].strip()

            hr_employee_dict[tc[0]].clockin(tc[3], tc[1])
            hr_employee_dict[tc[0]].clockout(tc[3], tc[2])

        count += 1

    tc_hand.close()

    for emp in hr_employee_dict:
        hr_employee_dict[emp].calc_pay()

    sal_emp_hand = open('salaried_employees.csv', 'r')
    count = 0
    sal_employee_dict = {}
    for line in sal_emp_hand:

        if count != 0:
            emp = line.split(',')
            emp[5] = emp[5].strip()
            emp[6] = emp[6].strip()
            if emp[5] == '-':
                emp[5] = 0
            employee = salariedemployee.SalariedEmployee(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], '25 Waterview Dr',
                                                          'Westford', 'MA', '01886')
            sal_employee_dict[emp[0]] = employee

        count += 1

    sal_emp_hand.close()

    rec_hand = open('receipts.csv', 'r')
    count = 0
    for line in rec_hand:

        if count != 0:
            comma_count = 0
            line2 = ''
            for cha in range(0, len(line)):
                if line[cha] == ',':
                    comma_count += 1
                    if comma_count > 5:
                        continue
                    else:
                        line2 = line2 + ','
                else:
                    line2 = line2 + line[cha]

            rec_data = line2.split(',')
            total = rec_data[5].strip()
            total = total.strip('"')
            total = total.strip()
            totalf = float(total)
            sal_employee_dict[rec_data[0]].create_receipt(rec_data[0], rec_data[1], rec_data[2], int(rec_data[3]), float(rec_data[4]),
                                                          totalf)
        count += 1
    rec_hand.close()

    for emp in sal_employee_dict:
        sal_employee_dict[emp].calc_pay()