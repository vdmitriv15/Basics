# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл
import json

with open("text_7.txt", "r", encoding="utf-8") as f:
    base_f = f.readlines()
    profit_all = 0
    j = 0
    profit_dict = {}
    loss_dict = {}
    for i in base_f:
        name, name_s, revenue, cost = i.split()
        profit = int(revenue) - int(cost)
        print(name, name_s, profit)
        if profit >= 0:
            profit_all += profit
            j += 1
            profit_dict[name] = profit
        else:
            loss_dict[f"{name}, убыток"] = abs(profit)
#print(profit_all)
average_profit = profit_all / j
print(average_profit)
#print(profit_dict)
my_list = [
    profit_dict,
    {"average profit": average_profit},
    loss_dict
]
print(my_list)


with open("my_file.json", "w") as write_f:
    json.dump(my_list, write_f, indent='\t', ensure_ascii=False)
