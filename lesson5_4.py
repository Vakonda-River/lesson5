file: str = input("Введите имя файла (пример = ххх.txt)")

voc = {"One": "Один","Two": "Два","Three": "Три","Four": "Четыре"}

translation = []

with open("text_4.txt") as input_data:
    for line in input_data:
        name, value = line.split(' - ')
        translation.append(f"{voc[name]} - {value}")

with open(file, "w", encoding="utf-8") as output_data:
    output_data.writelines(translation)
