from flask import request

class Gabinete:
    def __init__(self, app, app_initializer, sede):
        self.app = app
        self.app_initializer = app_initializer
        self.sede = sede
        self.routes()

    def routes(self):
        base_path = f'/v1/{self.sede}/gabinete'

        @self.app.route(f'{base_path}', methods=['GET'], endpoint=f'get_gabinetes_{self.sede}')
        def get_gabinetes():
            """
            Obtener todos los gabinetes.
            ---
            tags:
              - Gabinete
            responses:
              200:
                description: Lista de gabinetes obtenida correctamente.
              404:
                description: No se encontraron gabinetes.
            """
            return self.app_initializer.getGabineteController(self.sede).get_gabinetes()

        @self.app.route(f'{base_path}/<int:id>', methods=['GET'], endpoint=f'get_gabinete_by_id_{self.sede}')
        def get_gabinete_by_id(id):
            """
            Obtener gabinete por ID.
            ---
            tags:
              - Gabinete
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID del gabinete a consultar
            responses:
              200:
                description: Gabinete encontrado.
              404:
                description: Gabinete no encontrado.
            """
            return self.app_initializer.getGabineteController(self.sede).get_gabinete_by_id(id)

        @self.app.route(f'{base_path}', methods=['POST'], endpoint=f'create_gabinete_{self.sede}')
        def create_gabinete():
            """
            Crear un nuevo gabinete.
            ---
            tags:
              - Gabinete
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    required:
                      - nombre
                    properties:
                      nombre:
                        type: string
                        example: "Gabinete Central"
                      pais:
                        type: string
                        example: "Guatemala"
                      sistema_operativo:
                        type: string
                        example: "Windows"
            responses:
              201:
                description: Gabinete creado exitosamente.
              400:
                description: Error de validación o campos faltantes.
            """
            return self.app_initializer.getGabineteController(self.sede).create_gabinete(request.json)

        @self.app.route(f'{base_path}/<int:id>', methods=['PUT'], endpoint=f'update_gabinete_{self.sede}')
        def update_gabinete(id):
            """
            Actualizar gabinete por ID.
            ---
            tags:
              - Gabinete
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID del gabinete a actualizar
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      nombre:
                        type: string
                        example: "Gabinete Legal México"
                      pais:
                        type: string
                        example: "México"
                      sistema_operativo:
                        type: string
                        example: "Linux"
            responses:
              200:
                description: Gabinete actualizado exitosamente.
              404:
                description: Gabinete no encontrado.
            """
            return self.app_initializer.getGabineteController(self.sede).update_gabinete(id, request.json)
