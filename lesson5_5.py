from random import randrange

file = 'text_5.txt'
r_numbers = [randrange(1, 100) for _ in range(5)]

with open(file, 'w', encoding="utf-8") as output_data:
    output_data.write(" ".join(map(str, r_numbers)))

with open(file) as input_data:
    numbers = input_data.read().split()

my_f = open(file,'r', encoding="utf-8")
while True:
    content = my_f.read(1024)
    print(content)
    if not content:
        break

print(sum(float(x) for x in numbers))



