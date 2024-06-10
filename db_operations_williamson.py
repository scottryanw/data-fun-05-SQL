import sqlite3
import pandas as pd
import pathlib
import pyarrow
import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started")

db_file = pathlib.Path("project.db")

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting CSV data:", e)
        
def insert_records():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path('sql', 'insert_records.sql')
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e)

def update_records():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path('sql', 'update_records.sql')
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records updated successfully.")
    except sqlite3.Error as e:
        print("Error updating records:", e)

def delete_records():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path('sql', 'delete_records.sql')
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting records:", e)

def query_aggregation():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path('sql', 'query_aggregation.sql')
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Query Aggregation executed successfully.")
    except sqlite3.Error as e:
        print("Error querying aggregation for books:", e)

def query_filter():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path('sql', 'query_filter.sql')
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Query Filter executed successfully.")
    except sqlite3.Error as e:
        print("Error filtering book data:", e)

def query_sorting():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path('sql', 'query_aggregation.sql')
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Query Sorting executed successfully.")
    except sqlite3.Error as e:
        print("Error sorting book data:", e)

def query_group_by():
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path('sql', 'query_group_by.sql')
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Query Group By executed successfully.")
    except sqlite3.Error as e:
        print("Error executing query:", e)

def query_join():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path('sql', 'query_join.sql')
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Query Join executed successfully.")
    except sqlite3.Error as e:
        print("Error executing query:", e)


def main():
    insert_data_from_csv()
    create_tables()
    insert_records() 
    delete_records()
    query_aggregation()
    query_filter()
    query_sorting()
    query_group_by()
    query_join()    

    logging.info("All SQL operations completed successfully")

if __name__ == "__main__":
    main()

logging.info("Program ended")