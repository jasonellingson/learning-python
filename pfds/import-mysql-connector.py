import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='gat7sby!',
                                    host='127.0.0.1',
                                    database='sampledb')
    cursor = cnx.cursor()
    # definining employee rows
    emps = [
        (9001, "Jeff Russell", "sales"),
        (9002, "Jane Boorman", "sales"),
        (9003, "Tom Heints", "sales")
    ]
    # defining the query
    query_add_emp = ("""INSERT INTO emps (empno, empname, job)
                        VALUES (%s, %s, %s)""")
    # inserting the employee rows
    for emp in emps:
        cursor.execute(query_add_emp, emp)
    # defining and inserting salaries
    salary = [
        (9001, 3000),
        (9002, 2800),
        (9003, 2500)
    ]
    query_add_salary = ("""INSERT INTO salary (empno, salary)
                            VALUES (%s, %s)""")
    for sal in salary:
        cursor.execute(query_add_salary, sal)
    # definiing and inserting orders
    orders = [
        (2608, 9001, 35),
        (2617, 9001, 35),
        (2620, 9001, 139),
        (2621, 9002, 95),
        (2626, 9002, 218)
    ]
    query_add_order = ("""INSERT INTO orders(pono, empno, total)
                            VALUES(%s, %s, %s)""")
    for order in orders:
        cursor.execute(query_add_order, order)
    # making the insertions permanent in the database
    cnx.commit()
except mysql.connector.Error as err:
    print("Error-Code:", err.errno)
    print("Error-Message: {}".format(err.msg))
finally:
    cursor.close()
    cnx.close()