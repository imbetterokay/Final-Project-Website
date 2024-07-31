import sqlite3
import hashlib

conn = sqlite3.connect('userdata.db')
cur = conn.cursor()

# Execute an SQL command to create a table named 'userdata' if it does not already exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata (
        Id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

# Define username and password pairs, and hash the passwords using SHA-256
username1, password1 = "mrpot", hashlib.sha256("toptop".encode()).hexdigest()
username2, password2 = "mrpot2", hashlib.sha256("cece".encode()).hexdigest()
username3, password3 = "mrpot3", hashlib.sha256("aye".encode()).hexdigest()
username4, password4 = "mrpot4", hashlib.sha256("glow".encode()).hexdigest()
username5, password5 = "mrpot5", hashlib.sha256("beat".encode()).hexdigest()

# Insert the username and hashed password pairs into the 'userdata' table
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username5, password5))

conn.commit()
