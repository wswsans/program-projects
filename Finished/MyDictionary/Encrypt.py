#!/usr/bin/python3.6
#! coding: utf-8

strMinus = lambda txt, minus, big=True: ''.join([s for s in (txt if big else txt.lower()) if s != minus])
nSplit = lambda ls, Num: [ls[idx:idx + Num] for idx in range(0,len(ls), Num)]
### MakeDictionary
# Strings = [X for X in '1234567890-^¥qwertyuiop@[asdfghjkl;:]zxcvbnm,./_!"#$%&\'()=~|QWERTYUIOP`{ASDFGHJKL+*}ZXCVBNM<>?¡™£¢∞§¶•ªº–≠\\œ∑´®†¨ˆøπ“‘åß∂ƒ©˙∆˚¬…æ«Ω≈ç√∫˜µ≤≥÷⁄€‹›ﬁﬂ‡°·‚—±Œ„‰ˇÁØ∏”’ÅÍÎÏ˝ÓÔÒÚÆ»¸˛Ç◊ı˜Â¯˘¿ \n\t']
# Translater = { Word: ('0' * 8 * 3 + Bin)[-24:]  for Word, Bin in zip(Strings, [format(ord(X), 'b') for X in Strings])}
# revTranslater = {Binary:Strings for Strings, Binary in Translater.items()}
class Encryption:
	def __init__(self):
		self.__Free = None
		# print('Encryption Loaded!')

	def help(self, module=''):
		if module:
			try:
				return {
					'encrypt': 'encrypt [encode: en, decode: de], Coes, Passwd',
					'changePasswd': 'changePasswd Codes, OldPasswd, NewPasswd'
				}[module]
			except KeyError:
				return False
		else:
			return 'Wait'

	def encrypt(self, mode, Codes: str, Passwd: str):
			self.__Free = [ # To ten
				# [int(Translater[string], 2) for string in (Passwd * (len(Codes)//len(Passwd) + 1))[:len(Codes)]] ##### Passwd
				[ord(string) for string in (Passwd * (len(Codes)//len(Passwd) + 1))[:len(Codes)]] ##### Passwd
			]
			if mode == 'en':
				self.__Free.append([ord(string) for string in Codes])
				# self.__Free.append([int(Translater[string], 2) for string in Codes])
				return ' '.join(nSplit( 'I'.join( reversed( [format(self.__Free[1][Num] * self.__Free[0][Num], 'b') for Num in range(len(Codes))] ) ), 5))
				# return 'I'.join( [ format(int(Rev), 'b') for Rev in reversed( [self.__Free[1][Num] * self.__Free[0][Num] for Num in range(len(self.__Free[1]))] ) ] )
				#return '-=='.join( reversed( ''.join([''.join(list(tup)) for tup in {self.__Free[0][Num]:self.__Free[1][Num] for Num in range(len(self.__Free[0]))}.items()]) ) )
			elif mode == 'de':
				self.__Free.append(list(reversed(strMinus(Codes, ' ').split('I'))))
				return ''.join([ chr(Binary) for Binary in [(int(E, 2) // int(P)) for E, P in zip(self.__Free[1], self.__Free[0])] ] )
				# return ''.join([ revTranslater[Binary] for Binary in [('0' * 8 * 3 + Code)[-24:] for Code in [format(int(self.__Free[1][Num], 2) // self.__Free[0][Num], 'b') for Num in range(len(self.__Free[1]))] ] ] )
				# return ''.join( [revTranslater[Res] for Res in reversed([ ('0' * 8 * 3 + format(int(self.__Free[1][Num], 2) // self.__Free[0][Num], 'b'))[-24:] for Num in range(len(self.__Free[1])) ])] )
				# return ''.join([revTranslater[('0' * 24 + format(int(string), 'b'))[-24:]] for string in reversed(Codes.split('-=='))])
			else:
				print('encrypt [encode: en, decode: de], Coes, Passwd')
				return False

	def changePasswd(self, Codes: str, OldPasswd: str, NewPasswd: str):
		return self.encrypt('de', self.encrypt('en', Codes, OldPasswd), NewPasswd)

if __name__ == '__main__':
	from sys import argv
	mode = Code = Pass = Result = None
	Loop = None
	CMD = {'-m': 'mode', '-c': 'Code', '-p': 'Passwd'}
	for ARG in argv:
		if Loop == 'mode':
			mode = ARG
		elif Loop == 'Code':
			with open(ARG, mode='r', encoding='utf-8') as f:
				Code = f.read()
		elif Loop == 'Passwd':
			with open(ARG, mode='r', encoding='utf-8') as f:
				Pass = f.read()
		if ARG in CMD.keys():
			Loop = CMD[ARG]
			continue
		Loop = None
	if mode is None:
		mode = input('Mode(encode: en, decode: de): ')
	if Code is None:
		Code = input('Code: ')
	if Pass is None:
		Pass = input('Pass: ')
	print(Encryption().encrypt(mode=mode, Codes=Code, Passwd=Pass))