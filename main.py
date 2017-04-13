import sys
from win32com.client import Dispatch

Option = {
    '-s':'strServer',
    '-n':'strNamespace',
    '-u':'strUser',
    '-p':'strPassword',
    '-l':'strLocale',
    '-a':'strAuthority',
    '-S':'iSecurityFlags',
    '-w':'objwbemNamedValueSet'
}

class wmi:

    def __init__(self):
        self.d = dict()
        for id,i in enumerate(sys.argv):
            if id & 1:
                self.d[Option[i]]=sys.argv[id+1]
        self.sWbemLocator = Dispatch('WbemScripting.SWbemLocator')
        self.sWbemServices = self.sWbemLocator.ConnectServer(**self.d)

    def work(self):
        pass

    def ExecQuery(self):
        while True:
            query = input('WQL:>')
            if query == 'q':
                break
            try:
                sWbemObjectSet = self.sWbemServices.ExecQuery(query)
                print('Object')
                for id,sWbemObject in enumerate(sWbemObjectSet):
                    print('\tobject {0} : class = {1} name = {2}'.format(id, sWbemObject.CreationClassName, sWbemObject.Name))
                query = input('CHOOSE:>')
                if query == 'q':
                    break
                sWbemObject = sWbemObjectSet[int(query)]
                
                while True:
                    query = input('[{0}, {1}]:>'.format(sWbemObject.CreationClassName, sWbemObject.Name))
                    if query == 'q':
                        break
                    elif query == 'Q':
                        print('Qualifier')
                        for sWbemQualifier in sWbemObject.Qualifiers_:
                            print('\t{0} = {1}'.format(sWbemQualifier.name, sWbemQualifier.value))# ConvertPropertyValueToString(sWbemQualifier.value)))
                    elif query == 'P':
                        print('Property')
                        for sWbemProperty in sWbemObject.Properties_:
                            print('\t{0} = {1}'.format(sWbemProperty.name, sWbemProperty.value))
                    elif query == 'M':
                        print('Method')
                        for sWbemMethod in sWbemObject.Methods_:
                            print('\t{0}'.format(sWbemMethod.name))
                        # print(sWbemObject.GetObjectText_())
            except Exception as e:
                raise e
            else:
                pass
            

if __name__ == '__main__':
    try:
        print('usage:')
        print('\t-s <Server>\t\tExample:111.222.333.444')
        print('\t-n <NameSpace>\t\tExample:root\CIMV2')
        print('\t-u <User>\t\tExample:UserName')
        print('\t-p <Password>\t\tExample:Password')
        print('\t-l <Locale>\t\tExample:MS_xxxx')
        print('\t-a <Authority>\t\tExample:Kerberos:DOMAIN or NTLMDomain:DOMAIN')
        print('\t-S <SecurityFlags>\tExample:0 or 128')
        print('\t-w <WbemNamedValueSet>\tTypically, this is undefined.')
        print('')
        w = wmi()
    except Exception as e:
        print('somethin error!')
        exit()
    else:
        if 'strServer' in w.d:
            print('server\t\t'+w.d['strServer'])
        if 'strNamespace' in w.d:
            print('namespace\t'+w.d['strNamespace'])
        print('Connect success!')
    while True:
        try:
            w.ExecQuery()
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print('bye')
            exit()
        else:
            w.__init__()

# python main.py -s 172.24.66.150 -n /root/cimv2 -u pc -p `

# select * from win32_process