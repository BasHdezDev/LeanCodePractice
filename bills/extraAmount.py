import calculator


class ModelExtraAmount:
    def __init__(self, amount: float, interest: float, payment: int):
        self.amount = amount
        self.interest = interest
        self.payment = payment

    def amortization_extra_amount(self, number_amount_to_pay: int, extrapayment: float) -> list:
        amount_value = calculator.monthly_bills(self.amount, self.interest, self.payment)
        interest_x = self.interest / 100
        balance = self.amount
        amortization_table = [["Cuota", "balance", "Pago interés", "Abono capital"],
                              ["#", amount_value, self.interest, self.amount]]
        if self.payment == 1:
            amount_number = 1
            interest_ = (self.interest * balance) / 100
            payment_stock = amount_value - interest_
            row = [amount_number, balance, interest_, payment_stock]
            amortization_table.append(row)
        else:
            for cuota in range(1, self.payment + 1):
                amount_number = cuota
                interes = interest_x * balance
                payment_stock = amount_value - interes

                if number_amount_to_pay == amount_number:
                    cuota_real_a_abonar = extrapayment
                else:
                    cuota_real_a_abonar = amount_value
                    if balance <= 0:
                        payment_stock += balance + interes
                        balance = 0
                        break

                payment_stock = cuota_real_a_abonar - interes
                balance -= payment_stock

                if balance < 0:
                    payment_stock += balance + interes
                    balance = 0

                row = [amount_number, balance, interes, payment_stock]
                amortization_table.append(row)
                if balance < payment_stock:
                    payment_stock = balance

        return amortization_table


x = ModelExtraAmount(850000, 3.40, 24)

f = x.amortization_extra_amount(5, 90000)

print(f)