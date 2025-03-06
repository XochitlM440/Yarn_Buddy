import YarnObj
import catalog


#def project_picker(ylist:list[YarnObj.Yarn],params:list[str]) -> str:
# thinking that params could be a list of user inputted parameters
#   (from the console) that we could search the yarn list for? this is
#   probably the culmination of other functions tho since we'd need to
#   search by price range and yardage range and so forthh

# This function takes the input of the yarn catalog and a list of user parameters and returns a string of a potential project that
# they could make.

#def project_picker(ylist:list[YarnObj.Yarn],params:list[str]): -> str:
    #proj = input("Welcome! What kind project are you looking to make today?")
    #if proj in catalog.project_size(YarnObj.Size): # is this correct?


# need to think of what should be prioritized. if we input a price range
# and a yardage range, should it give you the cheaper one first or the
# one with more yarn

# The following range functions filter the yarn catalog by the specified parameters and returns a list of the names
# of corresponding yarns.

# by audrey
# This function takes the input of a list of yarn objects and an upper and lower price limit (in floats) and filters
# by yarns that are within that price range. The function gives an
# output dictionary with keys of the names of the yarns and the definitions of their prices

def price_range(ylist:list[YarnObj.Yarn],low:float,high:float) -> dict[str]:
    in_r = {}
    for idx in range(len(ylist)):
        if (ylist[idx].cost >= low) and (ylist[idx].cost <= high):
            in_r[ylist[idx].name] = ylist[idx].cost
    return in_r

# by audrey
#This function takes the input of a list of yarn objects and an upper and lower yardage limit (in floats) and filters
# by yarns that are within that yardage range. The function gives an
# output dictionary with keys of the names of the yarns and the definitions of their yardages
def yardage_range(ylist:list[YarnObj.Yarn], low: float, high: float) -> dict[str]:
    in_r = {}
    for idx in range(len(ylist)):
        if (ylist[idx].yardage >= low) and (ylist[idx].yardage <= high):
            in_r[ylist[idx].name] = ylist[idx].yardage
    return in_r

#This function takes the input of a list of yarn objects and a weight (int) and filters
# by yarns that are that weight. The function gives an
# output list of the names of the yarns of that weight
def weight_select(ylist:list[YarnObj.Yarn],type:str):
    proj = input("Excellent choice, what weight will you use to make your {}".format(type))
    if proj is int and proj in range(1,7): #correct range?


# This function takes the input of a list of yarn objects and a color (string) and filters
# by yarns that are that weight. The function gives an
# output list of the names of the yarns of that weight
def color_select(ylist: list[YarnObj.Yarn], type: str):
    proj = input("Excellent choice, what weight will you use to make your {}".format(type))
    if proj is int and proj in range(1, 7):  # correct range?


#by audrey
# A function that takes input of yarn catalog to find specific yardages within a price range.
# It takes inputs of the yarn database and an upper and lower limit, and outputs a dictionary with keys of yarn name
# and defs of how many you can buy for what price and how many yards it is

def yarn_quantity(ylist:list[[YarnObj.Yarn]], upperPrice:float,yardLim:float):
    q = {}
    for idx in range(len(ylist)):
        count = upperPrice//ylist[idx].cost
        cost_tot = count*ylist[idx].cost
        if count > 0:
            sum = count*ylist[idx].yardage
            if sum >= yardLim:
                q[ylist[idx].name] = str(count) + " for $" + str(cost_tot) + ", " + str(sum) + " yards"
    return q

#def yarn_specs(ylist:list[YarnObj.Yarn],params:list[str])
    # sim to proj pick but finds yarns that fit params. would extract data from params

#def params_builder():
    #takes user input, makes specifically ordered list based on user responses? would
#   be easier to use in long run but might need a lot of exceptions

#def main():
    #a = yarn_quantity(catalog.reduced_cat,25,1000)
    #print(a)
#main()