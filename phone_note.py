from easygui import *
f = open("nambers.txt", 'r+', encoding='utf-8')
text = f.readlines()

"""
ТЗ
на Отлично в одного человека надо сделать консольное приложение Телефонный справочник с внешним хранилищем информации, 
и чтоб был реализован основной функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.
"""


def outPutPhones(): #функция сохраняет в массив ar элементы массива text без переноса строки
    ar=[]
    for i in range(len(text)):
        if i!=len(text)-1:
            ar.append(text[i][:-1])
        else:
            ar.append(text[i])
    return ar


def windowShow(): #функция выводящая массив полученный в outPutPhones(): в окно
    ms = outPutPhones()
    msg = ''
    for l in range(len(ms)):
        msg+=ms[l]+"\n"
    title = "Просмотр книжки"
    button = "закрыть"
    msgbox(msg, title, button)


def findPhones(st): #функция проверяющая массив строк файла на полученную строку st, в случае нахождения хаписывает номер строки и ее значение
    u = []
    for i in range(len(text)):
        if st in text[i]:
            u.append(i)
            u.append(str(text[i]))
    if u == []:
        u.append("Нет результатов ")    
    return u


def windowFind(): #функция получающая строку, путем запроса ее через пользовательско окно, проверку через функцию findPhones(st): и вывод результата через окно + возращает результат работы функции findPhones(st):
    msg = "Введите атрибут"
    title = "Ввод переменной"
    fieldValues2 = enterbox(msg, title)
    msg=''
    res = findPhones(fieldValues2)
    if len(res)>1:
        for i in range(1,len(res),2):
            msg+=res[i]+"\n"
    else:
        msg=res[0]
    title = "Просмотр книжки"
    button = "Ок"
    msgbox(msg, title, button)
    return res


def changePhone(old,new): #функция которая открывает текущий файл для записи и проходится по всем элементам массива строк text записывая их в файл. И в случае равенства строки text-a и переменной old в файл записывается переменная new
    with open("nambers.txt", 'w', encoding='utf-8') as refile:
        for i in range(len(text)):
            if text[i] != old[1]:
                refile.write(text[i])
            else:
                refile.write(new+"\n")
   

def check(): #функция получает найденный массив от windowFind(), проверяет и в удволитворительном случае возращает массив
    while True:
        num = windowFind()
        if len(num) > 2:
            msg = "Поиск выдал несколько контактов. Утончните данные"
            title = "Ошибка"
            button = "Ок"
            msgbox(msg, title, button)
        elif num[0] == "Нет результатов ":
            continue
        else:
            break
    return num


def deletePhone(): #функция получает массив от check(), создает окно подтверждения и перезаписывает файл не включая элемент массива res
    res = check()
    msg=''
    title = "Просмотр книжки"
    for j in range(1,len(res),2):
        msg+=res[j]+"\n"
    buttons = ("Удалить","Отмена")
    choice = buttonbox(msg, title, buttons)
    if choice == "Удалить":
        with open("nambers.txt", 'w+', encoding='utf-8') as refle:
            for i in range(len(text)):
                if text[i] != res[1]:
                    refle.write(text[i])


def importPhones(imfile): #функция получает имя файла и записывает его элементы, если таких элементов нет в основном файле
    with open(imfile, 'r', encoding='utf-8') as refile:
        textImport = refile.readlines()
        for i in range(len(textImport)):
            if findPhones(textImport[i])[0] == "Нет результатов":
                f.write(textImport[i])

#importNumbers.txt

def importPhonesWindow(): #функция создает окна ввода имени файла, а так же результат работы importPhones(imfile)
    while True:
        msg = "Введите название импортированного файла с указанием расширения"
        title = "Ввод переменной"
        imfile = enterbox(msg, title)
        if imfile != None:
            try:
                importPhones(imfile)
                msg = "Успешно"
                title = "Информация"
                button = "закрыть"
                msgbox(msg, title, button)
                break
            except Exception as e: 
                print(e)
                msg = "Ошибка"
                title = "Информация"
                a = buttonbox(msg, title, choices=('Закрыть', 'Повторить'))
                if a == 'Закрыть':
                    break
        else:
            break


def checkInput(): #функция создает окно ввода 4х атрибутов и проверяет правильность их ввода
    while True:
        msg = 'Пожалуйста, заполните следующую контактную информацию'
        title = 'Учетный центр'
        fieldNames = ["Номер телефона*", "Имя*", "Доп. сведения", "Почта"]
        fieldValues = multenterbox(msg, title, fieldNames)
        num = ''.join(fieldValues[0].split())
        if fieldValues == ['', '', '', '']:
            msg = "Введено пустое значение"
        elif fieldValues[0] == '' or fieldValues[1] == '':
            msg = "Нужно указать ключевые атрибуты(номер телефона и имя)"
        elif num.isdigit() == False:
            msg = "Номер введен неправильно"
        else:
            resmsg = ""
            for i in range(len(fieldValues)):
                if fieldValues[i] == "":
                    resmsg += ('_ ')
                else:
                    resmsg+=fieldValues[i]+"   "
            if findPhones(resmsg)[0] != "Нет результатов ":
                msg = "Данная запись уже есть"  
            else:
                return resmsg
        title = "Ошибка" 
        button = "Ок" 
        msgbox(msg, title, button)


def inputInPhone(): #функция получает строку из checkInput(), записывает ее в файл и выводит информацию в окно
    resmsg = checkInput()
    title = "Просмотр книжки"
    button = "Ok"
    msgbox("Контакт: " + resmsg + " сохранен", title, button)
    f.write(resmsg)
    f.write('\n')           


def changePhoneWindow(): #функция получает значения old из check() и new из checkInput(), посылает в changePhone(old, new) и выводит информацию в окно
    old = check()
    new = checkInput()
    changePhone(old, new)
    msg = "Готово"
    title = "Информация"
    button = "закрыть" 
    msgbox(msg, title, button)

     
def mainWindow(): #функия выводящая пользователю меню с выбором функций
    while True:
        try:
            a = choicebox(msg='Выберете опцию', title='Контакты', choices=('просмотр', 'сохранение', 'импорт', 'поиск', 'удаление', 'изменение данных'))
            if a == 'просмотр': #+
                windowShow()
            if a == 'сохранение': #+
                inputInPhone()
            if a == 'импорт': #+
                importPhonesWindow() 
            if a == 'поиск': #+
                windowFind()
            if a == 'удаление': #+
                deletePhone()
            if a == 'изменение данных': #+
                changePhoneWindow()
            if a == None:
                break
        except:
            continue

mainWindow()

f.close()