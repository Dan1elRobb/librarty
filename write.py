from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Book, Publisher, Writer, Person
from random import randint
from datetime import date

publishers = [
    Publisher(p_name="Max"),
    Publisher(p_name="Seb"),
    Publisher(p_name="ChaNab"),
    Publisher(p_name='Black and White')
]

books = [
    Book(title="How to Train your dragon",
         isbn=(randint(999999999999,9999999999999)),
         num_pages=randint(200,1000),
         publication_date=date(1813, 2, 23),
         ),
    Book(title="AH flipping guide",
         isbn=(randint(999999999999, 9999999999999)),
         num_pages=randint(200, 1000),
         publication_date=date(2018, 5, 12),
         ),
    Book(title="Terrible coding",
         isbn=(randint(999999999999, 9999999999999)),
         num_pages=randint(200, 1000),
         publication_date=date(1987, 10, 10),
         )
]

authors = [
    Writer(w_name="Superman"),
    Writer(w_name="batman"),
    Writer(w_name="The flash"),
]

people = [
    Person(name="Sebastian Burbidge"),
    Person(name="Dave James"),
    Person(name="Stephen Spoerri"),
    Person(name="Ariella G"),
    Person(name="Merris Amos"),
    Person(name="Daniel Robb")
]

books[0].publisher = publishers[0]
books[1].publisher = publishers[1]
books[2].authors.append(authors[2])
books[2].authors.append(authors[3])
books[2].publisher = publishers[0]
books[3].authors.append(authors[3])
books[3].publisher = publishers[2]


books[3].borrowers.append(people[1])
books[3].borrowers.append(people[4])
books[0].borrowers.append(people[1])
books[2].borrowers.append(people[2])
books[2].borrowers.append(people[0])

engine = create_engine('sqlite:///library.sqlite', echo=True)

with Session(engine) as sess:
    sess.add_all(books)
    sess.commit()