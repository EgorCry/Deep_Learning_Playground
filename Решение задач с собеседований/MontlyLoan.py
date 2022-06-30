"""
Задана процентная ставка по кредиту (X% годовых), срок кредитования (N месяцев) и
сумма кредита (M рублей).
Необходимо рассчитать размер аннуитетного ежемесячного платежа.
"""


def check_month(mperc, yperc):
    msum = 1 + mperc / 100
    ysum = 1 + yperc / 100
    return msum ** 12 >= ysum


def float_binary_search(l, r, eps, check, params):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, params):
            r = m
        else:
            l = m
    return l


def check_credit(mpay, params):
    periods, creditsum, mperc = params
    for i in range(periods):
        percpay = creditsum * (mperc / 100)
        creditsum -= mpay - percpay
    return creditsum <= 0


def credit_binary_search(l, r, eps, check, params):
    while l + eps < r:
        m =(l + r) / 2
        if check(m, params):
            r = m
        else:
            l = m
    return l


eps = 0.01
x = 6
m = 12_000
n = 36
mperc = float_binary_search(0, x, eps, check_month, x)
monthly_pay = credit_binary_search(0, m, eps, check_credit, (n, m, mperc))
print(monthly_pay)
