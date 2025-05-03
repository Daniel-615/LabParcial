from flask import Flask
from src.connection.db_connection import Connection
from src.models.models import Models
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from src.lab.OracleHelper import OracleHelper
from src.config.config import Config

class Main:
    def __init__(self):
        self.app = Flask(__name__)
        self.connection = Connection()

        try:
            # Obtener URIs para cada sede
            #uri_guatemala = self.connection.connect_sqlserver_guatemala()
            uri_mexico = self.connection.connect_sqlserver_mexico()
            uri_elsalvador = self.connection.connect_sqlserver_elsalvador()
            uri_oracle = self.connection.connect_oracle()

            # Validar URIs necesarias
            if not all([ uri_mexico, uri_elsalvador, uri_oracle]):
                raise ValueError("Faltan una o más URIs de conexión a las bases de datos.")

            # Base de datos principal
            self.app.config['SQLALCHEMY_DATABASE_URI'] = uri_oracle

            # Bases de datos adicionales por sede
            self.app.config['SQLALCHEMY_BINDS'] = {
                'mexico': uri_mexico,
                'salvador': uri_elsalvador,
                'oracle': uri_oracle
            }

        except Exception as e:
            print(f"\n❌ Error al establecer conexiones a las bases de datos: {e}\n")

        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Inicializar ORM y modelos
        self.db = SQLAlchemy(self.getApp())
        self.models = Models(self.db)

        # Configurar controladores y rutas
        self.app_initializer = Config(self.getApp(), self.db, self.models)

        with self.app.app_context():
            self.db.create_all()
            # Crear secuencia y trigger en Oracle
            oracle_helper = OracleHelper(self.db)
            oracle_helper.create_auto_increment("LOG_ASUNTO")

        # Inicializar sistema de migraciones
        self.migrate = Migrate(self.getApp(), self.db)

    def startApp(self):
        self.app.run(debug=True, host="0.0.0.0", port=5000)

    def getApp(self):
        return self.app
