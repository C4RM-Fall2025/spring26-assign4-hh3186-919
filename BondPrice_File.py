
def getBondPrice(y, face, couponRate, m, ppy=1):
    coupon = face * couponRate / ppy
    price = 0
    for t in range(1, m * ppy + 1):
        price += coupon / (1 + y/ppy) ** t
    price += face / (1 + y/ppy) ** (m * ppy)
    return round(price)
