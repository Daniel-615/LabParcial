from flask import request

class Incidencia:
    def __init__(self, app, app_initializer, sede):
        self.app = app
        self.app_initializer = app_initializer
        self.sede = sede
        self.routes()

    def routes(self):
        base_path = f'/v1/{self.sede}/incidencia'

        @self.app.route(f'{base_path}', methods=['GET'], endpoint=f'get_incidencias_{self.sede}')
        def get_incidencias():
            """
            Obtener todas las incidencias.
            ---
            tags:
              - Incidencia
            responses:
              200:
                description: Lista de incidencias obtenida correctamente.
              404:
                description: No se encontraron incidencias.
            """
            return self.app_initializer.getIncidenciaController(self.sede).get_incidencias()

        @self.app.route(f'{base_path}/<int:id>', methods=['GET'], endpoint=f'get_incidencia_by_id_{self.sede}')
        def get_incidencia_by_id(id):
            """
            Obtener incidencia por ID.
            ---
            tags:
              - Incidencia
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID de la incidencia a consultar
            responses:
              200:
                description: Incidencia encontrada.
              404:
                description: Incidencia no encontrada.
            """
            return self.app_initializer.getIncidenciaController(self.sede).get_incidencia_by_id(id)

        @self.app.route(f'{base_path}', methods=['POST'], endpoint=f'create_incidencia_{self.sede}')
        def create_incidencia():
            """
            Crear una nueva incidencia.
            ---
            tags:
              - Incidencia
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    required:
                      - audiencia_id
                      - descripcion
                    properties:
                      audiencia_id:
                        type: integer
                        example: 1
                      descripcion:
                        type: string
                        example: "Se presentó un retraso por ausencia del abogado"
            responses:
              201:
                description: Incidencia creada correctamente.
              400:
                description: Error de validación o datos faltantes.
            """
            return self.app_initializer.getIncidenciaController(self.sede).create_incidencia(request.json)

        @self.app.route(f'{base_path}/<int:id>', methods=['PUT'], endpoint=f'update_incidencia_{self.sede}')
        def update_incidencia(id):
            """
            Actualizar una incidencia por ID.
            ---
            tags:
              - Incidencia
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID de la incidencia a actualizar
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      descripcion:
                        type: string
                        example: "Modificación del motivo de la incidencia"
            responses:
              200:
                description: Incidencia actualizada correctamente.
              404:
                description: Incidencia no encontrada.
            """
            return self.app_initializer.getIncidenciaController(self.sede).update_incidencia(id, request.json)
