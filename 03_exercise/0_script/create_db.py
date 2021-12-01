import mysql.connector
from mysql.connector import errorcode
import os


def get_tables():
    t = {}
    t[
        "student"
    ] = """
        CREATE TABLE `student` (
          ID INT NOT NULL AUTO_INCREMENT,
          NAME CHAR(20),
          UNIVERSITY_ID CHAR(30),
          GROUP_ID INT,
          PRIMARY KEY (ID)
        );
        """

    t[
        "student_group"
    ] = """
        CREATE TABLE student_group (
          ID INT NOT NULL AUTO_INCREMENT,
          NAME CHAR(20),
          PRIMARY KEY (ID)
        );
        """

    t[
        "course"
    ] = """
        CREATE TABLE course (
          ID INT NOT NULL AUTO_INCREMENT,
          NAME CHAR(40),
          YEAR CHAR(4),
          PRIMARY KEY (ID)
        );
        """
    t[
        "attendence"
    ] = """
        CREATE TABLE attending_course (
          ID INT NOT NULL AUTO_INCREMENT,
          ENROL_DATE DATE,
          COURSE_ID INT,
          STUDENT_ID INT,
          GRADE FLOAT,
          PRIMARY KEY (ID)
        );
        """
    return t


def create_db(host, username, password, db_name):
    mydb = mysql.connector.connect(host=host, user=username, password=password)

    mycur = mydb.cursor()
    try:
        mycur.execute("CREATE DATABASE {0}".format(db_name))
    except mysql.connector.Error as err:
        print(err.errno)
        # https://dev.mysql.com/doc/mysql-errors/8.0/en/server-error-reference.html
        if err.errno != errorcode.ER_DB_CREATE_EXISTS:
            print("Failed creating database: {}".format(err))
            exit(1)
        else:
            print("Database {0} exists!".format(db_name))

    mycur.execute("USE {}".format(db_name))

    tables = get_tables()
    for table_name in tables:
        table_description = tables[table_name]
        try:
            print("Creating table {}: ".format(table_name))
            mycur.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")


if __name__ == "__main__":
    host = "localhost"
    username = "root"
    password = "nomoresecret"
    db_name = "university"
    create_db(host, username, password, db_name)
