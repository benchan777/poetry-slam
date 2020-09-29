import random

lines_list = {}

def get_file_lines(filename):
    with open(filename, "r") as openfile:
        line = openfile.readlines()
        line_count = 1
        for i in line:
            lines_list[line_count] = i
            line_count += 1
    return lines_list

def lines_printed_backwards(lines_list):
    for key, value in reversed(lines_list.items()):
        print(f"{key}: {value}")

def lines_printed_random(lines_list):
    line_count = 1
    while line_count <= len(lines_list):
        index = random.randint(1, len(lines_list))
        print(f"{index}: {lines_list[index]}")
        line_count += 1

def lines_printed_custom(lines_list):
    word_list = []
    word_list_split = []
    for key, value in lines_list.items():
        word_list.append(value)
    poem_string = ''.join(word_list)
    word_list_split = poem_string.split()
    
get_file_lines("poem.txt")
lines_printed_backwards(lines_list)
lines_printed_random(lines_list)
lines_printed_custom(lines_list)