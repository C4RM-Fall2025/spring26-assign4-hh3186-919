def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    bondPrice = 0

    m = len(times)

    for t, y in zip(times, yc):
        cf = coupon
        if t == times[m - 1]:
            cf = cf + face

        pvm = 1 / ((1 + y) ** t)
        pvcf = cf * pvm
        bondPrice = bondPrice + pvcf

    return bondPrice
