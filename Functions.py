import YarnObj
import catalog


#def project_picker(ylist:list[YarnObj.Yarn],params:list[str]) -> str:
    # thinking that params could be a list of user inputted parameters
#   (from the console) that we could search the yarn list for? this is
#   probably the culmination of other functions tho since we'd need to
#   search by price range and yardage range and so forth

# need to think of what should be prioritized. if we input a price range
# and a yardage range, should it give you the cheaper one first or the
# one with more yarn

# by audrey
def price_range(ylist:list[YarnObj.Yarn],low:float,high:float) -> list[str]:
    in_r = []
    for idx in range(len(ylist)):
        if (ylist[idx].cost >= low) and (ylist[idx].cost <= high):
            in_r.append(ylist[idx].name)
    return in_r

# by audrey
def yardage_range(ylist:list[YarnObj.Yarn], low: float, high: float) -> list[str]:
    in_r = []
    for idx in range(len(ylist)):
        if (ylist[idx].yardage >= low) and (ylist[idx].yardage <= high):
            in_r.append(ylist[idx].name)
    return in_r

#def yarn_specs(ylist:list[YarnObj.Yarn],params:list[str])
    # sim to proj pick but finds yarns that fit params. would extract data from params

#def params_builder():
    #takes user input, makes specifically ordered list based on user responses? would
#   be easier to use in long run but might need a lot of exceptions

def main():
    a = price_range(catalog.short_cat,6,15)
    print(a)
main()