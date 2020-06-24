# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.

with open("text_6.txt", "r", encoding="utf-8") as f:
    base_f = f.readlines()
    print(base_f)
    dict_lessons = {}
    for i in base_f:
        lessons = i.split()
        lesson = lessons[0]
        lesson = lesson[:-1]
        nums = []
        for el in lessons[1:]:
            if el != '-':
                try:
                    int_el = int(el[:2])
                except ValueError:
                    int_el = int(el[:1])
                nums.append(int_el)
            num = sum(nums)
        dict_lessons[lesson] = num

    print(dict_lessons)


