import Functions
import YarnObj
import catalog
from catalog import project_size


# counter design works better than the other, use counters for page loops
# yarn selection pages by audrey
# project + yarn selection pages by xochitl

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
            print("On the Yarn Picker screens you can filter our yarn catalog by color, yarn weight, yarn fiber,")
            print("yarn price range, or yarn yardage range. You can start apply all of these filters to a single")
            print("list or start with a new search of the catalog each time.")
            print("\n On the Project Picker screen you can select a project to make, and then filter the yarn catalog")
            print("by the same parameters. You will get an output of how many skeins of a type of yarn that you would")
            print("need to buy to complete your chosen project.")
            a2 = input("To return to the menu, type 'r'. ")


            if a2.lower() == 'r':
                counter = 2
        elif a.lower() == 'y':
            # sends you to the yarn selection subloops
            y_page = 1
        elif a.lower() == 'p':
            # sends you to the project selection subloops
            p_page = 1

        while y_page > 0:
            p_page = 0
            p_select = 0
            # default landing page
            if y_page == 1:
                print(
                    "This is the yarn picker screen! Here you can find yarns by various preferences such as a price range,"
                    "a yardage range, or color. ")
                u = input("To start, type 's'. To see a full list of filtering parameters, type 'h'. To "
                          "go back to the main menu, type 'esc' at any time. ")


            # displayed after visiting the help page
            elif y_page > 2:
                print(
                    "This is the yarn picker screen! Here you can find yarns by various preferences such as a price range,"
                    "a yardage range, or color. ")
                u = input("To start, type 's'. To see a full list of filtering parameters, type 'h'. To "
                          "go back to the main menu, type 'esc' at any time. ")

            # entering yarn selection subloops
            if u.lower() == 's':
                y_select = 1
                new_list = catalog.reduced_cat
                while y_select > 0:
                    #filtering by color
                    u = input("Would you like to filter by color? type y or n. ")
                    if u.lower() == 'y':
                        print("Here's a list of available colors:")
                        print(catalog.colors)
                        new_list = Functions.color_select_yarn_only(new_list)

                        # option of saving or discarding current list
                        a = input("Would you like to filter this list by additional parameters? Type y or n. ")
                        if a.lower() == "y":
                            u = "n"
                        if a.lower() == "n":
                            new_list = catalog.reduced_cat
                            u = "n"
                        if a.lower() == 'esc':
                            y_page = 0
                            break
                    if u.lower() == "n":
                        u2 = input("Would you like to filter by yarn weight? type y or n. ")
                    if u.lower() == 'esc':
                        y_page = 0
                        break

                    #sorting by weight
                    if u2.lower() == "y":
                        print("Here's a list of available weights:")
                        print(catalog.weights)
                        new_list = Functions.weight_select_yarn_only(new_list)

                        # option of saving or discarding current list
                        a = input("Would you like to filter this list by additional parameters? Type y or n. ")
                        if a.lower() == "y":
                            u2 = "n"
                        if a.lower() == "n":
                            new_list = catalog.reduced_cat
                            u2 = "n"
                        if a.lower() == 'esc':
                            y_page = 0
                            break

                    #sorting by fiber content
                    if u2.lower() == "n":
                        u3 = input("Would you like to filter by yarn fiber? type y or n. ")
                    if u2.lower() == 'esc':
                        y_page = 0
                        break
                    if u3.lower() == "y":
                        print("Here's a list of available fibers:")
                        print(catalog.fibers)
                        new_list = Functions.fiber_select_yarn_only(new_list)

                        # option of saving or discarding current list
                        a = input("Would you like to filter this list by additional parameters? Type y or n. ")
                        if a.lower() == "y":
                            u3 = "n"
                        if a.lower() == "n":
                            new_list = catalog.reduced_cat
                            u3 = "n"
                        if a.lower() == 'esc':
                            y_page = 0
                            break

                    #sorting by cost
                    if u3.lower() == "n":
                        u4 = input("Would you like to filter by a cost range? type y or n. ")
                    if u3.lower() == 'esc':
                        y_page = 0
                        break

                    if u4.lower() == "y":
                        low = Functions.str_to_float(input("Please enter a lower price range. If you don't have one, enter 0. "))
                        high = Functions.str_to_float(input ("Please enter an upper price range. "))
                        new_list = Functions.price_range2(new_list,low,high)

                        # option of saving or discarding current list
                        a = input("Would you like to filter this list by additional parameters? Type y or n. ")
                        if a.lower() == "y":
                            u4 = "n"
                        if a.lower() == "n":
                            new_list = catalog.reduced_cat
                            u4 = "n"
                        if a.lower() == 'esc':
                            y_page = 0
                            break

                    #sorting by yardage
                    if u4.lower() == "n":
                        u5 = input("Would you like to filter by a yardage range? type y or n. ")
                    if u4.lower() == 'esc':
                        y_page = 0
                        break

                    if u5.lower() == "y":
                        low = Functions.str_to_float(input("Please enter a lower yardage range. If you don't have one, enter 0. "))
                        high = Functions.str_to_float(input("Please enter an upper yardage range. "))
                        new_list= Functions.yardage_range2(new_list, low, high)
                        u5 = "n"
                    if u5.lower() == 'esc':
                        y_page = 0
                        break

                    #end screen
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


        # by xochitl
        while p_page > 0:
            y_page = 0 # closes other section just in case they've navigated from there (or else it would continue to boot them back when the while loop closes)
            y_select = 0
            new_list = catalog.reduced_cat
            print("This is the project picker screen! Lets get you a project to work on. To go back to the main menu, type 'esc' at any time.")
            print("Here is a list of possible projects to pick from: hat, scarf, socks, shawl, sweater, baby blanket, and afghan.")
            p1 = input ("To pick a project, type it in here: ")

            if p1.lower() == 'esc':
                p_page = 0
                break

            elif p1.lower() in catalog.projects:
                type = p1.lower()
                p_select = 1

                while p_select > 0:

                    # start project subpages here
                    proj = 4
                    while p_select > 0:

                        #sorting by color
                        u = input("Would you like to filter by color? type y or n. ")
                        if u.lower() == 'esc': # currently doesn't  work, just re-displays the color select
                            p_page = 0
                            break
                        if u.lower() == 'y':
                            print("Here's a list of available colors:")
                            print(catalog.colors)
                            new_list = Functions.color_select(new_list, type)

                            # option of saving or discarding current list
                            a = input ("Would you like to filter by additional parameters? type y or n. ")
                            if a.lower() == 'y':
                                u = "n"
                            if a.lower() == "n":
                                new_list = catalog.reduced_cat
                                u = "n"
                            if a.lower() == 'esc':
                                p_page = 0
                                break

                        #sorting by weight
                        if u.lower() == "n":
                            u2 = input("Would you like to filter by yarn weight? type y or n. ")
                        if u2.lower() == "y":
                            print("Here's a list of available weights:")
                            print(catalog.weights)

                            new_list = Functions.weight_select_yarn_only(new_list)

                            # option of saving or discarding current list
                            a = input ("Would you like to filter by additional parameters? type y or n. ")
                            if a.lower() == 'y':
                                u2 = "n"
                            if a.lower() == "n":
                                new_list = catalog.reduced_cat
                                u2 = "n"
                            if a.lower() == 'esc':
                                p_page = 0
                                break

                        #sorting by fiber
                        if u2.lower() == "n":
                            u3 = input("Would you like to filter by yarn fiber? type y or n. ")
                        if u2.lower() == 'esc':
                            p_page = 0
                            break
                        if u3.lower() == "y":
                            print("Here's a list of available fibers:")
                            print(catalog.fibers)
                            new_list = Functions.fiber_select(new_list, type)

                            # option of saving or discarding current list
                            a = input ("Would you like to filter by additional parameters? type y or n. ")
                            if a.lower() == 'y':
                                u3 = "n"
                            if a.lower() == "n":
                                new_list = catalog.reduced_cat
                                u3 = "n"
                            if a.lower() == 'esc':
                                p_page = 0
                                break

                    # we don't actually need a yardage range prompt because the project selection itself is acting as the limiting range
                        if u3.lower() == "n":
                            u4 = input("Would you like to set a budget for your project? type y or n. ")
                            if u4 == "y":
                                print("Yarns range between $4 and $130")
                                high = Functions.str_to_float(input("What's your budget? Enter a number without dollar signs. "))
                                if u2 == "y":
                                    f_lim = Functions.get_size(catalog.project_size,p1,u2)
                                    lim = f_lim[1]
                                    print("Here are the names and quantities of yarns that fit your budget!")
                                    new_list = Functions.yarn_quantity(new_list,high,lim)
                                if u2 == "n":
                                    f_lim = Functions.get_size(catalog.project_size,p1,4)
                                    lim = f_lim[1]
                                    new_list = Functions.yarn_quantity(new_list,high,lim)
                                    print("Here are the names and quantities of yarns that fit your budget!")
                                    u5 = "n"
                            if u4 == "n":
                                u5 = "n"
                            if u4 == "esc":
                                p_page = 0
                                break
                        if u3.lower() == 'esc':
                            p_page = 0
                            break

                        if u5.lower() == "n":
                            print("Thanks for using the project picker!")
                            #start of showing results
                            a = input ("If you would like a condensed list of yarns that fit your project, type a. "
                                       "If you would like to see the details of each yarn, type b.")
                            if a.lower() == 'a':
                                print("Here is a condensed list of yarns that fit your project: {}".format(new_list))
                            if a.lower() == 'b':
                                print("Here are the yarns that fit your project and the details for each yarn:")
                                Functions.fancy_list(new_list)


                            p = input("To restart, type 'r'. To return to the main menu, type 'esc'. ")
                            if p == 'r':
                                y_select = 0
                            if p == 'esc':
                                y_page = 0
                                break  

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