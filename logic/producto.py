from dataBase.readDataBase import readDataBase

session = readDataBase()

print(session.execute("SELECT * FROM Productos").fetchall())