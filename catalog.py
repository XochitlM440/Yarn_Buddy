import YarnObj
colors = ["Red","Orange","Yellow","Green","Blue","Purple","Pink","Brown","Ombre","Multi"]
weights = [1,3,4,5,6,7]
fibers =  ["Acrylic","Cotton","Rayon","Wool","Bamboo","Polyester","Nylon","Alpaca","Merino","Yak","Viscose","Polyamide"]

short_cat = [YarnObj.Yarn("Pound of Love",["Red","Orange","Yellow","Green","Blue","Purple","Pink","Brown"],
                            ["Solid","Heather"],["Acrylic"],4,13.99,1020,{"Crochet":"J","Knit":"5.5"}),
               YarnObj.Yarn("Ferris Wheel",["Ombre"],["Tweed"],["Acrylic"],4,4.99,
                            270,{"Crochet":"H","Knit":"4.5"}),
             YarnObj.Yarn("Mandala", ["Multi", "Ombre"], ["Solid"], ["Acrylic"], 3, 8.99,
                          590, {"Crochet": "H", "Knit": "3.75"})]
#Yarn count:18
# 1st 18 yarns by audrey
# rest of yarns by xochitl
reduced_cat = [YarnObj.Yarn("Wool-Ease Thick and Quick",["Red","Orange","Yellow","Green","Blue","Purple","Pink",
                "Black","White","Brown","Gray"],["Solid","Tweed"],["Acrylic","Wool"],6,9.99,106,{"Crochet":"N","Knit":"13"}),
               YarnObj.Yarn("Heartland",["Red","Yellow","Green","Blue","Purple","Pink","White","Brown"],
                            ["Heather","Tweed"],["Acrylic"], 4,6.99,251,{"Crochet":"J","Knit":"5.5"}),
               YarnObj.Yarn("Mandala",["Multi","Ombre"],["Solid"],["Acrylic"],3,8.99,
                            590,{"Crochet":"H","Knit":"3.75"}),
               YarnObj.Yarn("24/7 Cotton",["Red","Yellow","Green","Blue","White","Black"],["Solid"],
                            ["Cotton"],4,5.99,186,{"Crochet":"G","Knit":"4"}),
               YarnObj.Yarn("Pound of Love",["Red","Orange","Yellow","Green","Blue","Purple","Pink","Brown"],
                            ["Solid","Heather"],["Acrylic"],4,13.99,1020,{"Crochet":"J","Knit":"5.5"}),
               YarnObj.Yarn("Ferris Wheel",["Ombre"],["Tweed"],["Acrylic"],4,4.99,
                            270,{"Crochet":"H","Knit":"4.5"}),
               YarnObj.Yarn("Hometown",["Red","Yellow","Green","Blue","Pink","Gray","White","Black"],["Solid","Tweed","Heather"],
                            ["Acrylic","Rayon"],6,5.99,81,{"Crochet":"N","Knit":"9"}),
               YarnObj.Yarn("Coboo",["Yellow","Green","Blue","Pink","Black","Gray"],["Solid"],
                            ["Bamboo","Cotton","Rayon"],3,5.99,232,{"Crochet":"G","Knit":"4"}),
               YarnObj.Yarn("Feels Like Butta",["Yellow","Blue","Pink","Black","White"],["Solid"],["Polyester"],
                            4,4.99,218,{"Crochet":"G","Knit":"4.5"}),
               YarnObj.Yarn("Homespun",["Multi"],["Solid","Heather"],["Acrylic","Polyester"],5,
                            8.99,185,{"Crochet":"K","Knit":"6"}),
               YarnObj.Yarn("Mandala Gradient",["Ombre"],["Solid"],["Acrylic","Nylon"],4,8.99,
                            295,{"Crochet":"I","Knit":"4"}),
               YarnObj.Yarn("Scarfie",["Mulit","Ombre"],["Solid","Tweed"],["Acrylic","Wool"],5,11.99,
                            312,{"Crochet":"K","Knit":"5.5"}),
               YarnObj.Yarn("Cover Story",["Multi"],["Solid"],["Polyester"],6,34.99,547,
                            {"Crochet":"N","Knit":"8"}),
               YarnObj.Yarn("Baby Soft",["Yellow","Green","Blue","Pink","White","Multi"],["Solid","Heather"],
                            ["Acrylic","Nylon","Rayon"],3,7.99,459,{"Crochet":"G","Knit":"4"}),
               YarnObj.Yarn("Go for Faux",["Blue","Pink","Brown","White","Gray","Black"],["Solid"],["Polyester"],
                            6,7.99,65,{"Crochet":"N","Knit":"9"}),
               YarnObj.Yarn("Landscapes",["Ombre"],["Solid"],["Acrylic"],4,6.99,147,
                            {"Crochet":"K","Knit":"6"}),
               YarnObj.Yarn("Go for Fleece Sherpa",["Red","Yellow","Blue","Black","White"],["Solid"],["Polyester"],
                            7,8.99,89,{"Crochet":"Q","Knit":"10"}),
               YarnObj.Yarn("Wool-Ease Aire",["Orange","Green","Blue","Purple","Black"],["Solid"],
                            ["Acrylic","Polyester","Wool"],6,7.99,218,{"Crochet":"J","Knit":"6"}),
               YarnObj.Yarn("Hue + Me Yarn", ["Beige", "Gray", "Blue", "Yellow", "Red", "Pink", "Teal", "Black", "Green", "Purple"], ["Solid"],
                            ["Acrylic", "Wool"], 5, 7.99, 137, {"Crochet": "K", "Knit": "10.5"}),
               YarnObj.Yarn("Color Theory",["White", "Blue", "Brown", "Purple", "Green", "Yellow"],["Solid"],
                            ["Acrylic"],4,6.99,246,{"Crochet":"I","Knit":"7"}),
               YarnObj.Yarn("Ice Cream",["Multi"],["Multi"],
                            ["Acrylic"],3,5.99,394,{"Crochet":"H","Knit":"5"}),
               YarnObj.Yarn("Touch of Alpaca",["Pink", "Yellow", "Gray", "Red", "Purple", "Black", "Green"],["Solid"],
                            ["Acrylic","Alpaca"],4,6.99,207,{"Crochet":"I","Knit":"7"}),
               YarnObj.Yarn("Feels Like Bliss",["White", "Blue", "Beige", "Gray", "Orange", "Yellow", "Purple"],["Solid"],
                            ["Nylon"],5,8.99,109,{"Crochet":"N","Knit":"11"}),
               YarnObj.Yarn("Pima Cotton",["White", "Blue", "Orange", "Puprle", "Multi", "Pink", "Gray"],["Solid", "Multi"],
                            ["Cotton"],4,7.49,186,{"Crochet":"I","Knit":"8"}),
               YarnObj.Yarn("Bundle of Love",["Multi"],["Multi"],
                            ["Acrylic"],4,13.99,688,{"Crochet":"J","Knit":"8"}),
               YarnObj.Yarn("Jeans",["Orange", "Blue", "Gray", "Black"],["Solid"],
                            ["Acrylic"],4,6.99,246,{"Crochet":"I","Knit":"7"}),
               YarnObj.Yarn("Stitch Soak Scrub",["Blue", "Pink", "Purple", "Gray", "Red", "Orange", "Black", "Green", "Yellow"],["Solid"],
                            ["Nylon"],4,3.99,92,{"Crochet":"H","Knit":"8"}),
               YarnObj.Yarn("Merino Yak Alpaca",["Blue", "Brown", "Gray", "Black", "Red", "Pink"],["Solid"],
                            ["Merino", "Alpaca", "Yak"],4,8.99,126,{"Crochet":"H","Knit":"7"}),
               YarnObj.Yarn("Mandala Sparkle",["Multi"],["Multi"],
                            ["Acrylic","Mettalic Poly"],3,8.99,328,{"Crochet":"H","Knit":"5"}),
               YarnObj.Yarn("Off The Hook",["White", "Black", "Gray", "Multi"],["Solid", "Multi"],
                            ["Polyester"],7,5.99,100,{"Crochet":"T","Knit":"11"}),
               YarnObj.Yarn("Landscapes Renewed",["Multi"],["Multi"],
                            ["Polyester"],4,10.99,232,{"Crochet":"I","Knit":"9"}),
               YarnObj.Yarn("Viscose Wrap Cone",["White", "Red", "Blue", "Purple", "Gray", "Black"],["Solid"],
                            ["Viscose"],1,23.95,2000,{"Crochet":"B","Knit":"3.5"}),
               YarnObj.Yarn("Yooge Yarn",["Green", "Blue", "Pink", "Beige", "Black"],["Solid"],
                            ["Polyamide", "Cotton"],7,102.99,109,{"Crochet":"T","Knit":"11"}),
               YarnObj.Yarn("Re-Up Bonus Bundle",["Blue", "White", "Pink", "Black", "Beige", "Green", "Brown"],["Solid"],
                            ["Polyester","Cotton"],4,14.99,651,{"Crochet":"I","Knit":"7"})
               ]


