import os

file_name = input()


def read_file(file_name):
    with open(file_name, 'r', encoding="utf-8") as lines:
        line = lines.readline()
    os.rename(file_name, 'example4.txt')
    return line


print(read_file(file_name))
