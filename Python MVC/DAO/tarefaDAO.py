import sqlite3 as sql

class TarefaDAO:
    def __init__(self):
        self.db = sql.connect("ToDoList.db")
        self.c = self.db.cursor ()
        
    def RetornarTarefas(self):
        return self.cursor.execute("SELECT * FROM Tarefas").fetchall()
    
    
    
    def Inserir(self, descricao, dataComeco, dataFinal, nivel):
    #     self.cursor.execut(f"""
    #         Insert INTO Tarefas ({descricaoCollum},{dataComecoCollum},{dataComeco},{dataFinalCollum}) 
    #         Values ('{descricao}','{dataComeco}', '{dataFinal}','{nivel}',0);                     
    # """)