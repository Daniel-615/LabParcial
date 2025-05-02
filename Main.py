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
            uri_sql_server=self.connection.connect_sqlserver()
            if not uri_sql_server:
                raise ValueError("No se pudo encontrar la URI de la base de datos.")
            self.app.config['SQLALCHEMY_DATABASE_URI'] = uri_sql_server
            self.app.config['SQLALCHEMY_BINDS'] = {
                'oracle': self.connection.connect_oracle()
            }  
        except Exception as e:
            print(f"Error al conectarse: {e}")
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
        
        self.db = SQLAlchemy(self.getApp())
        self.models = Models(self.db)
        self.app_initializer = Config(self.getApp(), self.db, self.models)

        with self.app.app_context():
                self.db.create_all() 
                oracle_helper = OracleHelper(self.db)
                oracle_helper.create_auto_increment("LOG_ASUNTO")

        self.migrate = Migrate(self.getApp(), self.db)  # Migraciones de la base de datos
    def startApp(self):
        self.app.run(debug=True,host="0.0.0.0",port=5000)
    def getApp(self):
        return self.app