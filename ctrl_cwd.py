import json
import os
import shutil

def punkt_menu(func):
    '''
    декоратор , который берет первый аргумент как название пункта меню, а остальные аргументы передает ф-ии
    при вызове ф-ии передаем имя пункта меню и аргументы
    '''
    def decor(*args):
        print('*'*20)
        # try вставил для тестирования , где selected_punkt неизвестен
        try:
            print(selected_punkt[0])
        except Exception :
            print()
        result = func(*args)
        return result
    return decor

@punkt_menu
def show_cwd():
    '''
    ф-я возвращает список объектов данного каталога
    '''
    return os.listdir()

@punkt_menu
def show_folders():
    '''
    ф-я возвращает список подкаталогов данного каталога
    '''
    lst_out = [item for item in os.listdir() if os.path.isdir(item)]
    return lst_out


@punkt_menu
def show_files():
    '''
    ф-я возвращает список файлов данного каталога
    '''
    lst_out =[item for item in os.listdir() if os.path.isfile(item)]
    return lst_out

@punkt_menu
def save_cwd_to_file():
    str_files='Dirs: '+ ','.join(show_folders())
    str_dirs = 'Files: ' + ','.join(show_files())
    with open('listdir.txt','w') as f:
        f.write(str_files+'\n')
        f.write(str_dirs)

@punkt_menu
def show_cwd():
  '''получить содержимого текущего каталога'''
  return os.listdir()

@punkt_menu
def cd_cwd( cwd ):
    ' смена текущего каталога '
    ret =''
    try:
        os.chdir(cwd)
    except NotADirectoryError :
        ret = f'{cwd} не является каталогом'
    except PermissionError :
        ret = f'{cwd} не доступен для пользователя'
    except FileNotFoundError :
        ret = f'{cwd} не существует'
    return ret

@punkt_menu
def cr_file(file):
    'создание файла'
    ret = ''
    try:
        f = open(file, 'w')
        f.close()
    except OSError:
        ret = f'Файл {file} не может быть создан'
    return ret

@punkt_menu
def cr_folder( folder):
    ' создание каталога '
    ret = ''
    try:
        os.mkdir(folder)
    except FileExistsError:
        ret = f'{folder} уже существует'
    except FileNotFoundError:
        ret = f'{folder} не имеет родительского каталога'
    return ret

@punkt_menu
def del_file(match):
    ret = ''
    if os.path.isdir(match) :
        try:
            os.rmdir(match)
        except FileNotFoundError:
            ret = f'Каталог {match} не существует'
        except OSError:
            ret = f'Каталог {match} не пустой'
    elif os.path.isfile(match):
        try:
            os.remove(match)
        except FileNotFoundError:
            ret = f'Файл {match} не существует'
    else:
        ret = f'{match} не является Файлом или каталогом'
    return ret


@punkt_menu
def cp_file( name_of_file_from,  name_of_file_to) :
    ret = ''
    try:
        shutil.copy(name_of_file_from, name_of_file_to)
    except OSError :
        ret = f'Файл {name_of_file_from} не скопирован. Проверьте наличие и права доступа целевого объекта'

    return ret

def submenu_1():
    '''
    ф-я высвечивает подпункты первого меню
    запрашивает и возвращает выбранный пункт подменю
    '''
    lst_menu.append('Просмотр содержимого рабочей директории')
    lst_menu.append('Сохранить содержимое рабочей директории в файл')
    lst_menu.append('Смена рабочей директории')
    lst_menu.append('Создать файл')
    lst_menu.append('Создать каталог')
    lst_menu.append('Удалить (файл/каталог)')
    lst_menu.append('Копировать (файл/каталог)')
    lst_menu.append('Посмотреть только каталоги')
    lst_menu.append('Посмотреть только файлы')
    lst_menu.append('Выход в главное меню')
    while True :
        ret=0
        print('Работа с файлами и папками: ')
        for i in range(len(lst_menu)):
            print(f'{i+1}. {lst_menu[i]}')
        while True:
            try:
                ret = int(input('Выберите пункт меню: '))
            except:
                print(f'Введите число от 1 до {len(lst_menu)}')
                continue
            else:
                break

        if ret ==1:
            selected_punkt.clear()
            selected_punkt.append(lst_menu[ret-1])
            print(f'Рабочая директория {os.getcwd()}')
            print('\n'.join(show_cwd()))
        elif ret == 2:
            selected_punkt.clear()
            selected_punkt.append(lst_menu[ret-1])
            save_cwd_to_file()
        elif ret == 3:
            selected_punkt.clear()
            selected_punkt.append(lst_menu[ret-1])
            new_cwd = input('Введите новый рабочий каталог: ')
            error = cd_cwd(new_cwd )
            print(f'Текущий каталог {new_cwd}' if error == ''
                  else f'Текущий каталог не изменён. Ошибка {error}')
        elif ret == 4:
            selected_punkt.clear()
            selected_punkt.append(lst_menu[ret-1])
            new_file = input('Введите имя нового файла: ')
            error = cr_file(new_file)
            print(f'Файл {new_file} создан' if error == ''
                  else f'Ошибка {error}. Файл {new_file} не создан')
        elif ret == 5:
            selected_punkt.clear()
            selected_punkt.append(lst_menu[ret-1])
            new_folder = input('Введите имя нового каталога: ')
            error = cr_folder(new_folder)
            print(f'каталог {new_folder} создан' if error == ''
                  else f'Ошибка {error}. каталог {new_folder} не создан')
        elif ret == 6:
            selected_punkt.clear()
            selected_punkt.append(lst_menu[ret-1])
            name_of_match = input('Введите имя файла или папки ')
            error = del_file(name_of_match)
            print(f'Файл / каталог {name_of_match} удален' if error == ''
                  else f'Ошибка {error} каталог {name_of_match} не удален')
        elif ret == 7:
            selected_punkt.clear()
            selected_punkt.append(lst_menu[ret-1])
            name_of_file_from = input('Введите имя исходного файла ')
            name_of_file_to = input('Введите имя целевого файла или каталога ')
            error = cp_file(name_of_file_from , name_of_file_to )
            print(f'Файл / каталог {name_of_file_from} скопирован в {name_of_file_to}' if error == ''
                  else f'Ошибка {error}. Файл {name_of_file_from} не скопирован')
        elif ret == 8:
            selected_punkt.clear()
            selected_punkt.append(lst_menu[ret-1])
            lst = show_folders()
            print('Каталогов не существует' if len(lst) == 0
                  else '\n'.join(lst))
        elif ret == 9:
            selected_punkt.clear()
            selected_punkt.append(lst_menu[ret-1])
            lst = show_files()
            print('Файлов не существует' if len(lst) == 0
                  else '\n'.join(lst))
        elif ret == 10:
            break

if __name__ == '__main__' :
    '''
    чтобы не объявлять глобальные переменные 
    список пунктов меню и выбранный пункт
    и не передавать их как параметры
    объявляем их в main функции в виде списков
    и внутри функциё делаем append и тогда они не становятся локальными
    и получают свое значение, которые видны всем ф-ям
    '''
    lst_menu = []
    selected_punkt=[]
    submenu_1()