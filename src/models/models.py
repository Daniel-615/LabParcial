class Models:
    def __init__(self, db):
        self.db = db

        # --- SQL Server - El Salvador ---
        class CLIENTE_SV(db.Model):
            __tablename__ = 'CLIENTE'
            __bind_key__ = 'salvador'
            id = db.Column(db.Integer, primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)
            direccion = db.Column(db.String(255))
            telefono = db.Column(db.String(50))
            email = db.Column(db.String(100))

            def to_dict(self):
                return vars(self)

        self.CLIENTE_SV = CLIENTE_SV

        class ASUNTO_SV(db.Model):
            __tablename__ = 'ASUNTO'
            __bind_key__ = 'salvador'
            expediente = db.Column(db.String(100), primary_key=True)
            fecha_inicio = db.Column(db.Date, default=db.func.current_date())
            fecha_fin = db.Column(db.Date)
            estado = db.Column(db.String(50))
            cliente_id = db.Column(db.Integer, db.ForeignKey('CLIENTE.id'), nullable=False)

            def to_dict(self):
                return vars(self)

        self.ASUNTO_SV = ASUNTO_SV

        class ABOGADO_SV(db.Model):
            __tablename__ = 'ABOGADO'
            __bind_key__ = 'salvador'
            pasaporte = db.Column(db.String(50), primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)

            def to_dict(self):
                return vars(self)

        self.ABOGADO_SV = ABOGADO_SV

        class GABINETE_SV(db.Model):
            __tablename__ = 'GABINETE'
            __bind_key__ = 'salvador'
            id = db.Column(db.Integer, primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)
            pais = db.Column(db.String(100))
            sistema_operativo = db.Column(db.String(100))

            def to_dict(self):
                return vars(self)

        self.GABINETE_SV = GABINETE_SV

        class ABOGADO_GABINETE_SV(db.Model):
            __tablename__ = 'ABOGADO_GABINETE'
            __bind_key__ = 'salvador'
            pasaporte = db.Column(db.String(50), db.ForeignKey('ABOGADO.pasaporte'), primary_key=True)
            gabinete_id = db.Column(db.Integer, db.ForeignKey('GABINETE.id'), primary_key=True)

            def to_dict(self):
                return vars(self)

        self.ABOGADO_GABINETE_SV = ABOGADO_GABINETE_SV

        class AUDIENCIA_SV(db.Model):
            __tablename__ = 'AUDIENCIA'
            __bind_key__ = 'salvador'
            id = db.Column(db.Integer, primary_key=True)
            asunto_exp = db.Column(db.String(100), db.ForeignKey('ASUNTO.expediente'), nullable=False)
            fecha = db.Column(db.DateTime, nullable=False)
            abogado_pasaporte = db.Column(db.String(50), db.ForeignKey('ABOGADO.pasaporte'), nullable=False)

            def to_dict(self):
                return vars(self)

        self.AUDIENCIA_SV = AUDIENCIA_SV

        class INCIDENCIA_SV(db.Model):
            __tablename__ = 'INCIDENCIA'
            __bind_key__ = 'salvador'
            id = db.Column(db.Integer, primary_key=True)
            audiencia_id = db.Column(db.Integer, db.ForeignKey('AUDIENCIA.id'), nullable=False)
            descripcion = db.Column(db.String(1000), nullable=False)

            def to_dict(self):
                return vars(self)

        self.INCIDENCIA_SV = INCIDENCIA_SV

        # --- SQL Server - Mexico ---
        class CLIENTE_MX(db.Model):
            __tablename__ = 'CLIENTE'
            __bind_key__ = 'mexico'
            id = db.Column(db.Integer, primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)
            direccion = db.Column(db.String(255))
            telefono = db.Column(db.String(50))
            email = db.Column(db.String(100))

            def to_dict(self):
                return vars(self)

        self.CLIENTE_MX = CLIENTE_MX

        class ASUNTO_MX(db.Model):
            __tablename__ = 'ASUNTO'
            __bind_key__ = 'mexico'
            expediente = db.Column(db.String(100), primary_key=True)
            fecha_inicio = db.Column(db.Date, default=db.func.current_date())
            fecha_fin = db.Column(db.Date)
            estado = db.Column(db.String(50))
            cliente_id = db.Column(db.Integer, db.ForeignKey('CLIENTE.id'), nullable=False)

            def to_dict(self):
                return vars(self)

        self.ASUNTO_MX = ASUNTO_MX

        class ABOGADO_MX(db.Model):
            __tablename__ = 'ABOGADO'
            __bind_key__ = 'mexico'
            pasaporte = db.Column(db.String(50), primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)

            def to_dict(self):
                return vars(self)

        self.ABOGADO_MX = ABOGADO_MX

        class GABINETE_MX(db.Model):
            __tablename__ = 'GABINETE'
            __bind_key__ = 'mexico'
            id = db.Column(db.Integer, primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)
            pais = db.Column(db.String(100))
            sistema_operativo = db.Column(db.String(100))

            def to_dict(self):
                return vars(self)

        self.GABINETE_MX = GABINETE_MX

        class ABOGADO_GABINETE_MX(db.Model):
            __tablename__ = 'ABOGADO_GABINETE'
            __bind_key__ = 'mexico'
            pasaporte = db.Column(db.String(50), db.ForeignKey('ABOGADO.pasaporte'), primary_key=True)
            gabinete_id = db.Column(db.Integer, db.ForeignKey('GABINETE.id'), primary_key=True)

            def to_dict(self):
                return vars(self)

        self.ABOGADO_GABINETE_MX = ABOGADO_GABINETE_MX

        class AUDIENCIA_MX(db.Model):
            __tablename__ = 'AUDIENCIA'
            __bind_key__ = 'mexico'
            id = db.Column(db.Integer, primary_key=True)
            asunto_exp = db.Column(db.String(100), db.ForeignKey('ASUNTO.expediente'), nullable=False)
            fecha = db.Column(db.DateTime, nullable=False)
            abogado_pasaporte = db.Column(db.String(50), db.ForeignKey('ABOGADO.pasaporte'), nullable=False)

            def to_dict(self):
                return vars(self)

        self.AUDIENCIA_MX = AUDIENCIA_MX

        class INCIDENCIA_MX(db.Model):
            __tablename__ = 'INCIDENCIA'
            __bind_key__ = 'mexico'
            id = db.Column(db.Integer, primary_key=True)
            audiencia_id = db.Column(db.Integer, db.ForeignKey('AUDIENCIA.id'), nullable=False)
            descripcion = db.Column(db.String(1000), nullable=False)

            def to_dict(self):
                return vars(self)

        self.INCIDENCIA_MX = INCIDENCIA_MX

        # --- Oracle - Central ---
        class LOG_ASUNTO(db.Model):
            __bind_key__ = 'oracle'
            __tablename__ = 'LOG_ASUNTO'
            id = db.Column(db.Integer, primary_key=True)
            expediente = db.Column(db.String(100), nullable=False)
            accion = db.Column(db.String(50), nullable=False)
            timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

            def to_dict(self):
                return vars(self)

        self.LOG_ASUNTO = LOG_ASUNTO
