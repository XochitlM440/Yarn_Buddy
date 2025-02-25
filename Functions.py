import yarnObj


def project_picker(ylist:list[yarnObj.Yarn],params:list[str]) -> str:
    # thinking that params could be a list of user inputted parameters
#   (from the console) that we could search the yarn list for? this is
#   probably the culmination of other functions tho since we'd need to
#   search by price range and yardage range and so forth

# need to think of what should be prioritized. if we input a price range
# and a yardage range, should it give you the cheaper one first or the
# one with more yarn

def price_range(ylist:list[yarnObj.Yarn],low:float,high:float) -> list[yarnObj.Yarn]:

def yardage_range(ylist:list[yarnObj.Yarn], low: float, high: float) -> list[yarnObj.Yarn]:

def yarn_specs(ylist:list[yarnObj.Yarn],params:list[str])
    # sim to proj pick but finds yarns that fit params. would extract data from params

def params_builder():
    #takes user input, makes specifically ordered list based on user responses? would
#   be easier to use in long run but might need a lot of exceptions