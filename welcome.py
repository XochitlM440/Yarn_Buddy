import Functions
import YarnObj
import catalog

def main():
    print("Welcome to Yarn Buddy! This program is run entirely from the command line.)")
    e = 0
    p = 0
    while e == 0:
        a = input("What would you like to do? To pick yarns, type 'y'. To find a project type, type 'p'. "
                  "To see a more detailed list of available functions, type 'h'. ")
        if a == 'y' or a == 'Y':
            p = 1
        elif a == 'p' or a == 'P':
            p = 2
        while p == 1:
            print("This is the yarn picker screen! Here you can find yarns by various preferences such as a price range,"
                  "a yardage range, or color. ")
            u = input("To start, type 's'. To see a full list of filtering parameters, type 'h'. To "
                      "go back to the main menu, type 'esc'. ")
            if u == 's' or u == 'S':
                u = input("Would you like to filter by color? type y or n.")
                c = 0
                if u == "y" or "Y":
                    color_u = input("What color? To see a full list of options, type 'c'.")
                        if color_u == 'c':
                            print
            elif u == 'esc':
                e = 0
        while p == 2:
            print("This is the project picker screen! ")




main()
