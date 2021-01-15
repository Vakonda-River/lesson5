with open("text_3.txt", encoding="utf-8") as f:
     worker_list = [worker_l.split() for worker_l in f.readlines()]

worker_inf = [{"name": worker[0],"rate": float(worker[1])} for worker in worker_list if len(worker) > 1]
print("Зарплату меньше 20'000 имеют:")
for worker in worker_inf:
     if worker['rate'] < 20000:
         print(worker['name'],worker['rate'])

sum = 0
for worker in worker_inf:
     sum  += worker['rate']

print("Средняя зарплата по фирме: ",sum/len(worker_list))