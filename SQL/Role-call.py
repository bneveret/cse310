import sqlite3
from sqlite3 import Error

#creates a connection to the database
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

#creates a table if it doesn't already exist
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# keeps track of the next id for the table
def get_next_id(conn):
    studentList = []
    cursor = conn.execute("SELECT name from STUDENTS;")
    for student in cursor:
        studentList.append(student[0])
    if studentList == []:
        return 1
    else:
        return len(studentList) + 1

#ensures a correct input for attendance
def presence_input(name):
    presence = input(f'{name}\n1. Present\n2. Absent\n')
    if presence == '1':
        presence = 'Present'
    elif presence == '2':
        presence = 'Absent'
    else:
        print('please enter 1 or 2')
        presence = presence_input(name)
    return presence

# loops through a student list and applies their attendance record to the database
def takerole(conn):
    studentList = []
    cursor = conn.execute("SELECT name from STUDENTS;")
    for student in cursor:
        studentList.append(student[0])
    for n in range(1,len(studentList)+1):
        presence = presence_input(studentList[n-1])
        conn.execute(f"UPDATE STUDENTS set ATTENDANCE = '{presence}' where ID ={n};")
    print('Attendance complete')

# alphebetizes the list of students
def reorder(conn):
    studentList = []
    cursor = conn.execute("SELECT name from STUDENTS;")
    for student in cursor:
        studentList.append(student[0])
    studentList.sort()
    for n in range(1,len(studentList)+1):
        conn.execute(f"UPDATE STUDENTS set NAME = '{studentList[n-1]}' where ID ={n};")

# displays the list of students
def list_students(conn):
    count = 1
    cursor = conn.execute("SELECT name from STUDENTS;")
    print('\n')
    for student in cursor:
        print(f'{count}. {student[0]}')
        count +=1
    print('\n')

# adds a new student to the database
def insert_student(conn, id):
    name = input('Enter students name: ').title()
    conn.execute(f"INSERT INTO STUDENTS (ID, NAME, ATTENDANCE) \
        VALUES ({id}, '{name}', 'Present');")
    reorder(conn)
    conn.commit()

# removes a student from the database
def delete_student(conn):
    name = input('Enter students name: ').title()
    studentList = []
    cursor = conn.execute("SELECT name from STUDENTS;")
    for student in cursor:
        studentList.append(student[0])
    mark = len(studentList)
    studentList.remove(name)
    studentList.sort()
    for n in range(1,len(studentList)+1):
        conn.execute(f"UPDATE STUDENTS set NAME = '{studentList[n-1]}' where ID ={n};")
    conn.execute(f"Delete from STUDENTS where ID = {mark};")
    conn.commit()

def main():

    database = r"students.db"

    sql_create_students_table = """ CREATE TABLE IF NOT EXISTS STUDENTS (
                                        ID INT PRIMARY KEY,
                                        NAME TEXT NOT NULL,
                                        ATTENDANCE TEXT
                                    ); """


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_students_table)

    else:
        print("Error! cannot create the database connection.")

    stop = 'nope'
    next_id = get_next_id(conn)

    print('Welcome to rolecall!\n')
    while stop == 'nope':
        user_selection = input('1. Add Student\n2. Remove Student\n3. Take Attendance\n4. List Students\n5. Quit\n')
        if user_selection == '1':
            insert_student(conn, next_id)
            next_id += 1
        elif user_selection == '2':
            delete_student(conn)
            next_id -= 1
        elif user_selection == '3':
            takerole(conn)
        elif user_selection == '4':
            list_students(conn)
        elif user_selection == '5':
            conn.close()
            stop = 'yep'
        else:
            print('Please select a number between 1 and 5')

if __name__ == '__main__':
    main()