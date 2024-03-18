class Person:

    def __init__(self, full_name: str, date_of_birth: str, phone_number: str, city: str, country: str,
                 home_address: str):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def __str__(self, format: str = "default"):
        if format == "short":
            return f"{self.full_name} ({self.city}, {self.country})"
        elif format == "full":
            return f"""
            **ПІБ:** {self.full_name}
            **Дата народження:** {self.date_of_birth}
            **Телефон:** {self.phone_number}
            **Місто:** {self.city}
            **Країна:** {self.country}
            **Домашня адреса:** {self.home_address}
            """
        else:
            return f"{self.full_name} ({self.phone_number})"

    def __eq__(self, other):
        return self.full_name == other.full_name

    def change_phone_number(self, new_phone_number: str):
        self.phone_number = new_phone_number

    def move_to_new_address(self, new_city: str, new_country: str, new_home_address: str):
        self.city = new_city
        self.country = new_country
        self.home_address = new_home_address


person1 = Person(
    full_name="Іванов Іван Іванович",
    date_of_birth="1980-01-01",
    phone_number="+380991234567",
    city="Київ",
    country="Україна",
    home_address="вул. Шевченка, 1",
)

person2 = Person(
    full_name="Петрова Марія Іванівна",
    date_of_birth="1985-05-05",
    phone_number="+380978901234",
    city="Львів",
    country="Україна",
    home_address="вул. Франка, 10",
)

print(person1)
print(person2)

print(person1 == person2)
print(person1.full_name == person2.full_name)

print(person1.__str__("short"))
print(person2.__str__("full"))


# Завдання 2
class City:

    def __init__(self, name: str, region: str, country: str, population: int, postal_code: str, phone_code: str):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def __str__(self, format: str = "default"):

        if format == "short":
            return f"{self.name} ({self.country})"
        elif format == "full":
            return f"""
            **Місто:** {self.name}
            **Регіон:** {self.region}
            **Країна:** {self.country}
            **Населення:** {self.population}
            **Поштовий індекс:** {self.postal_code}
            **Телефонний код:** {self.phone_code}
            """
        else:
            return f"{self.name} ({self.population})"

    def __eq__(self, other):
        return self.name == other.name

    def change_population(self, new_population: int):
        self.population = new_population

    def update_postal_code(self, new_postal_code: str):
        self.postal_code = new_postal_code


city1 = City(
    name="Київ",
    region="Київська область",
    country="Україна",
    population=2962150,
    postal_code="01001",
    phone_code="044",
)

city2 = City(
    name="Львів",
    region="Львівська область",
    country="Україна",
    population=721541,
    postal_code="79000",
    phone_code="032",
)

print(city1)
print(city2)

print(city1 == city2)
print(city1.name == city2.name)

print(city1.__str__("short"))
print(city2.__str__("full"))
# Завдання 3
from typing import List


class Country:

    def __init__(self, name: str, continent: str, population: int, phone_code: str, capital: str, cities: List[str]):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def __str__(self, format: str = "default"):

        if format == "short":
            return f"{self.name} ({self.continent})"
        elif format == "full":
            return f"""
            **Країна:** {self.name}
            **Континент:** {self.continent}
            **Населення:** {self.population}
            **Телефонний код:** {self.phone_code}
            **Столиця:** {self.capital}
            **Міста:** {", ".join(self.cities)}
            """
        else:
            return f"{self.name} ({self.population})"

    def __eq__(self, other):
        return self.name == other.name

    def add_city(self, new_city: str):
        self.cities.append(new_city)

    def change_capital(self, new_capital: str):
        self.capital = new_capital


country1 = Country(
    name="Україна",
    continent="Європа",
    population=44134693,
    phone_code="+380",
    capital="Київ",
    cities=["Львів", "Одеса", "Дніпро"],
)

country2 = Country(
    name="Польща",
    continent="Європа",
    population=38008111,
    phone_code="+48",
    capital="Варшава",
    cities=["Краків", "Вроцлав", "Гданськ"],
)

print(country1)
print(country2)

print(country1 == country2)
print(country1.name == country2.name)

print(country1.__str__("short"))
print(country2.__str__("full"))


# Завдання 4
class Watch:

    def __init__(self, model: str, manufacturer: str, year: int, price: float, type: str):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.type = type

    def __str__(self):
        return f"""
        **Модель:** {self.model}
        **Виробник:** {self.manufacturer}
        **Рік випуску:** {self.year}
        **Ціна:** {self.price} грн.
        **Тип:** {self.type}
        """

    def __eq__(self, other):
        return self.model == other.model

    def change_price(self, new_price: float):
        self.price = new_price


watch1 = Watch(
    model="Casio G-Shock GA-2100",
    manufacturer="Casio",
    year=2021,
    price=4000,
    type="наручний",
)

watch2 = Watch(
    model="Orient Bambino FAC0000EW",
    manufacturer="Orient",
    year=2020,
    price=6500,
    type="наручний",
)

print(watch1)
print(watch2)

print(watch1 == watch2)
print(watch1.model == watch2.model)

watch1.change_price(3500)
print(watch1.price)


# Завдання 5
class Website:

    def __init__(self, name: str, url: str, description: str):
        self.name = name
        self.url = url
        self.description = description

    def __str__(self):
        return f"""
        **Назва:** {self.name}
        **URL:** {self.url}
        **Опис:** {self.description}
        """

    def __eq__(self, other):
        return self.name == other.name

    def open_website(self):
        import webbrowser

        webbrowser.open(self.url)


website1 = Website(
    name="Google",
    url="https://www.google.com/",
    description="Пошукова система",
)

website2 = Website(
    name="YouTube",
    url="https://www.youtube.com/",
    description="Відеохостинг",
)

print(website1)
print(website2)

print(website1 == website2)
print(website1.name == website2.name)

website1.open_website()
website2.open_website()
