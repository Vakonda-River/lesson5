with open('text_2.txt') as f:
    lines = f.readlines()

all_lines = [a.split() for a in lines]
lines_cont = len(lines)
words_cont = sum([len(word_list) for word_list in all_lines])
print(f"Строк - {lines_cont}, слов - {words_cont}")
