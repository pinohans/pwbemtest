from var import *

def WPrint(str = '', op = WDes):
    print('{0}\n'.format(str))
    if str in WOption:
        for key, value in WOption[str].items():
            print('\t{0} {1}'.format(key, value[op]))
    print('')

def WChg(str):
    if str in WOption:
        return dict(map(lambda x:(x[1][WArg],x[1][WVal]),filter(lambda x:x[1][WVal]!=None,list(WOption[str].items()))))
    else:
        return dict()

def OPrint(sWbemObjectSet):
    print('Object\n')
    for id,sWbemObject in enumerate(sWbemObjectSet):
        print('\tobject {0} : class = {1} name = {2}'.format(id, sWbemObject.CreationClassName, sWbemObject.Name))
    return sWbemObjectSet

def WExecQuery(sWbemServices):
    while True:
        query = input('WQL:>')
        if query == 'q':
            break
        sWbemObjectSet = OPrint(sWbemServices.ExecQuery(query))

        WPrint('choose')
        query = input('choose:>')
        if query == 'q':
            break

        WPrint('ObjectOperate')
        WObjectOperate(sWbemObjectSet[int(query)])

def WObjectOperate(sWbemObject):
    while True:
        query = input('[{0}, {1}]:>'.format(sWbemObject.CreationClassName, sWbemObject.Name))
        if query == 'q':
            break
        elif query == 'Q':
            print('Qualifier')
            for sWbemQualifier in sWbemObject.Qualifiers_:
                print('\t{0} = {1}'.format(sWbemQualifier.name, sWbemQualifier.value))
        elif query == 'P':
            print('Property')
            for sWbemProperty in sWbemObject.Properties_:
                print('\t{0} = {1}'.format(sWbemProperty.name, sWbemProperty.value))
        elif query == 'M':
            print('Method')
            for sWbemMethod in sWbemObject.Methods_:
                print('\t{0}'.format(sWbemMethod.name))