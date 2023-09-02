import calculator


class ModelCalculator:
    def __init__(self, amount: float, interest: float, payment: int):
        self.amount = amount
        self.interest = interest
        self.payment = payment

    def amortization(self) -> list:
        amount_value = calculator.monthly_bills(self.amount, self.interest, self.payment)
        interest_x = self.interest / 100
        balance = self.amount
        amortization_table = [["Cuota", "balance", "Pago interés", "Abono capital"],
                              ["#", amount_value, self.interest, self.amount]]
        if self.payment == 1:
            self.interest = 0

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
                balance = balance - payment_stock

                if self.payment == 1:
                    payment_stock = 0
                    interes = 0

                if interes >= balance:
                    balance = payment_stock + interes
                    payment_stock = 0

                if balance <= 0:
                    balance = 0

                row = [amount_number, balance, interes, payment_stock]
                amortization_table.append(row)

        return amortization_table

