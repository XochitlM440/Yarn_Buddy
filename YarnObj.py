class Yarn:
    def __init__(self,name:str,colors:list[str],fiber:str,weight:int,
                 cost:float,yardage:float,tools:dict):
        self.name = name
        self.colors = colors
        self.fiber = fiber
        self.weight = weight
        self.cost = cost
        self.yardage = yardage
        self.tools = tools
        # if pulling from multiple catalogs/making stuff up, could add a company/manufacturer

    def __eq__(self):