import YarnObj
import catalog


#def project_picker(ylist:list[YarnObj.Yarn],params:list[str]) -> str:
    # thinking that params could be a list of user inputted parameters
#   (from the console) that we could search the yarn list for? this is
#   probably the culmination of other functions tho since we'd need to
#   search by price range and yardage range and so forth
def project_picker():
    proj = input("Welcome! What kind project are you looking to make today?")
    if proj in catalog.project_size(YarnObj.Size): # is this correct?
        print ("HI")
        print("why me?")


# need to think of what should be prioritized. if we input a price range
# and a yardage range, should it give you the cheaper one first or the
# one with more yarn

# by audrey
def price_range(ylist:list[YarnObj.Yarn],low:float,high:float) -> dict[str]:
    in_r = {}
    for idx in range(len(ylist)):
        if (ylist[idx].cost >= low) and (ylist[idx].cost <= high):
            in_r[ylist[idx].name] = ylist[idx].cost
    return in_r

# by audrey
def yardage_range(ylist:list[YarnObj.Yarn], low: float, high: float) -> dict[str]:
    in_r = {}
    for idx in range(len(ylist)):
        if (ylist[idx].yardage >= low) and (ylist[idx].yardage <= high):
            in_r[ylist[idx].name] = ylist[idx].yardage
    return in_r

def weight_select(type:str):
    proj = input("Excellent choice, what weight will you use to make your {}".format(type))
    if proj is int and proj in range(1,7): #correct range?




#A function that uses the above to find specific yardages within a price range.
# It takes inputs of the yarn database and an upper and lower limit, and outputs a dictionary
# of how many of each yarn type could be bought.
# Eg: you want to know what types of yarn you could buy for less than $50
# that would get you more than 500 yards, and it would tell you that you could buy 3 blues or 5 reds

#by audrey
def yarn_quantity(ylist:list[[YarnObj.Yarn]], upperPrice:float,yardLim:float):
    q = {}
    for idx in range(len(ylist)):
        count = upperPrice//ylist[idx].cost
        cost_tot = count*ylist[idx].cost
        if count > 0:
            sum = count*ylist[idx].yardage
            if sum >= yardLim:
                q[ylist[idx].name] = str(count) + " for $" + str(cost_tot) + " gets " + str(sum) + " yards"
    return q

#def yarn_specs(ylist:list[YarnObj.Yarn],params:list[str])
    # sim to proj pick but finds yarns that fit params. would extract data from params

#def params_builder():
    #takes user input, makes specifically ordered list based on user responses? would
#   be easier to use in long run but might need a lot of exceptions

def main():
    a = yarn_quantity(catalog.short_cat,50,1000)
    print(a)
main()