import sqlalchemy
from sqlalchemy.orm import sessionmaker
from modules import create_tables
import modules as M

DSN = 'postgresql://postgres:nicaragua21@localhost:5432/omr'
engine = sqlalchemy.create_engine(DSN)


# create_tables(engine)
pub_name = input('Введите название издателя: ')

with sessionmaker(bind=engine)() as session:
	quer = session.query(M.Publisher.name, M.Shop.name, M.Sale.price, M.Sale.date_sale).\
		join(M.Book).\
		join(M.Stock).\
		join(M.Shop).\
		join(M.Sale).\
		filter(M.Publisher.name == f'{pub_name}').all()

	for sale in quer:
		print(*sale, sep=' | ')


# 	course1 = Course(name='Python')
# 	course2 = Course(name='Kotlin')
# 	course3 = Course(name='JavaScript')
# 	session.add_all([course1, course2, course3])
#
# 	hw1 = Homework(number=1, description='Первая ДЗ', course=course1)
# 	hw2 = Homework(number=2, description='Вторая ДЗ', course=course3)
# 	session.add_all([hw1, hw2])
#
# 	for i in session.query(Homework).all():
# 		print(i)
# 	session.commit()
