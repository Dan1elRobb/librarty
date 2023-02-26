from sqlalchemy import Column, Integer, String, Date, Boolean, Table, UniqueConstraint, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

writer = Table("writer",
               Base.metadata,
               Column('book_id', ForeignKey('book.book_id')),
               Column('writerid', ForeignKey("writer.writerid")),
               UniqueConstraint('book_id', 'writerid')
               )

loan = Table("loan",
             Base.metadata,
             Column('book_id', ForeignKey('book.book_id')),
             Column('person_id', ForeignKey("person.person_id")),
             UniqueConstraint('book_id', 'person_id')
             )


class Book(Base):
    __tablename__ = "book"
    book = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    publisher_id = Column(Integer, ForeignKey("publisher.publisher_id"))
    publication_date = Column(Date)
    isbn = Column(String)
    writers = relationship("Writer",
                           secondary=writer)

    borrowers = relationship("Person",
                             secondary=loan)


class Publisher(Base):
    __tablename__ = "publisher"
    publisher = Column(Integer, primary_key=True, autoincrement=True)
    p_name = Column(String)


class Writer(Base):
    __tablename__ = "writer"
    Writer = Column(Integer, primary_key=True, autoincrement=True)
    w_name = Column(String)


class Person(Base):
    __tablename__ = "person"
    person = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
