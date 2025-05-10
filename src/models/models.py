class Models:
    def __init__(self, db):
        self.db = db
        class BaseModel(db.Model):
            __abstract__ = True  # no se crea tabla de esta clase

            def to_dict(self):
                """Devuelve todos los atributos como diccionario."""
                return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        class ClienteBase(BaseModel):
            __abstract__=True
            id = db.Column(db.Integer, primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)
            direccion = db.Column(db.String(255))
            telefono = db.Column(db.String(50))
            email = db.Column(db.String(100))
        class AsuntoBase(BaseModel):
            __abstract__=True
            expediente = db.Column(db.String(100), primary_key=True)
            fecha_inicio = db.Column(db.Date, default=db.func.current_date())
            fecha_fin = db.Column(db.Date)
            estado = db.Column(db.String(50))
            cliente_id = db.Column(db.Integer, db.ForeignKey('CLIENTE.id'), nullable=False)
        class GabineteBase(BaseModel):
            __abstract__=True
            id = db.Column(db.Integer, primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)
            pais = db.Column(db.String(100))
            sistema_operativo = db.Column(db.String(100))
        class AbogadoBase(BaseModel):
            __abstract__=True
            pasaporte = db.Column(db.String(50), primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)
        class AbogadoGabineteBase(BaseModel):
            __abstract__=True
            pasaporte = db.Column(db.String(50), db.ForeignKey('ABOGADO.pasaporte'), primary_key=True)
            gabinete_id = db.Column(db.Integer, db.ForeignKey('GABINETE.id'), primary_key=True)
        class AudienciaBase(BaseModel):
            __abstract__=True
            id = db.Column(db.Integer, primary_key=True)
            asunto_exp = db.Column(db.String(100), db.ForeignKey('ASUNTO.expediente'), nullable=False)
            fecha = db.Column(db.DateTime, nullable=False)
            abogado_pasaporte = db.Column(db.String(50), db.ForeignKey('ABOGADO.pasaporte'), nullable=False)
        class IncidenciaBase(BaseModel):
            __abstract__=True
            id = db.Column(db.Integer, primary_key=True)
            audiencia_id = db.Column(db.Integer, db.ForeignKey('AUDIENCIA.id'), nullable=False)
            descripcion = db.Column(db.String(1000), nullable=False)

        # --- SQL Server - El Salvador ---
        class CLIENTE_SV(ClienteBase):
            __tablename__ = 'CLIENTE'
            __bind_key__ = 'salvador'
        self.CLIENTE_SV = CLIENTE_SV
        class ASUNTO_SV(AsuntoBase):
            __tablename__ = 'ASUNTO'
            __bind_key__ = 'salvador'

        self.ASUNTO_SV = ASUNTO_SV

        class ABOGADO_SV(AbogadoBase):
            __tablename__ = 'ABOGADO'
            __bind_key__ = 'salvador'
        self.ABOGADO_SV = ABOGADO_SV

        class GABINETE_SV(GabineteBase):
            __tablename__ = 'GABINETE'
            __bind_key__ = 'salvador'
        self.GABINETE_SV = GABINETE_SV

        class ABOGADO_GABINETE_SV(AbogadoGabineteBase):
            __tablename__ = 'ABOGADO_GABINETE'
            __bind_key__ = 'salvador'
        self.ABOGADO_GABINETE_SV = ABOGADO_GABINETE_SV

        class AUDIENCIA_SV(AudienciaBase):
            __tablename__ = 'AUDIENCIA'
            __bind_key__ = 'salvador'
        self.AUDIENCIA_SV = AUDIENCIA_SV

        class INCIDENCIA_SV(IncidenciaBase):
            __tablename__ = 'INCIDENCIA'
            __bind_key__ = 'salvador'
        self.INCIDENCIA_SV = INCIDENCIA_SV

        # --- SQL Server - Mexico ---
        class CLIENTE_MX(ClienteBase):
            __tablename__ = 'CLIENTE'
            __bind_key__ = 'mexico'
        self.CLIENTE_MX = CLIENTE_MX

        class ASUNTO_MX(AsuntoBase):
            __tablename__ = 'ASUNTO'
            __bind_key__ = 'mexico'
        self.ASUNTO_MX = ASUNTO_MX

        class ABOGADO_MX(AbogadoBase):
            __tablename__ = 'ABOGADO'
            __bind_key__ = 'mexico'
        self.ABOGADO_MX = ABOGADO_MX

        class GABINETE_MX(GabineteBase):
            __tablename__ = 'GABINETE'
            __bind_key__ = 'mexico'
        self.GABINETE_MX = GABINETE_MX

        class ABOGADO_GABINETE_MX(AbogadoGabineteBase):
            __tablename__ = 'ABOGADO_GABINETE'
            __bind_key__ = 'mexico'
        self.ABOGADO_GABINETE_MX = ABOGADO_GABINETE_MX

        class AUDIENCIA_MX(AudienciaBase):
            __tablename__ = 'AUDIENCIA'
            __bind_key__ = 'mexico'
        self.AUDIENCIA_MX = AUDIENCIA_MX

        class INCIDENCIA_MX(IncidenciaBase):
            __tablename__ = 'INCIDENCIA'
            __bind_key__ = 'mexico'
        self.INCIDENCIA_MX = INCIDENCIA_MX

        # --- Oracle - Central ---
        class LOG_ASUNTO(BaseModel):
            __bind_key__ = 'oracle'
            __tablename__ = 'LOG_ASUNTO'
            id = db.Column(db.Integer, primary_key=True)
            expediente = db.Column(db.String(100), nullable=False)
            accion = db.Column(db.String(50), nullable=False)
            timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
        self.LOG_ASUNTO = LOG_ASUNTO
    # Diccionarios para acceder por sede
        self.ASUNTO = {
            'salvador': self.ASUNTO_SV,
            'mexico': self.ASUNTO_MX
        }
        self.CLIENTE = {
            'salvador': self.CLIENTE_SV,
            'mexico': self.CLIENTE_MX
        }

        self.ABOGADO = {
            'salvador': self.ABOGADO_SV,
            'mexico': self.ABOGADO_MX
        }

        self.GABINETE = {
            'salvador': self.GABINETE_SV,
            'mexico': self.GABINETE_MX
        }

        self.ABOGADO_GABINETE = {
            'salvador': self.ABOGADO_GABINETE_SV,
            'mexico': self.ABOGADO_GABINETE_MX
        }

        self.AUDIENCIA = {
            'salvador': self.AUDIENCIA_SV,
            'mexico': self.AUDIENCIA_MX
        }

        self.INCIDENCIA = {
            'salvador': self.INCIDENCIA_SV,
            'mexico': self.INCIDENCIA_MX
        }