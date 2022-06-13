import os

def os_uname():
    '''
    печать ОС
    '''
    dict = os.uname()
    print(dict.sysname + ' at ' + dict.machine)
    print(dict.release)
