import random
import os

import ctrl_cwd


def test_show_cwd():
    assert type(ctrl_cwd.show_cwd()) == type([]) # тип возвращаемого значения list
    assert ctrl_cwd.show_cwd() == os.listdir() # содержание

def test_cd_cwd():
    new_folder = 'folder-'+str(random.randint(1,1000)) #random name of folder
    assert ctrl_cwd.cd_cwd(new_folder) == f'{new_folder} не существует' # error

    ''' запоминаем текущий каталог, ищем хотя бы один существующий , переходим в него, возвращаемся'''
    cur_folder = os.getcwd()
    lst = os.listdir(cur_folder)
    for item in lst:
        if os.path.isdir(item):
            assert ctrl_cwd.cd_cwd(item) == ''  # change dir into existing dir
            assert ctrl_cwd.cd_cwd(cur_folder) == ''  # return to source dir
            break


def test_cr_folder():
    '''проверка 3х функций создание, проверка и удаление каталога, чтобы сама проверка была чистой функцией'''
    cur_folder = os.getcwd() # запоминаем текущий каталог
    new_folder = 'folder-'+str(random.randint(1,1000)) #random name of folder
    assert ctrl_cwd.cr_folder(new_folder) == '' # dir new_folder has been created , no error
    assert os.path.exists(cur_folder) # dir new_folder exists
    os.rmdir(new_folder)  # dir new_folder has been deleted

def test_cr_file():
    ''' проверка создания и удаления файла '''
    new_file = 'file-'+str(random.randint(1,1000)) #random name of file
    assert ctrl_cwd.cr_file(new_file) == '' # ile has been created succesfully
    assert os.path.exists(new_file) # file exists
    os.remove(new_file) # clean up
    assert not os.path.exists(new_file) # file exists

def test_del_file():
    new_folder = 'folder-'+str(random.randint(1,1000)) #random name of folder
    os.mkdir(new_folder)
    assert ctrl_cwd.del_file(new_folder) == '' # folder has been deleted
    assert not os.path.exists(new_folder) # folder not exists

    new_file = 'file-'+str(random.randint(1,1000)) #random name of file
    os.mkdir(new_file)
    assert ctrl_cwd.del_file(new_file) == '' # file has been deleted
    assert not os.path.exists(new_file) # file not exists

def test_cp_file():
    new_file_from = 'file-'+str(random.randint(1,1000)) #random name of source file
    new_file_to   = 'file-'+str(random.randint(1,1000)) #random name of target file
    f=open(new_file_from, 'w')  # creating source file
    f.close()
    assert ctrl_cwd.cp_file(new_file_from, new_file_to) == '' # file has been copied
    assert ctrl_cwd.cp_file(new_file_from, new_file_to) == ''  # file has been rewritten
    assert os.path.exists(new_file_to) #  file exists
    os.remove(new_file_to) # clean up
    os.remove(new_file_from) # clean up

def test_show_folders():
    for item in ctrl_cwd.show_folders():
        assert os.path.isdir(item)

def test_show_files():
    for item in ctrl_cwd.show_files():
        assert os.path.isfile(item)

def test_save_cwd_to_file():
    '''проверка 3х функций создание, проверка и удаление каталога, чтобы сама проверка была чистой функцией'''
    cur_folder = os.getcwd() # запоминаем текущий каталог
    new_folder = 'folder-'+str(random.randint(1,1000)) #random name of folder
    os.mkdir(new_folder)
    os.chdir(new_folder)
    os.mkdir(new_folder)

    with open('newfile.txt','w') as f:
        f.write('')

    ctrl_cwd.save_cwd_to_file()
    with open('listdir.txt') as f:
        lines = f.readlines()

    assert len(lines) == 2 # numbers of lines in file
    assert lines[0] == 'Dirs: '+new_folder+'\n'  # first line
    assert lines[1] == 'Files: newfile.txt' # second line
    os.rmdir(new_folder)  # dir new_folder has been deleted
    os.remove('newfile.txt')
    os.remove('listdir.txt')
    os.chdir('..')
    os.rmdir(new_folder)


if __name__ == '__main__':
    test_show_files()