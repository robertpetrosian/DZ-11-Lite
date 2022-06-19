import json
import os

'''
history - история счета - 2-мерный список 
строка - одна операция , которая есть список:
номер, сумма, наименование 
'''

def write_hist_acc(f_hist, history):
    '''
    аргумент: имя файла
    файл переписываем , записываем историю
    '''
    with open(f_hist, 'w') as f:
        json.dump(history,f)

def read_hist_acc(f_hist):
    '''
    аргумент: имя файла
    если файла нет создаем и пишем открытие счета , сумма=0
    если есть считываем
    возвращает историю счета
    '''

    if not os.path.isfile(f_hist):
        with open(f_hist,'w') as f:
            json.dump([[0,0,'открытие счета']],f)

    with open(f_hist) as f:
        result = json.load(f)

    return result

def get_max_nom_oper(history):
    '''
    получить максимальный номер операции
    '''
    nom_oper=[]
    result = 0
    for i in range(len(history)):
        nom_oper.append(history[i][0])
    if len(history) != 0:
        result = max(nom_oper)
    return result

def get_sum_summa_oper(history):
    '''
    возвращает сумму операций истории
    '''
    result=0
    for item in history:
        result += item[1]
    return result

def ctrl_acc():
    '''
    управление счетом
    '''

    while True:
        print('*'*20) # псевдо-очистка окна вывода
        print(f'На счету {get_sum_summa_oper(history)} руб')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история счета')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            # пополнение счета
            sum_add = int(input('Введите сумму пополнения счета: '))
            if sum_add <= 0:
                print('Неверная сумма, повторите операцию')
            else:
                history.append([get_max_nom_oper(history)+1 ,
                                sum_add ,
                                'пополнение счета'])
        elif choice == '2':
            # покупка
            ostatok = get_sum_summa_oper(history)
            if ostatok <= 0:
                print('На счету нет средств')
            else:
                name_sub = input('Введите назаание покупки : ')
                sum_sub = int(input('Введите сумму покупки: '))
                if ostatok - sum_sub < 0:
                    print('Неверная сумма, повторите операцию')
                else:
                    history.append([get_max_nom_oper(history)+1,
                                    - sum_sub,
                                    name_sub])
        elif choice == '3':
            if get_max_nom_oper(history) == 0:
                print('У счета нет истории')

            fmt_string='{:^10} {:^10} {:^30}'
            print(fmt_string.format('Номер','Сумма','Наименование'))
            for item in history:
                print(fmt_string.format(item[0],item[1], item[2]))

        elif choice == '4':
            write_hist_acc(f_hist, history)
            break
        else:
            print('Неверный пункт меню')


if __name__ == "__main__":
    f_hist = "hist_acc.json"
    history = read_hist_acc(f_hist)
    ctrl_acc()