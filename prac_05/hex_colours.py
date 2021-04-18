COLOUR_CODES = {"Aliceblue": "#f0f8ff", "coral1": "#ff7256",
                "cornsilk1": "#fff8dc", "DarkGoldenrod": "#b8860b",
                "DarkOliveGreen": "#556b2f", "DarkOliveGreen": "#556b2f",
                "DarkOliveGreen3": "#a2cd5a", "DarkOrchid": "#9932cc",
                "DarkOrchid1": "#bf3eff", "DarkSalmon": "#e9967a",
                "DarkSeaGreen1": "#c1ffc1"}
name_of_colour = input("Enter a colour you want the code for: ")
while name_of_colour != "":
    print("The code for \"{}\" is {}".format(name_of_colour, COLOUR_CODES.get(name_of_colour)))
    colour_name = input("Enter a colour you want the code for: ")
