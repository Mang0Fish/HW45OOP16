from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///example.db", echo=True)
Base = declarative_base()

class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_book1 = Books(title="Harry Potter and the Sorcerer's Stone", price=89.90)
new_book2 = Books(title="The Little Prince", price=45.50)
new_book3 = Books(title="1984", price=79.90)
new_book4 = Books(title="Les Misérables", price=99.00)
new_book5 = Books(title="Crime and Punishment", price=69.90)

new_books = [new_book1, new_book2, new_book3, new_book4, new_book5]

# session.add_all(new_books)
# session.commit()

books = session.query(Books).all()
for b in books:
    print(b.id, b.title, b.price)

big_books = session.query(Books).filter(Books.price > 70).all()
for b in big_books:
    print(b.id, b.title, b.price)

session.query(Books).filter(Books.title == "1984").update({"price":89.5})
session.commit()

session.query(Books).filter(Books.price == 99).delete()
session.commit()

books = session.query(Books).all()
for b in books:
    print(b.id, b.title, b.price)

#2
import threading
def print_1_100():
    for i in range(1,101):
        print(i)

def print_100_1():
    for i in range(100, 0, -1):
        print(i)


thread1 = threading.Thread(target=print_1_100())
thread2 = threading.Thread(target=print_100_1())

thread1.start()
thread2.start()
print("---------------------------------")

#3
import multiprocessing

process1 = multiprocessing.Process(target=print_1_100())
process2 = multiprocessing.Process(target=print_100_1())


if __name__ == "__main__":
    process1.start()
    process2.start()


#4

lock = threading.Lock()
capitals = [
        "Tokyo, Japan", "New Delhi, India", "Beijing, China",
        "Washington D.C., USA", "Brasília, Brazil", "Moscow, Russia",
        "London, UK", "Paris, France", "Berlin, Germany", "Rome, Italy"
    ]
with lock:
    for city in capitals[:5]:
            print(f"- {city}")
        

# I haven't copied everything so it won't be messy and cramped



