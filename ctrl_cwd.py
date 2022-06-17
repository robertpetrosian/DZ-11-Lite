import os
import shutil

def show_cwd():
  '''получить содержимого текущего каталога'''
  return os.listdir()

def cd_cwd(new_cwd):
    ' смена текущего каталога '
    ret =''
    try:
        os.chdir(new_cwd)
    except NotADirectoryError :
        ret = f'{new_cwd} не является каталогом'
    except PermissionError :
        ret = f'{new_cwd} не доступен для пользователя'
    except FileNotFoundError :
        ret = f'{new_cwd} не существует'
    return ret

def cr_file(new_file):
    'создание файла'
    ret = ''
    try:
        f = open(new_file, 'w')
        f.close()
    except OSError:
        ret = f'Файл {new_file} не может быть создан'
    return ret

def cr_folder(new_folder):
    ' создание каталога '
    ret = ''
    try:
        os.mkdir(new_folder)
    except FileExistsError:
        ret = f'{new_folder} уже существует'
    except FileNotFoundError:
        ret = f'{new_folder} не имеет родительского каталога'
    return ret

def del_file(name_of_match):
    ret = ''
    if os.path.isdir(name_of_match) :
        try:
            os.rmdir(name_of_match)
        except FileNotFoundError:
            ret = f'Каталог {name_of_match} не существует'
        except OSError:
            ret = f'Каталог {name_of_match} не пустой'
    elif os.path.isfile(name_of_match):
        try:
            os.remove(name_of_match)
        except FileNotFoundError:
            ret = f'Файл {name_of_match} не существует'
    else:
        ret = f'{name_of_match} не является Файлом или каталогом'
    return ret


def cp_file(name_of_file_from, name_of_file_to) :
    ret = ''
    try:
        shutil.copy(name_of_file_from, name_of_file_to)
    except OSError :
        ret = f'Файл {name_of_file_from} не скопирован. Проверьте наличие и права доступа целевого объекта'

    return ret

def show_folders():
    lst_out =[]
    lst_matches = os.listdir()
    for item in lst_matches:
        if os.path.isdir(item):
            lst_out.append(item)
    lst_out.sort()
    return lst_out

def show_files():
    lst_out =[]
    lst_matches = os.listdir()
    for item in lst_matches:
        if os.path.isfile(item):
            lst_out.append(item)
    lst_out.sort()
    return lst_out

def submenu_1():
    '''
    ф-я высвечивает подпункты первого меню
    запрашивает и возвращает выбранный пункт подменю
    '''
    while True :
        print('Работа с файлами и папками: ')
        print(' 1. Просмотр содержимого рабочей директории\n',
              '2. Смена рабочей директории\n',
              '3. Создать файл\n',
              '4. Создать каталог\n',
              '5. Удалить (файл/каталог)\n',
              '6. Копировать (файл/каталог)\n',
              '7. Посмотреть только каталоги\n',
              '8. Посмотреть только файлы\n',
              '9. Выход в главное меню\n')
        ret = input('Выберите пункт меню: ')
        if len(ret) != 1 or ret not in '123456789':
            continue
        elif ret =='1':
            print(f'Рабочая директория {os.getcwd()}')
            lst = show_cwd()
            lst_out=[]
            for item in lst:
                if os.path.isdir(item):
                    lst_out.append(f'Dir {item}')
                else:
                    lst_out.append(f'File {item}')
            lst_out.sort()
            for item in lst_out:
                print(item)
        elif ret == '2':
            new_cwd = input('Введите новый рабочий каталог: ')
            error = cd_cwd(new_cwd)
            if error == '':
                print(f'Текущий каталог {new_cwd}')
            else:
                print(f'Текущий каталог не изменён. Ошибка {error}')

        elif ret == '3':
            new_file = input('Введите имя нового файла: ')
            error = cr_file(new_file)
            if error == '':
                print(f'Файл {new_file} создан')
            else:
                print(f'Ошибка {error}. Файл {new_file} не создан')

        elif ret == '4':
            new_folder = input('Введите имя нового каталога: ')
            error = cr_folder(new_folder)
            if error == '':
                print(f'каталог {new_folder} создан')
            else:
                print(f'Ошибка {error}. каталог {new_folder} не создан')

        elif ret == '5':
            name_of_match = input('Введите имя файла или папки ')
            error = del_file(name_of_match)
            if error == '':
                print(f'Файл / каталог {name_of_match} удален')
            else:
                print(f'Ошибка {error} каталог {name_of_match} не удален')

        elif ret == '6':
            name_of_file_from = input('Введите имя исходного файла ')
            name_of_file_to = input('Введите имя целевого файла или каталога ')
            error = cp_file(name_of_file_from , name_of_file_to )
            if error == '':
                print(f'Файл / каталог {name_of_file_from} скопирован в {name_of_file_to}')
            else:
                print(f'Ошибка {error}. Файл {name_of_file_from} не скопирован')

        elif ret == '7':
            lst = show_folders()
            if len(lst) == 0:
                print('Каталогов не существует')
            else:
                for item in lst:
                    print(item)
        elif ret == '8':
            lst = show_files()
            if len(lst) == 0 :
                print('Файлов не существует')
            else:
                for item in lst:
                    print(item)
        else:
            break


if __name__ == '__main__' :
    submenu_1()