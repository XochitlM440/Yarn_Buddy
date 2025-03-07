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
    if len(in_r) == 0:
        print("no yarns could be found in that range.")
    else:
        print(in_r)
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
    if len(in_r) == 0:
        print("no yarns could be found in that range.")
    else:
        print(in_r)
        return in_r

#This function takes the input of a list of yarn objects and a weight (int) and filters
# by yarns that are that weight. The function gives an
# output list of the names of the yarns of that weight
#by xochitl
def weight_select(ylist:list[YarnObj.Yarn],type:str):
    weight_list = []
    counter = 1
    while counter > 0:
        if counter == 1:
            proj = input("Excellent choice, what color will you use to make your {} ".format(type))
        elif counter > 1:
            proj = input("Let's try that again, what color will you use to make your {} ".format(type))
        # sort list based on proj
        for idx in range(len(ylist)):
            x = ylist[idx].weight
            if proj in x:
                weight_list.append(ylist[idx])
        if weight_list == []:
            print("We can't find any yarn with the weight {}".format(proj))
            counter = 2
        else:
            counter = 0

#by xochitl
def price_select(ylist:list[YarnObj.Yarn],type:str):
    price_list = []
    counter = 1
    while counter > 0:
        if counter == 1:
            proj = input("Excellent choice, what price yarn do you want to use to make your {} ".format(type))
        elif counter > 1:
            proj = input("Let's try that again, what price yarn do you want to use to make your {} ".format(type))
        # sort list based on proj
        for idx in range(len(ylist)):
            x = ylist[idx].cost
            if proj in x:
                price_list.append(ylist[idx])
        if price_list == []:
            print("We can't find any yarn with the color {}".format(proj))
            counter = 2
        else:
            counter = 0


# This function takes the input of a list of yarn objects and a color (string) and filters
# by yarns that are that weight. The function gives an
# output list of the names of the yarns of that weight
#by xochitl
def color_select(ylist: list[YarnObj.Yarn], type: str):  #type is the garment that they chose at the beginning
    color_list = []
    counter = 1
    while counter > 0:
        if counter == 1:
            proj = input("Excellent choice, what color will you use to make your {} ".format(type))
        elif counter > 1:
            proj = input("Let's try that again, what color will you use to make your {} ".format(type))
        #sort list based on proj
        for idx in range(len(ylist)):
            x = ylist[idx].colors
            if proj in x:
                color_list.append(ylist[idx])
        if color_list == []:
            print("We can't find any yarn with the color {}".format(proj))
            counter = 2
        else:
            counter = 0

#by audrey
def color_select_yarn_only(ylist: list[YarnObj.Yarn]) -> list[str]:
    color_list = []
    counter = 1
    while counter > 0:
        if counter == 1:
            proj = input("What color would you like to filter by? ")
        elif counter > 1:
            proj = input("Let's try that again, what color will you use? ")
        #sort list based on proj
        for idx in range(len(ylist)):
            x = ylist[idx].colors
            if proj in x:
                color_list.append(ylist[idx].name)
        if color_list == []:
            print("We can't find any yarn with the color {}. Make sure your color is capitalized!".format(proj))
            counter = 2
        else:
            counter = 0
            print("Here are the yarns that fit your color!")
            print(color_list)


#by audrey
def weight_select_yarn_only(ylist: list[YarnObj.Yarn]) -> list[str]:
    weight_list = []
    counter = 1
    while counter > 0:
        if counter == 1:
            proj = int(input("What weight would you like to filter by? "))
        elif counter > 1:
            proj = int(input("Let's try that again, what weight will you use? "))
        #sort list based on proj
        for idx in range(len(ylist)):
            x = ylist[idx].weight
            if proj == x:
                weight_list.append(ylist[idx].name)
        if weight_list == []:
            print("We can't find any yarn with the weight {}.".format(proj))
            counter = 2
        else:
            counter = 0
            print("Here are the yarns that fit your weight!")
            print(weight_list)

# by audrey
def fiber_select_yarn_only(ylist: list[YarnObj.Yarn]) -> list[str]:
    fiber_list = []
    counter = 1
    while counter > 0:
        if counter == 1:
            proj = input("What fiber type would you like to filter by? ")
        elif counter > 1:
            proj = input("Let's try that again, what fiber will you use? ")
        #sort list based on proj
        for idx in range(len(ylist)):
            x = ylist[idx].fiber
            if proj in x:
                fiber_list.append(ylist[idx].name)
        if fiber_list == []:
            print("We can't find any yarn with the fiber {}. Make sure your fiber is capitalized!".format(proj))
            counter = 2
        else:
            counter = 0
            print("Here are the yarns that fit your fiber type!")
            print(fiber_list)






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
    #a = price_range(catalog.reduced_cat,0,30)

#main()


#this will run at the end once we have condensed listed of all the specs the user wants and how
#to print out the data in a nice way
def fancy_list (ylist: list[YarnObj.Yarn]):
    for i in range (len(ylist)):
        print(ylist[i].name)
        print ("yarn information")
        print ("Cost per skein: {}".format(ylist[i].cost))
        print ("Yardage: {}".format(ylist[i].yardage))
        print ("Yarn Weight: {}".format(ylist[i].weight))
        print ("Fiber Content: {}".format(ylist[i].fiber))
        print ("Available in: {}".format(ylist[i].colors))
        print ("For crocheting, we recommend using hook {}".format(ylist.[i].tools["Crochet"]))
        print ("For knitting, we recommend using needle size {}".format(ylist.[i].tools["Knit"]))
