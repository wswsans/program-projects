from getpass import getpass
from Encrypt import Encryption
Enc = Encryption()

class Account:
	def __init__(self):
		self.__AcVar = None
		print('coming soon...')

	def LOAD(PWD):
		if PWD=='POWER':
			with open('Dictionaries/10110 01111 1010I 10110 00011 0000I 11010 01000 1111I 10010 11110 1111I 11001 10011 0110I 10010 00100 110I1 10011 10101 001I1 00110 10000 100I1 10100 00011 010I1 01011 11001 011I1 01011 01010 000I1 01101 00111 111I1 01010 00100 11.mdic') as f:
				return Enc.encrypt('de', f.read(), Enc.encrypt('de', '11001 01100 0100I 10011 11101 1001I 11001 11010 1001I 11100 00111 001I1 10010 11000 100I1 00111 11011 001I1 10001 00000 000I1 10101 01111 001I1 10101 11010 01', 'SuperUser')).split('\n')

	def exist(self, User):
		try:
			self.__AcVar = self.LOAD('POWER')
			return User in self.__AcVar
		except Exception as Err:
			raise Err

	def add(self, User, Passwd, DicName):
		try:
			self.__AcVar = Enc.encrypt('en', 'w: Hello!\n\tr:World!\n', Passwd )
			with open('Dictionaries/{}.mdic'.format(Enc.encrypt('en', User + DicName, Passwd)), mode='w') as f:
				f.write(self.__AcVar)
			self.__AcVar = '\n'.join(self.LOAD('POWER'))
			with open('Dictionaries/10110 01111 1010I 10110 00011 0000I 11010 01000 1111I 10010 11110 1111I 11001 10011 0110I 10010 00100 110I1 10011 10101 001I1 00110 10000 100I1 10100 00011 010I1 01011 11001 011I1 01011 01010 000I1 01101 00111 111I1 01010 00100 11.mdic', mode='w') as f:
				self.__AcVar = Enc.encrypt('en', self.__AcVar + User + '\n', Enc.encrypt('de', '11001 01100 0100I 10011 11101 1001I 11001 11010 1001I 11100 00111 001I1 10010 11000 100I1 00111 11011 001I1 10001 00000 000I1 10101 01111 001I1 10101 11010 01', 'SuperUser'))
				f.write(self.__AcVar)
			return True
		except Exception as Err:
			print('A write error occurred')
			raise Err
	def remove(self, User, Passwd, DicName):
		try:
			with open('Dictionaries/{}.mdic'.format(Enc.encrypt('en', User + DicName, Passwd)), mode='w') as f:
				f.write('None')
			self.__AcVar = self.LOAD('POWER')
			del self.__AcVar[self.__AcVar.index(User)]
			self.__AcVar = Enc.encrypt('en', self.__AcVar, Enc.encrypt('de', '11001 01100 0100I 10011 11101 1001I 11001 11010 1001I 11100 00111 001I1 10010 11000 100I1 00111 11011 001I1 10001 00000 000I1 10101 01111 001I1 10101 11010 01', 'SuperUser'))
			with open('Dictionaries/10110 01111 1010I 10110 00011 0000I 11010 01000 1111I 10010 11110 1111I 11001 10011 0110I 10010 00100 110I1 10011 10101 001I1 00110 10000 100I1 10100 00011 010I1 01011 11001 011I1 01011 01010 000I1 01101 00111 111I1 01010 00100 11.mdic', mode='w') as f:
				f.write(self.__AcVar)
			return True
		except Exception as Err:
			print('A write error occurred')
			raise Err


