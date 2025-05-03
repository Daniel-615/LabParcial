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

        # Controladores SQL Server por sede
        self.controllers_sql_server('salvador')
        self.controllers_sql_server('mexico')
        self.controllers_oracle()

        # Rutas
        self.routes_sql_server('salvador')
        self.routes_sql_server('mexico')
        self.routes_oracle()

    # SQL SERVER: Getters generales por sede
    def getClienteController(self, sede): return self.cliente[sede]
    def getAsuntoController(self, sede): return self.asunto[sede]
    def getAbogadoController(self, sede): return self.abogado[sede]
    def getGabineteController(self, sede): return self.gabinete[sede]
    def getAbogadoGabineteController(self, sede): return self.abogado_gabinete[sede]
    def getAudienciaController(self, sede): return self.audiencia[sede]
    def getIncidenciaController(self, sede): return self.incidencia[sede]

    # Oracle: Getter único
    def getLogAsuntoController(self): return self.log_asunto

    def controllers_sql_server(self, sede):
        if not hasattr(self, 'cliente'):
            self.cliente = {}
            self.asunto = {}
            self.abogado = {}
            self.gabinete = {}
            self.abogado_gabinete = {}
            self.audiencia = {}
            self.incidencia = {}

        self.cliente[sede] = ClienteController(self.db, self.models, sede)
        self.asunto[sede] = AsuntoController(self.db, self.models, sede)
        self.abogado[sede] = AbogadoController(self.db, self.models, sede)
        self.gabinete[sede] = GabineteController(self.db, self.models, sede)
        self.abogado_gabinete[sede] = AbogadoGabineteController(self.db, self.models, sede)
        self.audiencia[sede] = AudienciaController(self.db, self.models, sede)
        self.incidencia[sede] = IncidenciaController(self.db, self.models, sede)

    def controllers_oracle(self):
        self.log_asunto = LogAsuntoController(self.db, self.models)

    def routes_sql_server(self, sede):
        ClienteRoute(self.app, self, sede)
        AsuntoRoute(self.app, self, sede)
        AbogadoRoute(self.app, self, sede)
        GabineteRoute(self.app, self, sede)
        AbogadoGabineteRoute(self.app, self, sede)
        AudienciaRoute(self.app, self, sede)
        IncidenciaRoute(self.app, self, sede)

    def routes_oracle(self):
        LogAsuntoRoute(self.app, self)
