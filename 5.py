class Printed(object):
	def __init__(self, name='TEST'):
		self.name = name

	def __str__(self):
		return self.name

class Magazine(Printed):
	def __init__(self, name='TEST', company='TEST_COMPANY'):
		super().__init__(name)
		self.company = company
	
class Book(Printed):
	def __init__(self, name='TEST', year=101, author='TEST_AUTHOR'):
		super().__init__(name)
		self.year = year
		self.author = author
	def __str__(self):
		return '{0} written by {1} in {2}'.format(self.name, self.author, self.year)
class Textbook(Book):
	def __init__(self, name='TEST', year=101, author='TEST_AUTHOR', clas=7):
		super().__init__(name, year, author)
		self.clas = clas
	def __str__(self):
		return super().__str__() + ' for {} class'.format(self.clas)

a = Textbook('Физика', 2018, 'Александр Пёрышкин',7)
b = Book('Атлант расправил плечи', 1957, 'Айн Рэнд')
c = Magazine('Квант', 'Наука')
d = Printed('Проба пера')
print(a,b,c,d, sep = '\n')
