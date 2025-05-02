from src.lab.controllers.cliente import Cliente
from src.lab.controllers.asunto import Asunto
from src.lab.controllers.abogado import Abogado
from src.lab.controllers.gabinete import Gabinete   
from src.lab.controllers.abogado_gabinete import AbogadoGabinete
from src.lab.controllers.audiencia import Audiencia 
from src.lab.controllers.incidencia import Incidencia
from src.lab.controllers.log_asunto import LogAsunto

from src.lab.routes.cliente import Cliente
from src.lab.routes.asunto import Asunto
from src.lab.routes.abogado import Abogado
from src.lab.routes.gabinete import Gabinete   
from src.lab.routes.abogado_gabinete import AbogadoGabinete
from src.lab.routes.audiencia import Audiencia 
from src.lab.routes.incidencia import Incidencia
from src.lab.routes.log_asunto import LogAsunto

class Config:
    def __init__(self,app,db,models):
        self.app=app
        self.db=db
        self.models=models
        self.controllers_oracle(db,models)
        self.controllers_sql_server(db,models)
        self.routes_oracle()
        self.routes_sql_server()
    #Geters
    def getModels(self):
        return self.models
    #SQL SERVER
    def getClienteControllers(self):
        return self.cliente
    def getAsuntoControllers(self):
        return self.asunto
    def getAbogadoControllers(self):
        return self.abogado
    def getGabineteControllers(self):
        return self.gabinete
    def getAbogadoGabineteControllers(self):
        return self.abogado_gabinete
    def getAudienciaControllers(self):
        return self.audiencia
    def getIncidenciaControllers(self):
        return self.incidencia
    #Oracle
    def getLogAsuntoControllers(self):
        return self.log_asunto
    def controllers_sql_server(self,db,models):
        self.cliente=Cliente(db,models)
        self.asunto=Asunto(db,models)
        self.abogado=Abogado(db,models)
        self.gabinete=Gabinete(db,models)   
        self.abogado_gabinete=AbogadoGabinete(db,models)
        self.audiencia=Audiencia(db,models) 
        self.incidencia=Incidencia(db,models)
    def controllers_oracle(self,db,models):
        self.log_asunto=LogAsunto(db,models)
    def routes_sql_server(self):
        self.cliente=Cliente(self.app,self)
        self.asunto=Asunto(self.app,self)
        self.abogado=Abogado(self.app,self)
        self.gabinete=Gabinete(self.app,self)
        self.abogado_gabinete=AbogadoGabinete(self.app,self)
        self.audiencia=Audiencia(self.app,self)
        self.incidencia=Incidencia(self.app,self)
    def routes_oracle(self):
        self.log_asunto=LogAsunto(self.app,self)