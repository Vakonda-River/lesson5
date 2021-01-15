import json
from typing import TextIO

comp_s = []
with open("text_7.txt", encoding="utf-8") as text:
    companies = {}
    profit_l = []

    for company in text:
        name, form, incom, costs = company.split()
        profit = float(incom) - float(costs)
        companies[name] = profit
        if profit:
            profit_l.append(profit)

comp_s.append(companies)
comp_s.append({"average profit": round(sum(profit_l) / len(profit_l), 2)})
print("companies:",len(profit_l))
print(comp_s)

with open('text_777.json', 'w') as res:
    json.dump(comp_s, res, indent=2)
    res.close()
