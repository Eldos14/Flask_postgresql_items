import psycopg2

def get_items():
    conn = psycopg2.connect(
        dbname="items",
        user="postgres",
        password="Eldos2001",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def get_buys():
    conn = psycopg2.connect(
        dbname="items",
        user="postgres",
        password="Eldos2001",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM buys")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
def add_buy(user_name, item_name, price):
    import datetime
    conn = psycopg2.connect(
        dbname="items",
        user="postgres",
        password="Eldos2001",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO buys (user_name, item_name, price, date) VALUES (%s, %s, %s, %s)",
        (user_name, item_name, price, datetime.date.today())
    )
    conn.commit()
    cursor.close()
    conn.close()
