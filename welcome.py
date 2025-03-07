import Functions
import YarnObj
import catalog
from catalog import project_size


# counter design works better than the other, use counters for page loops

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
                while y_select > 0:
                    u = input("Would you like to filter by color? type y or n. ")
                    if u.lower() == 'y':
                        print("Here's a list of available colors:")
                        print(catalog.colors)
                        Functions.color_select_yarn_only(catalog.reduced_cat)
                        u = "n"
                    if u.lower() == "n":
                        u2 = input("Would you like to filter by yarn weight? type y or n. ")

                    if u2.lower() == "y":
                        print("Here's a list of available weights:")
                        print(catalog.weights)
                        Functions.weight_select_yarn_only(catalog.reduced_cat)
                        u2 = "n"
                    if u2.lower() == "n":
                        u3 = input("Would you like to filter by yarn fiber? type y or n. ")

                    if u3.lower() == "y":
                        print("Here's a list of available fibers:")
                        print(catalog.fibers)
                        Functions.fiber_select_yarn_only(catalog.reduced_cat)
                        u3 = "n"
                    if u3.lower() == "n":
                        u4 = input("Would you like to filter by a cost range? type y or n. ")

                    if u4.lower() == "y":
                        low = float(input("Please enter a lower price range. If you don't have one, enter 0. "))
                        high = float(input ("Please enter an upper price range. "))
                        Functions.price_range(catalog.reduced_cat,low,high)
                        u4 = "n"
                    if u4.lower() == "n":
                        u5 = input("Would you like to filter by a yardage range? type y or n. ")

                    if u5.lower() == "y":
                        low = float(input("Please enter a lower yardage range. If you don't have one, enter 0. "))
                        high = float(input("Please enter an upper yardage range. "))
                        Functions.yardage_range(catalog.reduced_cat, low, high)
                        u5 = "n"
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
            print("This is the project picker screen! Lets get you a project to work on.")
            print("Here is a list of possible projects to pick from, scarf, socks, shawl, sweater, baby blanket, and afghan.")
            p1 = input ("To pick a project, type it in here:")
            x = project_size[YarnObj.Size]
            if p1.lower() in x.project:  #doesn't like the project??????
                type = p1.lower()
            else:
                b = input("looks like that project doesn't exist, check your spelling and try again by typing t:")
                if b.lower() == 't':
                    p_page = 1
                    break
                else:
                    p_page = 0   #how to make it go to the next screen?
            return type   #is this ok??


main()