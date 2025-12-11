# -- Task --

# Create a program that prints out every line to the song "99 bottles of beer on the wall."

# -- Requirements --

# - Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
# - Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# - Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

# -- [10/12/25] --

def bottles(value):

    vals = sorted(range(1, value + 1), reverse = True)

    for number in vals:

        if number == 1:
            print(str(number) + ' bottle of beer on the wall, ' + str(number) + ' bottle of beer! If this final bottle should happen to fall, there\'ll be no more bottles of beer on the wall!')

        else:
            print(str(number) + ' bottles of beer on the wall, ' + str(number) + ' bottles of beer! If one of these bottles should happen to fall, there\'d be ' + str(number) + ' bottles of beer on the wall!')

bottles(99)