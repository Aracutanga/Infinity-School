#Model (modelo):
# Representa a lógica de negócios e os dado da aplicação
#Pode incluir class  objetos qe representam entidades do domínio, como uuários, produtos, etc
#Não deve conter lógica de apresntação ou acesso a dados direto.

class TarefaModel:
    def __init__(self,dao):
        self.dao = dao
        self.nomeTabela = "Tarefa" 
        self.descricao = "Descricao"
        self.dataComeco = "DataComeco"
        self.dataTermino = "DataTermino"
        self.status = "Status"
        self.nivel = "Nivel"
        self.dao.cursor.execute(f""""
            CREATE TABLE IF {self.nomeTabela} NOT EXISTS(                
                {self.descricao} TEXT,
                {self.dataComeco} VARCHAR(20),
                {self.dataTermino} VARCHAR(20),
                {self.status} INTEGER,
                {self.nivel} INTEGER.    
            );                           
        """)
                           
        