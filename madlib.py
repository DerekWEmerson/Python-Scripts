# Allow user to put in their own madlib
# Auto detect the input types, or allow user to input them manually

def main():
    words = []
    madlibinputs()
    madlibprint(color1, adjective1, time1, adjective2, place1, food1, food2, verb1, noun1, number1)

def madlibinputs():
    # make a list, have second function "pop" values from bottom to top.
    # List of all inputs, loop over list with "var = input" followed by an append.
    color1 = input("Type a color: " )
    adjective1 = input("Type an adject: " )
    time1 = input("Type a time: " )
    adjective2 = input("Type an adject: " )
    place1 = input("Type a place: " )
    food1 = input("Type a food: " )
    food2 = input("Type a food: " )
    verb1 = input("Type a verb: " )
    noun1 = input("Type a noun: " )
    number1 = input("Type a number: " )
    words.append()

    return words
# color1, adjective1, time1, adjective2, place1, food1, food2, verb1, noun1, number1

def madlibprint(color1, adjective1, time1, adjective2, place1, food1, food2, verb1, noun1, number1):
    madlib = f"""
    Bats are so cool! They are {color1}, {adjective1} animals which \n
    have wings. They like to fly around at {time1} which makes some \n
    people scared of them. But bats are {adjective2}, and they don't want to \n
    hurt people. I have a pet bat that lives in {place1}. I like to feed him \n
    {food1} and {food2}. He likes to {verb1}. I am \n
    his favorite person, but he also likes {noun1}. I want to convince my \n
    parents to get me {number1} more bats.
    """
    print(madlib)

main()