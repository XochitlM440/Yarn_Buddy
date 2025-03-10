import YarnObj
import catalog

def str_to_float(s:str):
    try:
        f = float(s)
        return f
    except ValueError:
        return None


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

def price_range2(ylist:list[YarnObj.Yarn],low:float,high:float) -> dict[str]:
    in_r = {}
    in_r2 = []
    for idx in range(len(ylist)):
        if (ylist[idx].cost >= low) and (ylist[idx].cost <= high):
            in_r[ylist[idx].name] = ylist[idx].cost
            in_r2.append(ylist[idx])
    if len(in_r) == 0:
        print("no yarns could be found in that range.")
    else:
        print(in_r)
        return in_r2
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

def yardage_range2(ylist:list[YarnObj.Yarn], low: float, high: float) -> dict[str]:
    in_r = {}
    in_r2 = []
    for idx in range(len(ylist)):
        if (ylist[idx].yardage >= low) and (ylist[idx].yardage <= high):
            in_r[ylist[idx].name] = ylist[idx].yardage
            in_r2.append(ylist[idx])
    if len(in_r) == 0:
        print("no yarns could be found in that range.")
    else:
        print(in_r)
        return in_r2
#by xochitl
def yardage_range_with_project(ylist:list[YarnObj.Yarn], low:float, high:float, type:str, w:int):
    for i in range(len(catalog.project_size)):
        if type == catalog.project_size[i].project:
            x = catalog.project_size[i].yardage()
            y = x[w]
            z = y[0]
    range_list = []
    for idx in range(len(ylist)):
        if (ylist[idx].yardage >= low) and (ylist[idx].yardage <= high):
            range_list.append(ylist[idx])
    if len(range_list) == 0:
        print("no yarns could be found in that range.")
        return range_list
    else:
        print(range_list)
        return range_list



#by audrey
# A function that takes input of yarn catalog to find specific yardages within a price range.
# It takes inputs of the yarn database and an upper and lower limit, and outputs a dictionary with keys of yarn name
# and defs of how many you can buy for what price and how many yards it is

def yarn_quantity(ylist:list[[YarnObj.Yarn]], upperPrice:float,yardLim:float):
    q = {}
    q_full = []
    for idx in range(len(ylist)):
        count = upperPrice//ylist[idx].cost
        cost_tot = count*ylist[idx].cost
        if count > 0:
            sum = count*ylist[idx].yardage
            if sum >= yardLim:
                q[ylist[idx].name] = str(count) + " for $" + str(cost_tot) + ", " + str(sum) + " yards"
                q_full.append(ylist[idx])
    print(q)
    return q_full

#This function takes the input of a list of yarn objects and a weight (int) and filters
# by yarns that are that weight. The function gives an
# output list of the names of the yarns of that weight
#by xochitl
def weight_select(ylist:list[YarnObj.Yarn],type:str, proj:int):
    weight_list = []
    counter = 1
    while counter > 0:
        if counter > 1:
            proj = input("Let's try that again, what weight will you use to make your {} ".format(type))
        # sort list based on proj
        for idx in range(len(ylist)):
            x = ylist[idx].weight
            if proj == x:
                weight_list.append(ylist[idx])
        if weight_list == []:
            print("We can't find any yarn with the weight {}".format(proj))
            counter = 2
        else:
            counter = 0
            return weight_list

#by xochitl
def price_range_with_project(ylist:list[YarnObj.Yarn]) -> dict[str]:
    in_r = {}
    counter = 1
    while counter >1:
        if counter == 1:
            high = float(input("Please enter an upper price range. "))
            low = float(input("Please enter an lower price range. If you don't have a lower range, enter 0."))
        elif counter < 1:
            high = float(input ("Let's try that again, please enter an upper price range"))
            low = float(input("Please enter an lower price range. If you don't have a lower range, enter 0."))
        #sort based on high and low
        for idx in range(len(ylist)):
            if (ylist[idx].cost >= low) and (ylist[idx].cost <= high):
                in_r[ylist[idx].name] = ylist[idx].cost
            if len(in_r) == 0:
                print("no yarns could be found in that range.")
                counter = 2
            else:
                print(in_r)
                return in_r
                counter = 0

