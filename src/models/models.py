class Models:
    def __init__(self, db):
        self.db = db

        # --- SQL Server - Sucursales ---
        class CLIENTE(db.Model):
            __tablename__ = 'CLIENTE'
            __table_args__ = {'extend_existing': True}

            id = db.Column(db.Integer, primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)
            direccion = db.Column(db.String(255))
            telefono = db.Column(db.String(50))
            email = db.Column(db.String(100))

            def to_dict(self):
                return {
                    'id': self.id,
                    'nombre': self.nombre,
                    'direccion': self.direccion,
                    'telefono': self.telefono,
                    'email': self.email
                }

        self.CLIENTE = CLIENTE

        class ASUNTO(db.Model):
            __tablename__ = 'ASUNTO'
            __table_args__ = {'extend_existing': True}

            expediente = db.Column(db.String(100), primary_key=True)
            fecha_inicio = db.Column(db.Date, default=db.func.current_date())
            fecha_fin = db.Column(db.Date)
            estado = db.Column(db.String(50))
            cliente_id = db.Column(db.Integer, db.ForeignKey('CLIENTE.id'), nullable=False)

            def to_dict(self):
                return {
                    'expediente': self.expediente,
                    'fecha_inicio': str(self.fecha_inicio),
                    'fecha_fin': str(self.fecha_fin),
                    'estado': self.estado,
                    'cliente_id': self.cliente_id
                }

        self.ASUNTO = ASUNTO

        class ABOGADO(db.Model):
            __tablename__ = 'ABOGADO'
            __table_args__ = {'extend_existing': True}

            pasaporte = db.Column(db.String(50), primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)

            def to_dict(self):
                return {
                    'pasaporte': self.pasaporte,
                    'nombre': self.nombre
                }

        self.ABOGADO = ABOGADO

        class GABINETE(db.Model):
            __tablename__ = 'GABINETE'
            __table_args__ = {'extend_existing': True}

            id = db.Column(db.Integer, primary_key=True)
            nombre = db.Column(db.String(255), nullable=False)
            pais = db.Column(db.String(100))
            sistema_operativo = db.Column(db.String(100))

            def to_dict(self):
                return {
                    'id': self.id,
                    'nombre': self.nombre,
                    'pais': self.pais,
                    'sistema_operativo': self.sistema_operativo
                }

        self.GABINETE = GABINETE

        class ABOGADO_GABINETE(db.Model):
            __tablename__ = 'ABOGADO_GABINETE'
            __table_args__ = {'extend_existing': True}

            pasaporte = db.Column(db.String(50), db.ForeignKey('ABOGADO.pasaporte'), primary_key=True)
            gabinete_id = db.Column(db.Integer, db.ForeignKey('GABINETE.id'), primary_key=True)

            def to_dict(self):
                return {
                    'pasaporte': self.pasaporte,
                    'gabinete_id': self.gabinete_id
                }

        self.ABOGADO_GABINETE = ABOGADO_GABINETE

        class AUDIENCIA(db.Model):
            __tablename__ = 'AUDIENCIA'
            __table_args__ = {'extend_existing': True}

            id = db.Column(db.Integer, primary_key=True)
            asunto_exp = db.Column(db.String(100), db.ForeignKey('ASUNTO.expediente'), nullable=False)
            fecha = db.Column(db.DateTime, nullable=False)
            abogado_pasaporte = db.Column(db.String(50), db.ForeignKey('ABOGADO.pasaporte'), nullable=False)

            def to_dict(self):
                return {
                    'id': self.id,
                    'asunto_exp': self.asunto_exp,
                    'fecha': str(self.fecha),
                    'abogado_pasaporte': self.abogado_pasaporte
                }

        self.AUDIENCIA = AUDIENCIA

        class INCIDENCIA(db.Model):
            __tablename__ = 'INCIDENCIA'
            __table_args__ = {'extend_existing': True}

            id = db.Column(db.Integer, primary_key=True)
            audiencia_id = db.Column(db.Integer, db.ForeignKey('AUDIENCIA.id'), nullable=False)
            descripcion = db.Column(db.String(1000), nullable=False)

            def to_dict(self):
                return {
                    'id': self.id,
                    'audiencia_id': self.audiencia_id,
                    'descripcion': self.descripcion
                }

        self.INCIDENCIA = INCIDENCIA

        # --- Oracle - Central ---
        class LOG_ASUNTO(db.Model):
            __bind_key__ = 'oracle'
            __tablename__ = 'LOG_ASUNTO'
            __table_args__ = {'extend_existing': True}

            id = db.Column(db.Integer, primary_key=True)
            expediente = db.Column(db.String(100), nullable=False)
            accion = db.Column(db.String(50), nullable=False)
            timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

            def to_dict(self):
                return {
                    'id': self.id,
                    'expediente': self.expediente,
                    'accion': self.accion,
                    'timestamp': str(self.timestamp)
                }

        self.LOG_ASUNTO = LOG_ASUNTO
