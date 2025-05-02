# CONTROLADORES
from src.lab.controllers.cliente import Cliente as ClienteController
from src.lab.controllers.asunto import Asunto as AsuntoController
from src.lab.controllers.abogado import Abogado as AbogadoController
from src.lab.controllers.gabinete import Gabinete as GabineteController
from src.lab.controllers.abogado_gabinete import AbogadoGabinete as AbogadoGabineteController
from src.lab.controllers.audiencia import Audiencia as AudienciaController
from src.lab.controllers.incidencia import Incidencia as IncidenciaController
from src.lab.controllers.log_asunto import LogAsunto as LogAsuntoController

# RUTAS
from src.lab.routes.cliente import Cliente as ClienteRoute
from src.lab.routes.asunto import Asunto as AsuntoRoute
from src.lab.routes.abogado import Abogado as AbogadoRoute
from src.lab.routes.gabinete import Gabinete as GabineteRoute
from src.lab.routes.abogado_gabinete import AbogadoGabinete as AbogadoGabineteRoute
from src.lab.routes.audiencia import Audiencia as AudienciaRoute
from src.lab.routes.incidencia import Incidencia as IncidenciaRoute
from src.lab.routes.log_asunto import LogAsunto as LogAsuntoRoute

class Config:
    def __init__(self, app, db, models):
        self.app = app
        self.db = db
        self.models = models

        self.controllers_oracle(db, models)
        self.controllers_sql_server(db, models)

        self.routes_oracle()
        self.routes_sql_server()

    # Getters
    def getModels(self):
        return self.models

    # SQL SERVER: Getters para controladores
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

    # Oracle: Getter
    def getLogAsuntoControllers(self):
        return self.log_asunto

    # INSTANCIACIÓN DE CONTROLADORES (lógica de negocio)
    def controllers_sql_server(self, db, models):
        self.cliente = ClienteController(db, models)
        self.asunto = AsuntoController(db, models)
        self.abogado = AbogadoController(db, models)
        self.gabinete = GabineteController(db, models)
        self.abogado_gabinete = AbogadoGabineteController(db, models)
        self.audiencia = AudienciaController(db, models)
        self.incidencia = IncidenciaController(db, models)

    def controllers_oracle(self, db, models):
        self.log_asunto = LogAsuntoController(db, models)

    # REGISTRO DE RUTAS (API)
    def routes_sql_server(self):
        self.cliente_route = ClienteRoute(self.app, self)
        self.asunto_route = AsuntoRoute(self.app, self)
        self.abogado_route = AbogadoRoute(self.app, self)
        self.gabinete_route = GabineteRoute(self.app, self)
        self.abogado_gabinete_route = AbogadoGabineteRoute(self.app, self)
        self.audiencia_route = AudienciaRoute(self.app, self)
        self.incidencia_route = IncidenciaRoute(self.app, self)

    def routes_oracle(self):
        self.log_asunto_route = LogAsuntoRoute(self.app, self)
