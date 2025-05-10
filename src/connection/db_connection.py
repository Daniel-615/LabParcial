import os
from dotenv import load_dotenv

if not load_dotenv(override=True):
    print("Warning: .env file not found or could not be loaded.")

class Connection:
    def __init__(self):
        # México
        self.user_sql_mx = os.getenv("DB_USER_SQL_MX")
        self.pass_sql_mx = os.getenv("DB_PASSWORD_SQL_MX")
        self.db_sql_mx = os.getenv("DB_NAME_SQL_MX")
        self.host_sql_mx = os.getenv("DB_HOST_SQL_MX")

        # El Salvador
        self.user_sql_sv = os.getenv("DB_USER_SQL_SV")
        self.pass_sql_sv = os.getenv("DB_PASSWORD_SQL_SV")
        self.db_sql_sv = os.getenv("DB_NAME_SQL_SV")
        self.host_sql_sv = os.getenv("DB_HOST_SQL_SV")

        # Oracle
        self.host_oracle = os.getenv("DB_HOST_ORACLE")
        self.user_oracle = os.getenv("DB_USER_ORACLE")
        self.password_oracle = os.getenv("DB_PASSWORD_ORACLE")
        self.database_oracle = os.getenv("DB_NAME_ORACLE")
        self.port_oracle = os.getenv("DB_PORT_ORACLE")

    def connect_sqlserver_guatemala(self):
        return (
            f"mssql+pyodbc://{self.user_sql_gt}:{self.pass_sql_gt}@{self.host_sql_gt}/{self.db_sql_gt}"
            f"?driver=ODBC+Driver+17+for+SQL+Server&encrypt=yes&TrustServerCertificate=yes"
        )

    def connect_sqlserver_mexico(self):
        return (
            f"mssql+pyodbc://{self.user_sql_mx}:{self.pass_sql_mx}@{self.host_sql_mx}/{self.db_sql_mx}"
            f"?driver=ODBC+Driver+17+for+SQL+Server&encrypt=yes&TrustServerCertificate=yes"
        )

    def connect_sqlserver_elsalvador(self):
        return (
            f"mssql+pyodbc://{self.user_sql_sv}:{self.pass_sql_sv}@{self.host_sql_sv}/{self.db_sql_sv}"
            f"?driver=ODBC+Driver+17+for+SQL+Server&encrypt=yes&TrustServerCertificate=yes"
        )

    def connect_oracle(self):
        return (
            f"oracle+oracledb://{self.user_oracle}:{self.password_oracle}@"
            f"{self.host_oracle}:{self.port_oracle}/?service_name={self.database_oracle}"
        )
