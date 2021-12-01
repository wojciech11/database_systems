import mysql.connector
from mysql.connector import errorcode


def insert_student_groups(cur):
    groups = [
        'INSERT INTO student_group (NAME) VALUES ("Group A")',
        'INSERT INTO student_group (NAME) VALUES ("Group B")',
        'INSERT INTO student_group (NAME) VALUES ("Group C")',
    ]

    for g in groups:
        cur.execute(g)


def insert_students(cur):
    # add students
    # please do not assume the groups IDs
    # but query for them
    pass


# notice: we miss error handling
def insert_data(host, username, password, db_name):
    mydb = mysql.connector.connect(host=host, user=username, password=password)
    with mydb.cursor() as mycur:
        mycur.execute("USE {0}".format(db_name))
        mycur = mydb.cursor()
        insert_student_groups(mycur)

    with mydb.cursor() as mycur:
        mycur.execute("USE {0}".format(db_name))
        mycur.execute("select * from student_group")
        for sg_id, sg_name in mycur:
            print(sg_id, sg_name)

    with mydb.cursor() as mycur:
        mycur.execute("USE {0}".format(db_name))
        insert_students(mycur)

    # add code to print out all students


if __name__ == "__main__":
    host = "localhost"
    username = "root"
    password = "nomoresecret"
    db_name = "university"
    insert_data(host, username, password, db_name)
