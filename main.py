poem_lines = {}

def get_file_lines(filename):
    with open(filename, "r") as openfile:
        line = openfile.readlines()
        line_count = 1
        for i in line:
            poem_lines[line_count] = i
            line_count += 1


# def get_file_lines(filename):
#     with open(filename, "r") as openfile:
#         lines_list = openfile.readlines()
#         print(lines_list)

def lines_printed_backwards(lines_list):
    with open("poem.txt", "r") as openfile:
        line = openfile.readlines()
        line_count = len(line)

        for i in reversed(line):
            print(f"{line_count} {i}")
            line_count -= 1


get_file_lines("poem.txt")
print(poem_lines)