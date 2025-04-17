import string

import psycopg2
import random

conn = psycopg2.connect(database = "postgres",
                        user = "postgres",
                        host= 'localhost',
                        password = "Str0ngP@ssword",
                        port = 5432)

cursor = conn.cursor()

for i in range(1001, 10000):
    s = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    cursor.execute(f"INSERT INTO test1 (a, b) VALUES ({i}, 'Course {i}')")

conn.commit()