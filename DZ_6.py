# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text


def int_func(text):
    list_text = list(text)
    for i in list_text:
        if ord(i) < 97 or ord(i) > 122:
            print('Некоретный ввод. Принимаются только маленьких латинских букв')
            break
        else:
            text = text.title()
            return text


#text = input('введите слово из маленьких латинских букв ')
#print(int_func(text))


# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def title_sentence(sentence):
    sentence_list = sentence.split()
    new_sentence_list = []
    for word in sentence_list:
        word = int_func(word)
        new_sentence_list.append(word)
    #print(new_sentence_list)
    try:
        new_sentence = ' '.join(new_sentence_list)
    except TypeError:
        print("ошибка")
    else:
        #print(new_sentence)
        return new_sentence


sentence = input("введите строку из слов, разделенных пробелом (каждое слово состоит из латинских букв в нижнем "
                 "регистре) ")
print(title_sentence(sentence))