#project size
project_size = [YarnObj.Size("hat", {1:[250,325], 2: [250,325], 3: [200,225], 4: [125,200], 5: [125,150], 7: 30-60}),
                YarnObj.Size("scarf", {1: [525,825], 2: [450,625], 3: [375,500], 4: [375,400], 5: [250,375], 6: [250,375], 7: [125,200]}),
                YarnObj.Size("socks", {1: [350,500], 2: [300,450], 3: [275,400], 4: [275,375], 5: [250,350], 6: [200,250], 7:[175,200]}),
                YarnObj.Size("shawl", {1: [550,850], 2: [450,700], 3: [400,625], 4: [375,550], 5: [350,500], 6: [350,475], 7: [300,400]}),
                YarnObj.Size("sweater", {1: [3375,3375], 2: [1750,2625], 3: [1500,2250], 4: [1125,1625], 5: [950,1125], 6: [825,1125], 7: [825, 1125]}),
                YarnObj.Size("baby blanket", {1: [1500,1625], 2: [3500, 3750], 3: [3000, 3500], 4: [2250, 3125], 5: [2000,2250], 6: [1625,2000], 7: [1375,1625]}),
                YarnObj.Size("afghan", {1: [3750,4125], 2:[3500,3750], 3:[3000,3500], 4: [2250,3125], 5: [2000,2250], 6: [1625,2000], 7: [1375,1625]})]


