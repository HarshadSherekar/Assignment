
tons_to_kg=lambda weight : weight*1000
kg_to_gm=lambda ton_to_kg: ton_to_kg *1000000
gm_to_mg=lambda kg_to_gm : kg_to_gm*1000000000
mg_to_pound=lambda weight :weight*0.00000220462


def weightconverter(weight,conversiontype,conversionfun):
    result=conversionfun(weight)
    print(f"{weight} {conversiontype.split()[0]} = {result} {conversiontype.split()[2]}")
    return result


weight=float(input("enter a weight value"))
weightconverter(weight,"tons to kilograms",tons_to_kg)
weightconverter(weight,"kilograms to grams",kg_to_gm)
weightconverter(weight,"gram to miligram",gm_to_mg)
weightconverter(weight,"miligram to pound",mg_to_pound)