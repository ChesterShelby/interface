filename = "Pyshkin.txt"

# 1. Чтение из файла (в одну строку)
with open(filename, encoding="utf-8") as file:
   data = file.read()
   print(data)

print()

# 2. Чтение из файла (в список)
with open(filename, encoding="utf-8") as file:
   data = file.readlines()
   print(data)


# 3. Чтение из файла (построчно)

with open(filename, encoding="utf-8") as file:
    f = 0
    for line in file:
        print(f, line.strip())
        f += 1