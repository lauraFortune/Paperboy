import sqlite3

def connect(): 
    cnx = sqlite3.connect("mynews.db")
    cur = cnx.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY, categoryName TEXT, image TEXT, url TEXT, publish_date TEXT, title TEXT, description TEXT)") # will only create table if does not already exist
    cnx.commit()
    cnx.close()

def save(categoryName, image, url, publish_date, title, description):
    cnx = sqlite3.connect("mynews.db")
    cur = cnx.cursor()
    cur.execute("INSERT INTO articles VALUES(NULL, ?, ?, ?, ?, ?, ?)", (categoryName, image, url, publish_date, title, description)) # NULL WILL CREATE ID AUTOMATICALLY - ? entered values not yet known
    cnx.commit()
    cnx.close

def show():
    cnx = sqlite3.connect("mynews.db")
    cur = cnx.cursor()
    cur.execute("SELECT * FROM articles")
    rows=cur.fetchall() #data is stored in rows variable
    cnx.close
    return rows

def delete(id):
    cnx=sqlite3.connect("mynews.db") 
    cur=cnx.cursor()
    cur.execute("DELETE FROM articles WHERE id=?", (id,))
    cnx.commit() # commit the changes
    cnx.close # close

connect() #connect function will run as soon as front end runs as backend is imported to frontend
