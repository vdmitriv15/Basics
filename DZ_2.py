# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("base.txt", "r", encoding="utf-8") as base_f:
    base_list = base_f.read()
    num_str = 0
    j = 0
    for i in base_list:
        if i == "\n":
            num_str = num_str + 1
            print(j)
        j += 1


print(num_str)