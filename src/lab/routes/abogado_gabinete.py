from flask import request

class AbogadoGabinete:
    def __init__(self, app, app_initializer, sede):
        self.app = app
        self.app_initializer = app_initializer
        self.sede = sede
        self.routes()

    def routes(self):
        base_path = f'/v1/{self.sede}/abogado/gabinete'

        @self.app.route(f'{base_path}', methods=['GET'], endpoint=f'get_abogado_gabinete_{self.sede}')
        def get_abogado_gabinete():
            """
            Obtener todas las asociaciones abogado-gabinete.
            ---
            tags:
              - Abogado-Gabinete
            responses:
              200:
                description: Lista de asociaciones obtenida correctamente
              500:
                description: Error interno del servidor
            """
            return self.app_initializer.getAbogadoGabineteController(self.sede).get_abogado_gabinete()

        @self.app.route(f'{base_path}/<int:id>', methods=['GET'], endpoint=f'get_abogado_gabinete_by_id_{self.sede}')
        def get_abogado_gabinete_by_id(id):
            """
            Obtener asociaciones por ID de gabinete.
            ---
            tags:
              - Abogado-Gabinete
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID del gabinete
            responses:
              200:
                description: Asociación encontrada
              404:
                description: Asociación no encontrada
            """
            return self.app_initializer.getAbogadoGabineteController(self.sede).get_abogado_gabinete_by_id(id)

        @self.app.route(f'{base_path}', methods=['POST'], endpoint=f'create_abogado_gabinete_{self.sede}')
        def create_abogado_gabinete():
            """
            Crear una nueva asociación abogado-gabinete.
            ---
            tags:
              - Abogado-Gabinete
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      pasaporte:
                        type: string
                      gabinete_id:
                        type: integer
            responses:
              201:
                description: Asociación creada exitosamente
              400:
                description: Datos inválidos
            """
            return self.app_initializer.getAbogadoGabineteController(self.sede).create_abogado_gabinete(request.json)

        @self.app.route(f'{base_path}/<int:id>', methods=['PUT'], endpoint=f'update_abogado_gabinete_{self.sede}')
        def update_abogado_gabinete(id):
            """
            Actualizar la asociación abogado-gabinete por ID de gabinete.
            ---
            tags:
              - Abogado-Gabinete
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID del gabinete
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      pasaporte:
                        type: string
            responses:
              200:
                description: Asociación actualizada
              404:
                description: Asociación no encontrada
            """
            return self.app_initializer.getAbogadoGabineteController(self.sede).update_abogado_gabinete(id, request.json)
