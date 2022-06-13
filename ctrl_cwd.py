import os
def show_cwd():
    '''
    печать содержимого текущего каталога
    '''

    print(os.listdir() )

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

    what_want = input('Введите 1 - создать файл, 2 - создать каталог, любой символ - отказ')
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
    name_of_match = input('Введите имя файла или папки')
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


    os.removedirs()
    return

def cp_file():
    return

def show_folders():
    return

def show_files():
    return


def submenu_1():
    '''
    ф-я высвечивает подпункты первого меню
    запрашивает и возвращает выбранный пункт подменю
    '''
    ret = '0'
    while ret == '0':
        print('Работа с файлами и папками: ')
        print(' 1. Просмотр содержимого рабочей директории\n',
              '2. Смена рабочей директории\n',
              '3. Создать папку\n',
              '4. Удалить (файл/папку)\n',
              '5. Копировать (файл/папку)\n',
              '6. Посмотреть только папки\n',
              '7. Посмотреть только файлы\n',
              '8. Выход в главное меню\n')
        ret = input('Выберите пункт меню:')
        if len(ret) != 1 or ret not in '12345678':
            ret='0'
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

