import Functions
import YarnObj
import catalog
from catalog import project_size


# counter design works better than the other, use counters for page loops
# yarn selection pages by audrey

def main():
    counter = 1
    y_page = 0
    p_page = 0
    while counter > 0:
        if counter == 1:
            print("Welcome to Yarn Buddy! This program is run entirely from the command line.")
            print("What would you like to do?")
            a = input("To pick yarns, type 'y'. To find a project type, type 'p'. "
                      "To see a more detailed list of available functions, type 'h'. ")
        elif counter > 1:
            print("Welcome to Yarn Buddy! This program is run entirely from the command line.")
            print("What would you like to do?")
            a = input("To pick yarns, type 'y'. To find a project type, type 'p'. "
                      "To see a more detailed list of available functions, type 'h'. ")
        if a.lower() == 'h':
            print("This is the help menu! Here's a list of our available functions.")
            counter = 2
        elif a.lower() == 'y':
            y_page = 1
        elif a.lower() == 'p':
            p_page = 1
        while y_page > 0:
            if y_page == 1:
                print(
                    "This is the yarn picker screen! Here you can find yarns by various preferences such as a price range,"
                    "a yardage range, or color. ")
                u = input("To start, type 's'. To see a full list of filtering parameters, type 'h'. To "
                          "go back to the main menu, type 'esc'. ")
            elif y_page > 2:
                print(
                    "This is the yarn picker screen! Here you can find yarns by various preferences such as a price range,"
                    "a yardage range, or color. ")
                u = input("To start, type 's'. To see a full list of filtering parameters, type 'h'. To "
                          "go back to the main menu, type 'esc'. ")
            if u.lower() == 's':
                y_select = 1
                new_list = catalog.reduced_cat
                while y_select > 0:
                    u = input("Would you like to filter by color? type y or n. ")
                    if u.lower() == 'y':
                        print("Here's a list of available colors:")
                        print(catalog.colors)
                        new_list = Functions.color_select_yarn_only(new_list)
                        a = input("Would you like to filter this list by additional parameters? Type y or n. ")
                        if a.lower() == "y":
                            u = "n"
                        if a.lower() == "n":
                            new_list = catalog.reduced_cat
                            u = "n"
                    if u.lower() == "n":
                        u2 = input("Would you like to filter by yarn weight? type y or n. ")

                    if u2.lower() == "y":
                        print("Here's a list of available weights:")
                        print(catalog.weights)
                        new_list = Functions.weight_select_yarn_only(catalog.reduced_cat)

                        a = input("Would you like to filter this list by additional parameters? Type y or n. ")
                        if a.lower() == "y":
                            u2 = "n"
                        if a.lower() == "n":
                            new_list = catalog.reduced_cat
                            u2 = "n"

                    if u2.lower() == "n":
                        u3 = input("Would you like to filter by yarn fiber? type y or n. ")

                    if u3.lower() == "y":
                        print("Here's a list of available fibers:")
                        print(catalog.fibers)
                        new_list = Functions.fiber_select_yarn_only(catalog.reduced_cat)

                        a = input("Would you like to filter this list by additional parameters? Type y or n. ")
                        if a.lower() == "y":
                            u3 = "n"
                        if a.lower() == "n":
                            new_list = catalog.reduced_cat
                            u3 = "n"
                    if u3.lower() == "n":
                        u4 = input("Would you like to filter by a cost range? type y or n. ")

                    if u4.lower() == "y":
                        low = Functions.str_to_float(input("Please enter a lower price range. If you don't have one, enter 0. "))
                        high = Functions.str_to_float(input ("Please enter an upper price range. "))
                        new_list = Functions.price_range(catalog.reduced_cat,low,high)

                        a = input("Would you like to filter this list by additional parameters? Type y or n. ")
                        if a.lower() == "y":
                            u4 = "n"
                        if a.lower() == "n":
                            new_list = catalog.reduced_cat
                            u4 = "n"
                    if u4.lower() == "n":
                        u5 = input("Would you like to filter by a yardage range? type y or n. ")

                    if u5.lower() == "y":
                        low = Functions.str_to_float(input("Please enter a lower yardage range. If you don't have one, enter 0. "))
                        high = Functions.str_to_float(input("Please enter an upper yardage range. "))
                        new_list= Functions.yardage_range(catalog.reduced_cat, low, high)

                    if u5.lower() == "n":
                        print("Thanks for using the yarn picker!")
                        p = input("To restart, type 'r'. To return to the main menu, type 'esc'. ")
                        if p == 'r':
                            y_select = 0
                        if p == 'esc':
                            y_page = 0
                            break #this is currently not working (it was earlier), setting y_page to 0 should close the
                            # while loop and boot back to counter, but it's going back to the color select prompt. setting
                            # a break does work though.

            if u.lower() == 'h':
                print("Yarns can be filtered by color, yarn weight, fiber, price, or yardage.")
                continue
            if u.lower() == 'esc':
                y_page = 0  # because setting y_page to 0 terminates the while loop, booting back to start



        while p_page > 0:  #by xochitl
            new_list = catalog.reduced_cat
            print("This is the project picker screen! Lets get you a project to work on.")
            print("Here is a list of possible projects to pick from: hat, scarf, socks, shawl, sweater, baby blanket, and afghan.")
            p1 = input ("To pick a project, type it in here: ")


            if p1.lower() in catalog.projects:
                type = p1.lower()
                p_select = 1

                while p_select > 0:
                    # start project subpages here
                    proj = 4
                    while y_select > 0:
                        u = input("Would you like to filter by color? type y or n. ")
                        if u.lower() == 'y':
                            print("Here's a list of available colors:")
                            print(catalog.colors)
                            new_list = Functions.color_select(new_list, type)

                            a = input ("Would you like to filter by additional parameters? type y or n. ")
                            if a.lower() == 'y':
                                u = "n"
                            if a.lower() == "n":
                                new_list = catalog.reduced_cat
                                u = "n"


                        if u.lower() == "n":
                            u2 = input("Would you like to filter by yarn weight? type y or n. ")
                        if u2.lower() == "y":
                            print("Here's a list of available weights:")
                            print(catalog.weights)
                            proj = int(input("What weight will you use to make your {} ".format(type)))
                            new_list = Functions.weight_select(new_list, type, proj)
                            a = input ("Would you like to filter by additional parameters? type y or n. ")
                            if a.lower() == 'y':
                                u2 = "n"
                            if a.lower() == "n":
                                new_list = catalog.reduced_cat
                                u2 = "n"


                        if u2.lower() == "n":
                            u3 = input("Would you like to filter by yarn fiber? type y or n. ")
                        if u3.lower() == "y":
                            print("Here's a list of available fibers:")
                            print(catalog.fibers)
                            new_list = Functions.fiber_select(new_list, type)
                            a = input ("Would you like to filter by additional parameters? type y or n. ")
                            if a.lower() == 'y':
                                u3 = "n"
                            if a.lower() == "n":
                                new_list = catalog.reduced_cat
                                u3 = "n"

                        if u3.lower() == "n":
                            u5 = input("Would you like to filter by a yardage range? type y or n. ")
                            counter = 1
                            while counter > 0:
                                if counter == 1:
                                    if u5.lower() == "y":
                                            new_list = Functions.price_range_with_project(new_list)
                                            low = Functions.str_to_float(input(
                                                "Please enter a lower yardage range. If you don't have one, enter 0. "))
                                            high = Functions.str_to_float(input("Please enter an upper yardage range. "))
                                elif counter > 1:
                                    low = Functions.str_to_float(input(
                                        "Please enter a lower yardage range. If you don't have one, enter 0. "))
                                    high = Functions.str_to_float(input("Please enter an upper yardage range. "))
                                    if u2.lower() == "y":
                                        weight = proj
                                        new_list = Functions.yardage_range_with_project(new_list, low, high, type, weight)
                                    if u2.lower() == "n":
                                        weight = 4
                                        new_list = Functions.yarn_quantity_with_project(new_list, low, high, type, weight)

                                    if new_list == []:
                                        a = input ("We couldn't find any yarns that match your parameters, lets try that again.")
                                        counter = 2
                                    else:
                                        counter = 0



                                a = input("Would you like to filter by additional parameters? type y or n. ")
                                if a.lower() == 'y':
                                    u5 = "n"
                                if a.lower() == "n":
                                    new_list = catalog.reduced_cat
                                    u5 = "n"

                        if u5.lower() == "n":
                            print("Thanks for using the project picker!")
                            #start of showing results
                            a = input ("If you would like a condensed list of yarns that fit your project, type a. "
                                       "If you would like to see the details of each yarn, type b.")
                            if a.lower() == 'a':
                                print("Here is a condensed list of yarns that fit your project: {}".format(new_list))
                            if a.lower() == 'b':
                                print("Here are the yarns that fit your project and the details for each yarn: {}".format(Functions.fancy_list(new_list)))


                            p = input("To restart, type 'r'. To return to the main menu, type 'esc'. ")
                            if p == 'r':
                                y_select = 0
                            if p == 'esc':
                                y_page = 0
                                break  # this is currently not working (it was earlier), setting y_page to 0 should close the
                                # while loop and boot back to counter, but it's going back to the color select prompt. setting
                                # a break does work though.

                if u.lower() == 'h':
                    print("Yarns can be filtered by color, yarn weight, fiber, price, or yardage.")
                    continue
                if u.lower() == 'esc':
                    y_page = 0
            else:
                b = input("looks like that project doesn't exist, check your spelling and try again by typing t:")
                if b.lower() == 't':
                    p_page = 0



main()