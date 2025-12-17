def km_to_m(km):
    return km*1000

def m_to_cm(m):
   return m*1000

def cm_to_mm(cm):
    return cm*10

def ft_to_inch(ft):
    return ft*12

def inch_to_cm(inch):
    return inch*2.54

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
