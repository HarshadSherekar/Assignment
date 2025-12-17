km_to_m = lambda dist : dist*1000
m_to_cm =  lambda dist : dist*100
cm_to_mm = lambda dist : dist*10
ft_to_inch = lambda dist: dist*12
inch_to_cm= lambda dist : dist*2.54



def disconverter(distance,conversiontype,conversionfun):
    result=conversionfun(distance)
    print(f"{distance} {conversiontype.split()[0]} = {result} {conversiontype.split()[2]}")
    return result

distance=float(input("enter a distance value"))
disconverter(distance,"kilometer to meter", km_to_m)
disconverter(distance,"meter to centimeter", m_to_cm)
disconverter(distance,"centimeter to milimeter", cm_to_mm)
disconverter(distance,"feet  to inch ", ft_to_inch)
disconverter(distance," inch to cm ", inch_to_cm)    
    