WArg = 0
WVal = 1
WDes = 2
WMet = 3

WOption = {

	'Main':{
	    '-s':['strServer', '127.0.0.1', '<Server> Example:111.222.333.444'],
	    '-n':['strNamespace', 'root\default', '<NameSpace> Example:/root/cimv2'],
	    '-u':['strUser', None, '<User> Example:UserName'],
	    '-p':['strPassword', None, '<Password> Example:Password'],
	    '-l':['strLocale', None, '<Locale> Example:MS_xxxx'],
	    '-a':['strAuthority', None, '<Authority> Example:Kerberos:DOMAIN or NTLMDomain:DOMAIN'],
	    '-S':['iSecurityFlags', None, '<SecurityFlags> Example:0 or 128']
	},

	'WQL':{
		'<WQL>':[None, None, 'Example:SELECT * FROM Win32_Process'],
		'q':[None, None, 'quit']
	},

	'choose':{
		'<number>':[None, None, 'Example:0 or 1 or ...'],
		'q':[None, None, 'quit']
	},

	'ObjectOperate':{
		'Q':['Qualifier', None, 'Object\'s qualifiers'],
		'P':['Property', None, 'Object\'s properties'],
		'M':['Method', None, 'Object\'s methods'],
		'q':[None, None, 'quit']
	}

}