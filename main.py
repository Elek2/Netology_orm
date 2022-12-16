import sqlalchemy
from sqlalchemy.orm import sessionmaker
from modules import create_tables
import modules as M
import json

DSN = 'postgresql://postgres:nicaragua21@localhost:5432/omr'
engine = sqlalchemy.create_engine(DSN)

with open("tests_data.json", "r") as read_file:
	data = json.load(read_file)

create_tables(engine)
pub_name = input('Введите название издателя: ')

with sessionmaker(bind=engine)() as session:
	for i in data:
		table_name = i['model'].capitalize()
		table_colums = i['fields']
		record = eval(f"M.{table_name}(**{table_colums})")
		session.add(record)
		session.commit()

	quer = session.query(M.Publisher.name, M.Shop.name, M.Sale.price, M.Sale.date_sale). \
		join(M.Book). \
		join(M.Stock). \
		join(M.Shop). \
		join(M.Sale). \
		filter(M.Publisher.name == f'{pub_name}').all()

	for sale in quer:
		print(*sale, sep=' | ')

