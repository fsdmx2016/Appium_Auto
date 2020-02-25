#coding=utf-8
from configparser import ConfigParser


class ReadIni:
	def __init__(self,file_path=None):
		if file_path == None:
			self.file_path = '..\config\LocalElement.ini'
		else:
			self.file_path = file_path
		self.data = self.read_ini()
	def read_ini(self):
		read_ini = ConfigParser()
		read_ini.read(self.file_path)
		return read_ini

	#通过key获取对应的value
	def get_value(self,key,section=None):
		if section == None:
			section = 'login_element'
		try:
			value = self.data.get(section,key)		
		except:
			value = None
		return value


if __name__ == '__main__':
    run = ReadIni()
    print(run.read_ini())
