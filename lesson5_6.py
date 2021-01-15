subjects = {}

with open('text_6.txt', encoding="utf-8") as f:
     for i in f:
         subject_info = i.split()
         name = subject_info[0].rstrip(':')
         subjects[name] = subject_info[1:]

res = {}

for key, value in subjects.items():
     res[key] = sum(
         [
             int(hours[:hours.index('(')])
             for hours in value
             if hours != '-'
         ]
     )

print(res)
