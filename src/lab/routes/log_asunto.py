from flask import request

class LogAsunto:
    def __init__(self, app, app_initializer):
        self.app = app
        self.app_initializer = app_initializer
        self.routes()

    def routes(self):
        @self.app.route('/v1/log_asunto', methods=['GET'])
        def get_logs():
            """
            Obtener todos los registros del log de asuntos.
            ---
            tags:
              - LogAsunto
            responses:
              200:
                description: Lista de registros obtenida correctamente.
              404:
                description: No se encontraron registros.
            """
            return self.app_initializer.getLogAsuntoController().get_logs()

        @self.app.route('/v1/log_asunto/<int:id>', methods=['GET'])
        def get_log_by_id(id):
            """
            Obtener un registro del log por ID.
            ---
            tags:
              - LogAsunto
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID del registro en el log
            responses:
              200:
                description: Registro encontrado.
              404:
                description: Registro no encontrado.
            """
            return self.app_initializer.getLogAsuntoController().get_log_by_id(id)

        @self.app.route('/v1/log_asunto', methods=['POST'])
        def create_log():
            """
            Crear un nuevo registro en el log de asuntos.
            ---
            tags:
              - LogAsunto
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    required:
                      - expediente
                      - accion
                    properties:
                      expediente:
                        type: string
                        example: "EXP12345"
                      accion:
                        type: string
                        example: "ASUNTO CREADO"
            responses:
              201:
                description: Registro creado correctamente.
              400:
                description: Datos faltantes o inválidos.
            """
            return self.app_initializer.getLogAsuntoController().create_log(request.json)

        @self.app.route('/v1/log_asunto/<int:id>', methods=['PUT'])
        def update_log(id):
            """
            Actualizar un registro del log por ID.
            ---
            tags:
              - LogAsunto
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID del log a actualizar
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      accion:
                        type: string
                        example: "ACTUALIZACIÓN DE AUDIENCIA"
            responses:
              200:
                description: Registro actualizado correctamente.
              404:
                description: Registro no encontrado.
            """
            return self.app_initializer.getLogAsuntoController().update_log(id, request.json)

        @self.app.route('/v1/inner_join/log_asunto', methods=['GET'])
        def inner_join():
            """
            Obtener registros del log con detalles del asunto asociado (unión distribuida).
            ---
            tags:
              - LogAsunto
            responses:
              200:
                description: Registros del log con asuntos relacionados.
              404:
                description: No se encontraron resultados combinados.
            """
            return self.app_initializer.getLogAsuntoController().innerJoin()
