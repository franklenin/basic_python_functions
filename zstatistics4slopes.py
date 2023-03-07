
import math

#------------------------------------------------------
#------------------------------------------------------
def standard_error (se_1, se_2):
    ''' Code for computing the z statistics between 
    two slopes
    '''
    
    # Power of two for the standard errors
    a = math.pow(se_1, 2)
    b = math.pow(se_2, 2)

    # We sum the result
    c = a + b
    
    # We obtain the root squared
    SE = math.sqrt(c)
        
    return(SE)  


#------------------------------------------------------
#------------------------------------------------------
def z_statistic (slope_1, slope_2, se_1, se_2):
    
    # Obtain the difference between the slopes
    slope_difference = slope_1 - slope_2
    
    # Computer the standard erorr
    SE = standard_error(se_1, se_2)
    
    # Obtain Z score
    z = slope_difference / SE

    print('Z score = ', z)

    
    return(z)    