
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Book, Publisher, Writer, Person
from random import randint
from datetime import date

publishers = [
    Publisher(publisher_name="Macmillan"),
    Publisher(publisher_name="Simon & Schuster"),
    Publisher(publisher_name="Penguin"),
    Publisher(publisher_name="Harper Collins")
]

books = [
    Book(title="Pride and Prejudice",
         isbn="".join([str(randint(0, 9)) for _ in range(13)]),
         num_pages=279,
         publication_date=date(1813, 2, 23),
         ),
    Book(title="Normal People",
         isbn="".join([str(randint(0, 9)) for _ in range(13)]),
         num_pages=266,
         publication_date=date(2018, 5, 12),
         ),
    Book(title="How to Train your dragon",
         isbn=(randint(999999999999, 9999999999999)),
         num_pages=randint(200, 1000),
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


writers = [
    Writer(writer_name="Jane Eyre"),
    Writer(w_name="Superman"),
    Writer(w_name="batman"),
    Writer(w_name="The flash"),
]

people = [
    Person(name="Sebastian Burbidge", membership_expiry=False),
    Person(name="Jon Rahm", membership_expiry=False),
    Person(name="Oli Zeidler", membership_expiry=False),
    Person(name="Arthur Delport", membership_expiry=False),
    Person(name="Catherine Johnson", membership_expiry=False),
    Person(name="Clive Newsend", membership_expiry=False)
]

books[randint(1,4)].writers.append(writers[0])
books[randint(1,4)].publisher = publishers[0]
books[randint(1,4)].writers.append(writers[1])
books[randint(1,4)].publisher = publishers[1]
books[randint(1,4)].writers.append(writers[2])
books[randint(1,4)].writers.append(writers[3])
books[randint(1,4)].publisher = publishers[0]
books[randint(1,4)].writers.append(writers[3])
books[randint(1,4)].publisher = publishers[2]
books[randint(1,4)].writers.append(writers[3])
books[randint(1,4)].publisher = publishers[3]

books[randint(1,4)].borrowers.append(people[5])
books[randint(1,4)].borrowers.append(people[1])
books[randint(1,4)].borrowers.append(people[4])
books[randint(1,4)].borrowers.append(people[1])
books[randint(1,4)].borrowers.append(people[2])
books[randint(1,4)].borrowers.append(people[0])

engine = create_engine('sqlite:///library.sqlite', echo=True)

with Session(engine) as sess:
    sess.add_all(books)
    sess.commit()
