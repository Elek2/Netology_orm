import sqlalchemy
from sqlalchemy.orm import sessionmaker
from modules import create_tables
import modules as mls
import json

DSN = 'postgresql://postgres:nicaragua21@localhost:5432/omr'
engine = sqlalchemy.create_engine(DSN)

with open("tests_data.json", "r") as read_file:
	data = json.load(read_file)

create_tables(engine)
pub_name = input('Введите название издателя: ')

with sessionmaker(bind=engine)() as session:
	for rec in data:
		t_name = rec['model'].capitalize()
		t_id = rec['pk']
		t_colums = rec['fields']
		session.add(eval(f"M.{t_name}(id = {t_id}, **{t_colums})"))
		session.commit()

	quer = session.query(mls.Publisher.name, mls.Shop.name, mls.Sale.price, mls.Sale.date_sale). \
		join(mls.Book). \
		join(mls.Stock). \
		join(mls.Shop). \
		join(mls.Sale). \
		filter(mls.Publisher.name == f'{pub_name}').all()

	for sale in quer:
		print(*sale, sep=' | ')
