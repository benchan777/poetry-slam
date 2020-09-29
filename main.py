import random

# initialize empty dictionary
lines_list = {}

# this function opens the file and inputs all the data into the lines_list dictionary
def get_file_lines(filename):
    with open(filename, "r") as openfile:
        line = openfile.readlines()
        line_count = 1
        for i in line:
            lines_list[line_count] = i
            line_count += 1
    return lines_list

# this function prints the key and value of the dictionary in reverse order
def lines_printed_backwards(lines_list):
    for key, value in reversed(lines_list.items()):
        print(f"{key}: {value}")
        print(f"{key}: {value}", file = open("backwards poem.txt", "a"))

# this function prints out the lines of the poem in random order
def lines_printed_random(lines_list):
    line_count = 1 # initializes number of lines

    # this while loop selects a random integer between 1 and the length of the list, the prints out the line
    # repeats until the number of random lines is equal to the number of lines in the original poem
    while line_count <= len(lines_list):
        index = random.randint(1, len(lines_list))
        print(f"{index}: {lines_list[index]}")
        print(f"{index}: {lines_list[index]}", file = open("random poem.txt", "a"))
        line_count += 1

# this function appends the dictionary values into a list, joins all list items into a long string
# it then uses the sorted() function to sort all the words in the string into a list by alphabetical order
def lines_printed_custom(lines_list):
    word_list = []
    word_list_split = []
    for key, value in lines_list.items():
        word_list.append(value)
    poem_string = ''.join(word_list)
    word_list_split = poem_string.split()
    sorted_list = sorted(word_list_split)
    print(sorted_list)
    print(sorted_list, file = open("alphabetized letters.txt", "a"))

# this function prints the poem line by line with each line having the words rearranged in a random order
def lines_printed_scrambled(filename):
    temp = []
    line_count = 0
    with open(filename, "r") as openfile:
        lines = openfile.readline()
        while line_count < len(lines_list) - 1:
            for word in lines.split():
                temp.append(word)
            random.shuffle(temp)
            joined_temp = " ".join(temp)
            print(joined_temp)
            print(joined_temp, file = open("scrambled poem.txt", "a"))
            line_count += 1
            temp.clear()
            lines = next(openfile)

get_file_lines("poem.txt")

print("Welcome to the poetry slam!")
print("If you would like to read the poem in original form, please enter 1.")
print("If you would like to read the poem in reverse, please enter 2.")
print("If you would like to read the poem in random order, please enter 3.")
print("If you would like all the words of the poem sorted into alphabetical order, please enter 4.")
print("If you would like to read the poem with each line randomly rearranged, please enter 5.")

while True:
    option_select = input("Enter your selection here: ")

    if option_select == "1":
        print(lines_list)
        break
    elif option_select == "2":
        lines_printed_backwards(lines_list)
        break
    elif option_select == "3":
        lines_printed_random(lines_list)
        break
    elif option_select == "4":
        lines_printed_custom(lines_list)
        break
    elif option_select == "5":
        lines_printed_scrambled("poem.txt")
        break
    print("Please only enter a number from 1-5!")