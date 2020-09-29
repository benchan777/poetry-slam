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
        print(key, value)


get_file_lines("poem.txt")
lines_printed_backwards(lines_list)