class Manage:
	def __init__(self):
		self.__MDMVar = None
		self.AcData = {'User': 'None', 'Passwd': 'None', 'DicName': 'None'}
		# print('MyDictionariesManage Loaded!')

	def read(self):
		try:
			with open('Dictionaries/{0}.mdic'.format(Enc.encrypt('en', self.AcData['User'] + self.AcData['DicName'], self.AcData['Passwd']))) as f:
				self.__MDMVar = {'word': list(), 'reason': list()}
				for dic in Enc.encrypt('de', f.read(), self.AcData['Passwd']).split('\n'):
					if dic[:3] == 'w: ':
						self.__MDMVar['word'].append(dic[3:])
					if dic[:3] == '\tr:':
						self.__MDMVar['reason'].append(dic[3:])
				return {Word: Reason for Word, Reason in zip(self.__MDMVar['word'], self.__MDMVar['reason']) }
		except Exception as Err:
			raise Err

	def add(self, content: dict):
		try:
			self.__MDMVar = Enc.encrypt('en', '\n'.join( [ 'w: {0}\n\tr:{1}'.format(word, reason) for word, reason in dict( list(self.read().items()) + list(content.items()) ).items() ] ), self.AcData['Passwd'] )
			with open('Dictionaries/{0}.mdic'.format(Enc.encrypt('en', self.AcData['User'] + self.AcData['DicName'], self.AcData['Passwd'])), mode='w') as f:
				f.write(self.__MDMVar)
			return True
		except Exception as Err:
			print('A write error occurred')
			raise Err

	def remove(self, word):
		try:
			self.__MDMVar = self.read()
			del self.__MDMVar[word]
			self.__MDMVar = '\n'.join( [ 'w: {0}\n\tr:{1}'.format(word, reason) for word, reason in self.__MDMVar.items() ] )
			with open('Dictionaries/{0}.mdic'.format(Enc.encrypt('en', self.AcData['User'] + self.AcData['DicName'], self.AcData['Passwd'])), mode='w') as f:
				f.write(Enc.encrypt('en', self.__MDMVar, self.AcData['Passwd']))
			return True
		except KeyError:
			print('NotFound')
		except Exception as Err:
			print('A reomve error occurred')
			raise Err

	def show(self, word):
		try:
			return self.read()[word]
		except KeyError:
			print(word, 'NotFound')
		except Exception as Err:
			raise Err

	def makeDictionary(self):
		try:
			self.__MDMVar = Enc.encrypt('en', 'w: Hello!\n\tr:World!\n', self.AcData['Passwd'] )
			with open('Dictionaries/{0}.mdic'.format(Enc.encrypt('en', self.AcData['User'] + self.AcData['DicName'], self.AcData['Passwd'])), mode='w') as f:
				f.write(self.__MDMVar)
			return True
		except Exception as Err:
			print('A write error occurred')
			raise Err

	def reset(self):
		self.makeDictionary()


#TODO: AccountDataの簡略化, removeで，全部消えた時, 

if __name__ == '__main__':
	MDM = Manage()
	Account = Account()
	MDM.AcData = {'User': input('UName: '), 'Passwd': getpass('Password: '), 'DicName': input('DictionaryName: ')}
	print('Help: h')
	while True:
		try:
			Command = input('>> ')
			if Command == 'h':
				print('r: read, a: add, rm: remove, s: show, rs: reset, q: quit')
			elif Command == 'r':
				print(MDM.read())
			elif Command == 'a':
				print(MDM.add({input('Word: '): input('Reason: ')}))
			elif Command == 'rm':
				print(MDM.remove(input('Word: ')))
			elif Command == 's':
				print(MDM.show(input('Word: ')))
			elif Command == 'rs':
				print(MDM.reset())
			elif Command == 'q':
				break
			elif Command == 'Ac':
				while True:
					ACommand = input(':>>> ')
					if ACommand == 'h':
						print('a: Add, rm: remove, e: exist, c: changeUser, q: quit')
					elif ACommand == 'a':
						print(Account.add(input('UName: '), getpass('Passwd: '), input('DicName: ')))
					elif ACommand == 'rm':
						print(Account.remove(input('UName: '), getpass('Passwd: '), input('DicName: ')))
					elif ACommand == 'e':
						print(Account.exist(input('UName: ')))
					elif ACommand == 'c':
						MDM.AcData = {'User': input('UName: '), 'Passwd': getpass('Password: '), 'DicName': input('DictionaryName: ')}
					elif ACommand == 'q':
						break
		except KeyboardInterrupt:
			print('\ncommand: q')
		except EOFError:
			print('\ncommand: q')