#by xochitl
def yardage_range_with_project(ylist:list[YarnObj.Yarn], upperPrice:float, type:str):
    for i in range(len(catalog.project_size)):
        if type == catalog.project_size[i].project:
            x = catalog.project_size[i].yardage()
    a = input("What weight of yarn will you use to make your {}? enter a number between 1 and 7".format(type))
    if a in catalog.weights:
        y = catalog.project_size[i].weight   #still want to call that i value but don't want to put it in the for loop
    x = yardage_range()




#by xochitl
def fiber_select(ylist:list[YarnObj.Yarn],type:str):
    fiber_list = []
    counter = 1
    while counter > 0:
        if counter == 1:
            proj = input("What fiber will you use to make your {} ".format(type))
        elif counter > 1:
            proj = input("Let's try that again, what fiber will you use to make your {} ".format(type))
        # sort list based on proj
        for idx in range(len(ylist)):
            x = ylist[idx].fiber
            if proj in x:
                fiber_list.append(ylist[idx])
        if fiber_list == []:
            print("We can't find any yarn with the fiber {}".format(proj))
            counter = 2
        else:
            counter = 0
    return fiber_list


# This function takes the input of a list of yarn objects and a color (string) and filters
# by yarns that are that weight. The function gives an
# output list of the names of the yarns of that weight
#by xochitl
def color_select(ylist: list[YarnObj.Yarn], type: str):  #type is the garment that they chose at the beginning
    color_list = []
    color_list_full = []
    counter = 1
    while counter > 0:
        if counter == 1:
            proj = input("What color will you use to make your {} ".format(type))
        elif counter > 1:
            proj = input("Let's try that again, what color will you use to make your {} ".format(type))
        #sort list based on proj
        for idx in range(len(ylist)):
            x = ylist[idx].colors
            if proj in x:
                color_list.append(ylist[idx].name)
                color_list_full.append(ylist[idx])
        if color_list == []:
            print("We can't find any yarn with the color {}".format(proj))
            counter = 2
        else:
            print("Here are the yarns that fit your color:")
            print(color_list)
            counter = 0
    return color_list_full

#by audrey
def color_select_yarn_only(ylist: list[YarnObj.Yarn]) -> list[str]:
    color_list = []
    color_list_full = []
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
                color_list_full.append(ylist[idx])
        if color_list == []:
            print("We can't find any yarn with the color {}. Make sure your color is capitalized!".format(proj))
            counter = 2
        else:
            counter = 0
            print("Here are the yarns that fit your color!")
            print(color_list)
    return color_list_full


#by audrey
def weight_select_yarn_only(ylist: list[YarnObj.Yarn]) -> list[str]:
    weight_list = []
    weight_list_full = []
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
                weight_list_full.append((ylist[idx]))
        if weight_list == []:
            print("We can't find any yarn with the weight {}.".format(proj))
            counter = 2
        else:
            counter = 0
            print("Here are the yarns that fit your weight!")
            print(weight_list)
    return proj
    return weight_list_full

# by audrey
def fiber_select_yarn_only(ylist: list[YarnObj.Yarn]) -> list[str]:
    fiber_list = []
    fiber_list_full = []
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
                fiber_list_full.append(ylist[idx])
        if fiber_list == []:
            print("We can't find any yarn with the fiber {}. Make sure your fiber is capitalized!".format(proj))
            counter = 2
        else:
            counter = 0
            print("Here are the yarns that fit your fiber type!")
            print(fiber_list)
    return fiber_list_full


# by audrey
def get_size(slist:list[YarnObj.Size],type:str,weight:int) -> list[int]:
    r = []
    for idx in range(len(slist)):
        if type == slist[idx].project:
            r2 = slist[idx].yardage[weight]
            r.append(r2)
    return r2


#this will run at the end once we have condensed listed of all the specs the user wants and how
#to print out the data in a nice way hhh
#by xochitl
def fancy_list (ylist: list[YarnObj.Yarn]):
    for i in range (len(ylist)):
        print(ylist[i].name)
        print ("Yarn information:")
        print ("Cost per skein: {}".format(ylist[i].cost))
        print ("Yardage: {}".format(ylist[i].yardage))
        print ("Yarn Weight: {}".format(ylist[i].weight))
        print ("Fiber Content: {}".format(ylist[i].fiber))
        print ("Available in: {}".format(ylist[i].colors))
        print ("For crocheting, we recommend using hook {}".format(ylist[i].tools["Crochet"]))
        print ("For knitting, we recommend using needle size {}".format(ylist[i].tools["Knit"]))
