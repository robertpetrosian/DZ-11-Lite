import os
import shutil

def show_cwd():
    '''
    печать содержимого текущего каталога
    '''
    lst_out = []
    for item in os.listdir():
        if os.path.isdir(item):
            lst_out.append(f'Dir {item}')
        else:
            lst_out.append(f'File {item}')
    lst_out.sort()
    for item in lst_out:
        print(item)

def cd_cwd():
    '''
    смена текущего каталога
    '''

    new_cwd = input('Введите целевой каталог: ')
    try:
        os.chdir(new_cwd)
    except NotADirectoryError :
        print(f'{new_cwd} не является каталогом')
    except PermissionError :
        print(f'{new_cwd} не доступен для пользователя')
    else:
        print(f'Новый текущий каталог {new_cwd}')

def cr_file():
    '''
    создание файла или каталога
    '''

    what_want = input('Введите 1 - создать файл, 2 - создать каталог, любой символ - отказ ')
    if what_want == '1':
        new_file = input('Введите имя нового файла: ')
        try:
            f = open(new_file, 'w')
            f.close()
        except OSError:
            print(f'Файл {new_file} не может быть создан')
        else:
            print(f'Файл {new_file} создан')
    elif what_want == '2':
        new_cwd = input('Введите имя нового каталога: ')
        try:
            os.mkdir(new_cwd)
        except FileExistsError:
            print(f'{new_cwd} уже существует')
        except FileNotFoundError:
            print(f'{new_cwd} не имеет родительского каталога')
        else:
            print(f'Новый каталог {new_cwd}')

def del_file():
    name_of_match = input('Введите имя файла или папки ')
    if os.path.isdir(name_of_match) :
        try:
            os.rmdir(name_of_match)
        except FileNotFoundError:
            print(f'Каталог {name_of_match} не существует')
        except OSError:
            print(f'Каталог {name_of_match} не пустой')
        else:
            print(f'Каталог {name_of_match} удален')
    else:
        try:
            os.remove(name_of_match)
        except FileNotFoundError:
            print(f'Файл {name_of_match} не существует')
        else:
            print(f'Файл {name_of_match} удален')

def cp_file():
    name_of_file_from = input('Введите имя исходного файла ')
    name_of_file_to = input('Введите имя целевого файла или каталога ')
    try:
        ret = shutil.copy(name_of_file_from, name_of_file_to)
    except OSError:
        print(f'Файл {name_of_file_from} не может быть скопирован. Проверьте наличие и права доступа целевого объекта')
    else:
        print(f'Файл {ret} успешно скпирован')
def show_folders():
    lst_matches = os.listdir()
    counter = 0
    for item in lst_matches:
        if os.path.isdir(item):
            counter += 1
            print(item)
    if counter == 0:
        print(f'Каталоги отсутствуют')

def show_files():
    lst_matches = os.listdir()
    counter = 0
    for item in lst_matches:
        if not os.path.isdir(item):
            counter += 1
            print(item)

    if counter == 0:
        print(f'Файлы отсутствуют')


def submenu_1():
    '''
    ф-я высвечивает подпункты первого меню
    запрашивает и возвращает выбранный пункт подменю
    '''
    while True :
        print('Работа с файлами и папками: ')
        print(' 1. Просмотр содержимого рабочей директории\n',
              '2. Смена рабочей директории\n',
              '3. Создать файл или папку\n',
              '4. Удалить (файл/папку)\n',
              '5. Копировать (файл/папку)\n',
              '6. Посмотреть только папки\n',
              '7. Посмотреть только файлы\n',
              '8. Выход в главное меню\n')
        ret = input('Выберите пункт меню: ')
        if len(ret) != 1 or ret not in '12345678':
            continue
        elif ret=='1':
            show_cwd()
        elif ret == '2':
            cd_cwd()
        elif ret == '3':
            cr_file()
        elif ret == '4':
            del_file()
        elif ret == '5':
            cp_file()
        elif ret == '6':
            show_folders()
        elif ret == '7':
            show_files()
        else:
            break

