import sqlite3

my_db = sqlite3.connect("my_database.db")

my_cursor = my_db.cursor()

# my_statement = '''
#                 create table my_table(
#                     title text,
#                     author text,
#                     tag text
#                 )
#                  '''

# my_cursor.execute(my_statement)

my_data = """
            insert into my_table values (
                'scraping' ,
                'bibek',
                'python')
            """

my_cursor.execute(my_data)

my_db.commit()

my_db.close()