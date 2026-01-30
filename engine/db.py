import sqlite3

conn = sqlite3.connect('sophia.db')   

cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id INTEGER PRIMARY KEY, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'MySQL Workbench','C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe')"
#cursor.execute(query)
#conn.commit()
#conn.close()

query = "CREATE TABLE IF NOT EXISTS web_command(id INTEGER PRIMARY KEY, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'ChatGPT','https://chatgpt.com')"
cursor.execute(query)
conn.commit()
conn.close()