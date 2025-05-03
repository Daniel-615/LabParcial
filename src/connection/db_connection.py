
import os
from dotenv import load_dotenv
if not load_dotenv(override=True):
    print("Warning: .env file not found or could not be loaded.")
class Connection:
    def __init__(self):
        self.user_sql_server = os.getenv("DB_USER_SQL_SERVER")
        self.password_sql_server = os.getenv("DB_PASSWORD_SQL_SERVER")
        self.database_sql_server = os.getenv("DB_NAME_SQL_SERVER")
        self.port_sql_server = os.getenv("DB_PORT_SQL_SERVER")
        self.host_oracle = os.getenv("DB_HOST_ORACLE")
        self.user_oracle = os.getenv("DB_USER_ORACLE")
        self.password_oracle = os.getenv("DB_PASSWORD_ORACLE")
        self.database_oracle = os.getenv("DB_NAME_ORACLE")
        self.port_oracle = os.getenv("DB_PORT_ORACLE")
        

    def connect_sqlserver(self):
        try:
            connection_url = (
                f"mssql+pyodbc://{self.user_sql_server}:{self.password_sql_server}@"
                f"JOSEILLESCAS/lab"
                f"?driver=ODBC+Driver+17+for+SQL+Server&encrypt=yes&TrustServerCertificate=yes"
            )
            return connection_url
        except Exception as e:
            print(f"Error al construir la URL de conexión: {e}")
            return None
    def connect_oracle(self):
        try:
            connection_url = (
                f"oracle+oracledb://{self.user_oracle}:{self.password_oracle}@"
                f"{self.host_oracle}:{self.port_oracle}/?service_name={self.database_oracle}"
            )
            return connection_url
        except Exception as e:
            print(f"Error al construir la URL de conexión Oracle: {e}")
            return None