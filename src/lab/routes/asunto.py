from flask import request

class Asunto:
    def __init__(self, app, app_initializer, sede):
        self.app = app
        self.app_initializer = app_initializer
        self.sede = sede
        self.routes()

    def routes(self):
        base_path = f'/v1/{self.sede}/asunto'

        @self.app.route(f'{base_path}', methods=['GET'], endpoint=f'get_asunto_{self.sede}')
        def get_asunto():
            """
            Obtener todos los asuntos.
            ---
            tags:
              - Asunto
            parameters:
              - name: page
                in: query
                type: integer
                description: Página actual
              - name: page_size
                in: query
                type: integer
                description: Cantidad de resultados por página
            responses:
              200:
                description: Lista de asuntos obtenida exitosamente
              404:
                description: No hay asuntos disponibles
            """
            return self.app_initializer.getAsuntoController(self.sede).get_asunto()

        @self.app.route(f'{base_path}/<string:expediente>', methods=['GET'], endpoint=f'get_asunto_by_id_{self.sede}')
        def get_asunto_by_id(expediente):
            """
            Obtener asunto por expediente.
            ---
            tags:
              - Asunto
            parameters:
              - name: expediente
                in: path
                required: true
                type: string
                description: Número de expediente del asunto
            responses:
              200:
                description: Asunto encontrado
              404:
                description: Asunto no encontrado
            """
            return self.app_initializer.getAsuntoController(self.sede).get_asunto_by_id(expediente)

        @self.app.route(f'{base_path}', methods=['POST'], endpoint=f'create_asunto_{self.sede}')
        def create_asunto():
            """
            Crear nuevo asunto.
            ---
            tags:
              - Asunto
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    required:
                      - expediente
                      - cliente_id
                    properties:
                      expediente:
                        type: string
                        example: "EXP-2025-001"
                      cliente_id:
                        type: integer
                        example: 5
                      estado:
                        type: string
                        example: "en trámite"
            responses:
              201:
                description: Asunto creado exitosamente
              400:
                description: Datos inválidos o sede incorrecta
            """
            return self.app_initializer.getAsuntoController(self.sede).create_asunto(request.json)

        @self.app.route(f'{base_path}/<string:expediente>', methods=['PUT'], endpoint=f'update_asunto_{self.sede}')
        def update_asunto(expediente):
            """
            Actualizar asunto por expediente.
            ---
            tags:
              - Asunto
            parameters:
              - name: expediente
                in: path
                required: true
                type: string
                description: Número de expediente del asunto a actualizar
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      estado:
                        type: string
                        example: "finalizado"
                      fecha_fin:
                        type: string
                        format: date
                        example: "2025-12-01"
            responses:
              200:
                description: Asunto actualizado exitosamente
              400:
                description: Datos inválidos o formato de fecha incorrecto
              404:
                description: Asunto no encontrado
            """
            return self.app_initializer.getAsuntoController(self.sede).update_asunto(expediente, request.json)
