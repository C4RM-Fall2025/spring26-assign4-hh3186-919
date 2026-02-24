def getBondPrice(y, face, couponRate, m, ppy = 1):
  pvcfsum = 0
cf = couponRate * face
for t in range (1, (ppy *m) +1):
  pv = (1 + y/ppy) ** (-t)
  pvcf = pv*cf/ppy
  #pvcfsum = pvcfsum + pvcf
  pvcfsum += pvcf
bondprice = pvcfsum + pv*face
return (bondprice)
