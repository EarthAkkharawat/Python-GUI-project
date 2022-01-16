import sqlite3

conn = sqlite3.connect('allexpense.db')
c = conn.cursor()

#Build table
c.execute("""CREATE TABLE IF NOT EXISTS expense (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
        dt text,
		eplist text,
		price real)""")


def insert_expense(dt,eplist,price):
    ID = None
    with conn:
        c.execute("""INSERT INTO expense VALUES (?,?,?,?)""",
                  (ID,dt,eplist,price))
    conn.commit()
    print('Data was inserted')

def view_expense():
    with conn:
        c.execute("SELECT * FROM expense")
        expense = c.fetchall()
        print(expense)

    return expense


insert_expense('2020-06-28','rice',10000)
insert_expense('2020-06-28','water',30000)

allexpense = view_expense()
#print("First expense eplist: ",allexpense[0][1])

# delete function

def del_expense(ID):
    with conn:
        c.execute("DELETE FROM expense WHERE ID=(?)",[(ID)])
    conn.commit()
    print('Data was delete')


def update_expense(ID,price_change):
    with conn:
        c.execute("UPDATE expense SET price = (?) WHERE ID=(?)",([price_change,ID]))
    conn.commit()
    print('Data was updated')
    #view_expense()