import sys
from win32com.client import Dispatch

from fun import *
from var import *

class wmi:

    def __init__(self):
        for id,i in enumerate(sys.argv):
            if id & 1:
                WOption['Main'][i][WVal]=sys.argv[id+1]
        self.sWbemLocator = Dispatch('WbemScripting.SWbemLocator')
        self.sWbemServices = self.sWbemLocator.ConnectServer(**WChg('Main'))

    def work(self):
        pass

    def ExecQuery(self):
        WPrint('ExecQuery')
        WExecQuery(self.sWbemServices)

if __name__ == '__main__':
    while True:
        try:
            WPrint('Main')
            w = wmi()
        except Exception as e:
            print('Something error!\n')
            exit()
        else:
            print('Login as {0}@\\\\{1}\\{2} success!\n'.format(WOption['Main']['-u'][WVal], WOption['Main']['-s'][WVal], WOption['Main']['-n'][WVal]))

        try:
            w.ExecQuery()
        except KeyboardInterrupt as e:
            print('bye')
            exit()
        except Exception as e:
            print('ERROR:{0}\n'.format(e))

# main -s 172.24.66.150 -n /root/cimv2 -u pc -p `

# select * from win32_process