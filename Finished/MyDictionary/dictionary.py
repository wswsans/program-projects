import os
class dictionary:
	def __init__(self, name):
		print("辞書を作成しました。")
		self.dic_name = name
		self.make_list = {"作成日": "このスプリクトを作成したのは2018年4月8日です。"}

	def make(self, name, desc):
		self.make_list[name] = desc
		print(name, "を作成しました")
		return "make"+name

	def delete(self, name):
		try:
			self.make_list[name]
		except Exception:
			print("そもそも辞書にありません")
			return "Not Found"+name
		else:
			del self.make_list[name]
			print("削除しました")
			return "delete"+name

	def puts(self, name):
		try:
			self.make_list[name]
		except Exception:
			print("辞書にありませんでした。")
		else:
			print(self.make_list[name])

	def download(self):
		key = list(self.make_list.keys())
		value = list(self.make_list.values())
		with open(os.path.dirname(os.path.abspath(__file__))+"/make_list.txt", "w") as f:
			f.write(self.dic_name + "の辞書")
			for i in range(len(self.make_list)):
				f.write("{0}: {1}".format(key[i], value[i]))
		print("書き込みが終わりました。")
		return "Downloaded"


