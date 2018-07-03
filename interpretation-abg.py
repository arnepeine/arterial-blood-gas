#The calculations above are based on the Henderson-Hasselbalch equation:
#pH = pK + log*[HCO3-]/[CO2]
#Replacing pK = 6.1, and [CO2] = 0.03 * pCO2, and removing the logarithms to get
#HCO3 = 0.03 * pCO2 * 10^(pH - 6.1)
#Henderson-Hasselbalch equation
#B.E. = 0.02786 * pCO2 * 10 (pH - 6.1) + 13.77 * pH - 124.58
#V 1.1.

# NOTE: These are not meant to be used within clinical trials or treatment
# This script can not handle exceptions (e.g. full compensations) and does not handle errors correctly
# Next steps: Error handling

def calculateBEPCO2(pco2,ph):
    hco3 = 0.03 * pco2 * 10**(ph-6.1)
    be= 0.02786 * pco2 * 10**(ph - 6.1) + 13.77 * ph - 124.58
    #if type_of_bga = metabolic_acidosis
    return print(hco3,be)


def ABGinterpretation(ph,pco2,na,k,cl):
    hco3 = 0.03 * pco2 * 10**(ph-6.1)
    be = 0.02786 * pco2 * 10**(ph - 6.1) + 13.77 * ph - 124.58
    anion_gap= (na+k)-(cl+hco3)
    
    if ph <7.35:
        if pco2 > 45:
            result="respiratory acidosis"
        elif hco3 < 24:
            result="metabolic acidosis"
        else:
            result="unknown"
    elif ph >7.43:
        if pco2 < 38:
            result="respiratory alkalosis"
        elif hco3 > 30:
            result="metabolic alkalosis"
        else:
            result="unknown"
    else:
        result="normal acid-base or compensated"
    

    return(ph,pco2,na,k,cl,hco3,be,anion_gap,result)
 # to be implemented: error handling       

print(ABGinterpretation(7.11,33,143,3.4,12))   
        
    
