def getBondDuration(y, face, couponRate, m, ppy=1):
    
    couponRate = couponRate / ppy
    m = m * ppy         
    y = y / ppy          
    pvcfsum = 0                 
    pvcfwsum = 0                
for t in range(1, m + 1):                  
        pvm = (1 + y) ** (-t)                 
        cf = face * couponRate               
        if t == m:                             
            cf = cf + face                    
        pvcf = pvm * cf                   
        pvcfw = pvcf * t                    
        pvcfwsum = pvcfwsum + pvcfw            
        pvcfsum = pvcfsum  + pvcf            

    bondDuration = (pvcfwsum / pvcfsum) / ppy  
    return bondDuration
