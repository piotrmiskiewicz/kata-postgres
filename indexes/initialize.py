import string

import psycopg2
import random
import json

conn = psycopg2.connect(database = "postgres",
                        user = "postgres",
                        host= 'localhost',
                        password = "Str0ngP@ssword",
                        port = 5432)




names = ["Amelia", "Olivia", "Peter", "John", "William", "James", "Lily"]
cities = [
    ("Gliwice", 44, 100),
    ("Bielsko biała", 43, 300),
    ("Zywiec", 34, 300),
    ("Rybnik", 44, 200),
    ("Sosnowiec", 41, 200),
    ("Pszczyna", 43, 200),
    ("Opole", 21, 200),
    ("Kielce", 25, 0),
    ("Tczew", 83, 100),
    ("Szczecin", 70, 0),
    ("Cieszyn", 43, 400),
    ("Lublin", 20, 0),
    ("Katowice", 40, 0),
    ("Bytom", 41, 900),
    ("Milówka", 34, 360),
    ("Tychy", 43, 100),
    ("Rzeszów", 35, 0),
    ("Brzesko", 32, 800),
    ("Nowy Targ", 34, 400)
]
rareCities = [
    ("Toszek", 44, 180),
    ("Kietrz", 48, 130),
    ("Zabrze", 41, 800)
]


for j in range (0, 5000):
    cursor = conn.cursor()
    for i in range(0, 100):
        if random.randint(1, 400) == 5:
            city = random.choice(rareCities)
            print("RARE")
        else:
            city = random.choice(cities)
        cityName = city[0]
        zipSuffix = random.randint(0, 19)
        b = city[2] + zipSuffix
        zipCode = f"{city[1]}-{b:03}"
        firstName = random.choice(names)
        age = random.randint(30, 70)

        obj = {"x":{"y":random.randint(1, 10), "city":cityName}}
        js = json.dumps(obj)

        print(firstName, age, zipCode, cityName, js)

        cursor.execute(f"INSERT INTO person (first_name, age, zip, city, data_s, data_b) VALUES ('{firstName}', {age},"
                       f"'{zipCode}', '{cityName}', '{js}', '{js}')")

    conn.commit()