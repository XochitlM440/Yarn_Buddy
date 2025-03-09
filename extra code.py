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
