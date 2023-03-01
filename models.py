from sqlalchemy import Column, Integer, String, Date, Boolean, Table, UniqueConstraint, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

book_writer = Table("book_writer",
                    Base.metadata,
                    Column('book_id', ForeignKey('book.book_id')),
                    Column('writer_id', ForeignKey("writer.writer_id")),
                    UniqueConstraint('book_id', 'writer_id')
                    )

book_loan = Table("book_loan",
                  Base.metadata,
                  Column('book_id', ForeignKey('book.book_id')),
                  Column('person_id', ForeignKey("person.person_id")),
                  UniqueConstraint('book_id', 'person_id')
                  )


class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    isbn = Column(String, unique=True)
    num_pages = Column(Integer)
    publication_date = Column(Date)
    publisher_id = Column(Integer, ForeignKey("publisher.publisher_id"))

    writers = relationship("Writer",
                           secondary=book_writer,
                           order_by='(Writer.writer_name)')

    borrowers = relationship("Person",
                             secondary=book_loan,
                             order_by='(Person.name)')

    publisher = relationship("Publisher")


class Publisher(Base):
    __tablename__ = "publisher"
    publisher_id = Column(Integer, primary_key=True, autoincrement=True)
    publisher_name = Column(String)
    books = relationship("Book")




class Writer(Base):
    __tablename__ = "writer"
    writer_id = Column(Integer, primary_key=True, autoincrement=True)
    writer_name = Column(String)

    works = relationship("Book",
                         secondary=book_writer)



class Person(Base):
    __tablename__ = "person"
    person_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    membership_expiry = Column(Boolean)

    on_loan = relationship("Book",
                           secondary=book_loan,
                           order_by='(Book.title)')