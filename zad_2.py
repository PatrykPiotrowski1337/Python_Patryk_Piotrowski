from zad_1 import Student


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self):
        return f""" Biblioteka znajduje się w miasto {self._city},
        na ulicy {self._street},
        kod pocztowy to: {self._zip_code},
        godziny otwarcia: {self._zip_code},
        Kontakt:{self._phone}"""

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city) -> None:
        self.city = city

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, street):
        self._street = street

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        self._zip_code = zip_code

    @property
    def open_hours(self):
        return self.open_hours

    @open_hours.setter
    def open_hours(self, open_hours):
        self._open_hours = open_hours

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self._first_name = first_name
        self._last_Name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self):
        return f""" Imie {self._first_name} Nazwisko{self._last_Name},
             urodzony{self._birth_date}, zatrudniony{self._hire_date},
             zamieszkaly {self._city} na ulicy {self._street}kod pocztowy{self._zip_code},
             numer kontaktowy {self._phone}"""

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_Name

    @last_name.setter
    def last_name(self, last_name):
        self._last_Name = last_name

    @property
    def hire_date(self):
        return self._hire_date

    @hire_date.setter
    def hire_date(self, hire_date):
        self._hire_date = hire_date

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def zip_code(self):
        return self.zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        self._zip_code = zip_code

    @property
    def phone(self):
        return self.phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone


class Book:
    def __init__(self, library: Library, publication_date, author_name, author_surname, number_of_pages):
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self):
        return f"""{self._library},
            data publikacji {self._publication_date}
            autor:{self._author_name} {self._author_surname}
            ilość stron {self._number_of_pages}"""

    @property
    def library(self):
        return self._library

    @library.setter
    def library(self, library: Library):
        self._library = library

    @property
    def publication_date(self):
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        self._publication_date = publication_date

    @property
    def author_name(self):
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        self._author_name = author_name

    @property
    def author_surname(self):
        return self._author_surname

    @author_surname.setter
    def author_surname(self, author_surname):
        self._author_surname = author_surname

    @property
    def number_of_pages(self):
        return self.number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages):
        self._number_of_pages = number_of_pages


class Order:
    def __init__(self, employee: Employee, student: Student, books: Book, order_date):
        self._employee = employee
        self._student = student
        self._books = books
        self._order_date = order_date

    def __str__(self):
        return f""" pracownik{self._employee},
        student{self._student},
        ksiazki{self._books},
        data zamowienia{self._order_date}"""

    @property
    def employee(self):
        return self._employee

    @employee.setter
    def employee(self, employee: Employee):
        self._employee = employee

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, student: Student):
        self._student = student

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, books):
        self._books = books

    @property
    def order_date(self):
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        self._order_date = order_date


Biblioteka1 = Library("będzin", "mała", "1111", "12-13", "473-512-412")
Biblioteka2 = Library("będzin2", "m2ała", "12111", "22-13", "2473-512-412")

ksiazka1 = Book(Biblioteka1, "11.11.1111", "Tadeusz", "Wąsik", "12")
ksiazka2 = Book(Biblioteka2, "11.12.1111", "marian", "Wtsk", "17")
ksiazka3 = Book(Biblioteka2, "11.13.1111", "Patryk", "Kuba", "22")
ksiazka4 = Book(Biblioteka1, "11.14.1111", "Marian", "Artur", "41")
ksiazka5 = Book(Biblioteka2, "11.15.1111", "Anita", "Bomba", "51")

Pracownik1 = Employee("Kuba", "Patryk", "11.11.2021", "01,11,2001", "Kato", "kato", "123", "1234")
Pracownik2 = Employee("Andrzej", "Tomek", "11.11.2021", "01,11,1981", "Kato", "Stara", "123", "1234")
Pracownik3 = Employee("Kuba", "Patryk", "11.11.2021", "01,11,1955", "Kato", "Nowa", "123", "1234")

uczen1 = Student("kuba", "90")
uczen2 = Student("Patryk", "91")
uczen3 = Student("tomek", "51")

zamowienie1 = Order(Pracownik2, uczen1, ksiazka2, "11.12.2021")
zamowienie2 = Order(Pracownik1, uczen3, ksiazka5, "11.21.2021")

print(zamowienie1)
print(zamowienie2)
