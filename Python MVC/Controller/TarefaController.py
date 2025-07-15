




import DAO.tarefaDAO as TDAO
import Model.tarefaModel as TModel

class TarefaControler:
    def __init__(self):
        self.dao = TDAO.TarefaDAO()
        self.model = TModel.TarefaModel(self.dao)
        
    def InserirTarefa(self, descricao, dataComeco, dataFinal, nivel):
        self.dao.Inserir(self.model.descricao, descricao, self.model.dataComeco, dataComeco, self.model.dataTermino, dataFinal, self.model.nivel, nivel, self.model.status)
        pass
    
    def AtualizarTarefa(self):
        pass
    
    def VisualizaTarefas(self):
        pass
    
    def RemoverTarefa(self):
        pass
    
    

