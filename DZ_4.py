# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
dict_ru = {
    'Один': '1',
    'Два': '2',
    'Три': '3',
    'Четыре': '4'
}

with open("text_4.txt", "r", encoding="utf-8") as f:
    base_f = f.readlines()
    for i in base_f:
        nums_eng, l, value = i.split()
        for j, q in dict_ru.items():
            if value == q:
                num_ru = f"{j} - {q}\n"

        with open("text_44.txt", "a", encoding="utf-8") as new_f:
            new_file = new_f.writelines(num_ru)





