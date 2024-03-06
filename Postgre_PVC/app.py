import psycopg2

def create_conn():
    print("here")

    conn = psycopg2.connect(
        host='127.0.0.1',
        port='50476',
        database='testdb',
        user='admin',
        password='adminpwd'
    )

    return conn

conn = create_conn()

with conn.cursor() as cursor:
    cursor.execute('''select version()''')
    print("connected")