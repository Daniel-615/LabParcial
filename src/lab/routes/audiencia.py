from flask import request

class Audiencia:
    def __init__(self, app, app_initializer, sede):
        self.app = app
        self.app_initializer = app_initializer
        self.sede = sede
        self.routes()

    def routes(self):
        base_path = f'/v1/{self.sede}/audiencia'

        @self.app.route(f'{base_path}', methods=['GET'], endpoint=f'get_audiencia_{self.sede}')
        def get_audiencia():
            """
            Obtener todas las audiencias.
            ---
            tags:
              - Audiencia
            parameters:
              - name: page
                in: query
                type: integer
                description: Página actual
              - name: per_page
                in: query
                type: integer
                description: Número de resultados por página
            responses:
              200:
                description: Lista de audiencias obtenida exitosamente
              404:
                description: No hay audiencias registradas
            """
            return self.app_initializer.getAudienciaController(self.sede).get_all_audiencias()

        @self.app.route(f'{base_path}/<int:id>', methods=['GET'], endpoint=f'get_audiencia_by_id_{self.sede}')
        def get_audiencia_by_id(id):
            """
            Obtener audiencia por ID.
            ---
            tags:
              - Audiencia
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID único de la audiencia
            responses:
              200:
                description: Audiencia encontrada
              404:
                description: Audiencia no encontrada
            """
            return self.app_initializer.getAudienciaController(self.sede).get_audiencia_by_id(id)

        @self.app.route(f'{base_path}', methods=['POST'], endpoint=f'create_audiencia_{self.sede}')
        def create_audiencia():
            """
            Crear una nueva audiencia.
            ---
            tags:
              - Audiencia
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    required:
                      - asunto_exp
                      - fecha
                      - abogado_pasaporte
                    properties:
                      asunto_exp:
                        type: string
                        example: "EXP-2025-001"
                      fecha:
                        type: string
                        format: date-time
                        example: "2025-05-10T10:30:00"
                      abogado_pasaporte:
                        type: string
                        example: "P123456789"
            responses:
              201:
                description: Audiencia creada exitosamente
              400:
                description: Datos inválidos o campos obligatorios faltantes
              404:
                description: Asunto o abogado no encontrado
            """
            return self.app_initializer.getAudienciaController(self.sede).create_audiencia(request.json)

        @self.app.route(f'{base_path}/<int:id>', methods=['PUT'], endpoint=f'update_audiencia_{self.sede}')
        def update_audiencia(id):
            """
            Actualizar una audiencia existente.
            ---
            tags:
              - Audiencia
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID de la audiencia a actualizar
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      fecha:
                        type: string
                        format: date-time
                        example: "2025-06-01T14:00:00"
                      abogado_pasaporte:
                        type: string
                        example: "P987654321"
            responses:
              200:
                description: Audiencia actualizada exitosamente
              400:
                description: Formato de fecha inválido o datos incorrectos
              404:
                description: Audiencia o abogado no encontrado
            """
            return self.app_initializer.getAudienciaController(self.sede).update_audiencia(id, request.json)
