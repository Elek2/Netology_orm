import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Table = declarative_base()


class Publisher(Table):
	__tablename__ = 'publisher'

	id = sq.Column(sq.Integer, primary_key=True)
	name = sq.Column(sq.String, unique=True)


class Book(Table):
	__tablename__ = 'book'

	id = sq.Column(sq.Integer, primary_key=True)
	title = sq.Column(sq.String, nullable=False)
	id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"))
	publisher = relationship(Publisher, backref="hz")


class Shop(Table):
	__tablename__ = 'shop'

	id = sq.Column(sq.Integer, primary_key=True)
	name = sq.Column(sq.String, unique=True)


class Stock(Table):
	__tablename__ = 'stock'

	id = sq.Column(sq.Integer, primary_key=True)
	id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
	id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
	count = sq.Column(sq.Integer, nullable=False)
	book = relationship(Book)
	shop = relationship(Shop)


class Sale(Table):
	__tablename__ = 'sale'

	id = sq.Column(sq.Integer, primary_key=True)
	price = sq.Column(sq.Float, sq.CheckConstraint("price>0"))
	date_sale = sq.Column(sq.DATE, nullable=False)
	id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
	count = sq.Column(sq.Integer, nullable=False)
	stock = relationship(Stock)


def create_tables(engine):
	Table.metadata.drop_all(engine)
	Table.metadata.create_all(engine)
