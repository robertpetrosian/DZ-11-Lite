import author
import bank_acc
import ctrl_cwd
import os_is
import victorina


def main_menu():
    '''
    ф-я высвечивает пункты главного меню
    запрашивает и возвращает выбранный пункт меню
    '''
    ret = '0'
    while ret == '0':
        print('Главное меню:')
        print(' 1. Работа с файлами и папками\n',
              '2. Операционная система\n',
              '3. Автор программы\n',
              '4. Викторина "Угадай ДР Писателя"\n',
              '5. Мой банковский счет\n',
              '6. Выход')
        ret = input('Выберите пункт меню:')
        if len(ret) != 1 or ret not in '123456':
            ret='0'
    return ret



if __name__ == '__main__':
    'запуск главной программы '

    while True:
        ret = main_menu()
        if ret == '1':
            ctrl_cwd.submenu_1()
        elif ret == '2':
            os_is.os_uname()
        elif ret == '3':
            author.author_of_prg()
        elif ret == '4':
            victorina.dr_writers()
        elif ret == '5':
            bank_acc.ctrl_acc()

        else:
            exit()
