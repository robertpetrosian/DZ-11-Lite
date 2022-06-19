import json
import os
import random
import bank_acc


def test_read_hist_acc():
    '''
    тестирование read_bank_acc
    '''
    # врем файл для истории счета, чтоб не портить имеющийся
    nof = str(random.randint(1,1000))+'.json'
    bank_acc.read_hist_acc(nof)
    assert os.path.isfile(nof) # файл истории счета создан
    with open(nof) as f:
        result = json.load(f)
    assert result == [[0,0,'открытие счета']] # проверка содержания нового файла
    os.remove(nof) # удаление файла

def test_write_hist_acc():
    # врем файл для истории счета, чтоб не портить имеющийся
    nof = str(random.randint(1,1000))+'.json'
    bank_acc.write_hist_acc(nof,[[1,2,'123']] )
    assert os.path.isfile(nof) # файл истории счета создан
    with open(nof) as f:
        res=json.load(f)
    assert res == [[1,2,'123']]
    res.extend([[2,3,'456']])
    res.extend([[3,4,'789']])
    bank_acc.write_hist_acc(nof,res )
    assert os.path.isfile(nof) # файл истории счета создан
    with open(nof) as f:
        res=json.load(f)
    assert type(res) == type([]) # it is list
    assert len(res) == 3 # there are 3 lines
    assert res[0] == [1,2,'123'] # first linr of history
    assert res[1] == [2,3,'456'] # second linr of history
    assert res[2] == [3,4,'789'] # third linr of history
    os.remove(nof) # clean up

def test_get_max_nom_oper():
    res = [[1,100,'test1'],
           [10,100,'test10'],
           [7,100,'test7'],
           [0,100,'test0']]
    assert bank_acc.get_max_nom_oper(res) == 10 # max nom operation
    res.pop(1)
    assert bank_acc.get_max_nom_oper(res) == 7 # max nom operation
    res.append([4,123,'qwerty'])
    assert bank_acc.get_max_nom_oper(res) == 7 # max nom operation


def test_get_sum_summa_oper():
    res = [[1,-100,'test1'],
           [10,-100,'test10'],
           [7,100,'test7'],
           [0,100,'test0']]
    assert bank_acc.get_sum_summa_oper(res) == 0 # sum of  operations
    res.append([12,1000, 'test 12'])
    assert bank_acc.get_sum_summa_oper(res) == 1000 # sum of  operations
    res.append([11,-5000, 'test 11']) #
    assert bank_acc.get_sum_summa_oper(res) == -4000 # sum of  operations
