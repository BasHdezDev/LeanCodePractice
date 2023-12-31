import cases_tests


def monthly_bills(amount, interest, payments) -> float:
    p = interest/100
    if amount == 0:
        raise cases_tests.ZeroAmount
    elif interest*12 > 100:
        raise cases_tests.Usura
    elif payments <= 0:
        raise cases_tests.NegativePayment
    elif payments == 1:
        return amount
    elif interest == 0:
        return amount/payments
    else:
        return (amount * p)/(1 - (1 + p)**(-payments))


def total_interest(self) -> float:
    amount_value = monthly_bills(self.amount, self.interest, self.payment)
    total = (amount_value * self.payment) - self.amount
    return total
