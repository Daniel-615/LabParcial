from flask import request

class Cliente:
    def __init__(self, app, app_initializer, sede):
        self.app = app
        self.app_initializer = app_initializer
        self.sede = sede
        self.routes()

    def routes(self):
        base_path = f'/v1/{self.sede}/cliente'

        @self.app.route(f'{base_path}', methods=['GET'], endpoint=f'get_clientes_{self.sede}')
        def get_clientes():
            """
            Obtener todos los clientes.
            ---
            tags:
              - Cliente
            parameters:
              - name: page
                in: query
                type: integer
                description: Página actual
              - name: per_page
                in: query
                type: integer
                description: Cantidad por página
            responses:
              200:
                description: Lista de clientes
              404:
                description: No hay clientes registrados
            """
            return self.app_initializer.getClienteController(self.sede).get_clientes()

        @self.app.route(f'{base_path}/<int:id>', methods=['GET'], endpoint=f'get_cliente_by_id_{self.sede}')
        def get_cliente_by_id(id):
            """
            Obtener cliente por ID.
            ---
            tags:
              - Cliente
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID del cliente
            responses:
              200:
                description: Cliente encontrado
              404:
                description: Cliente no encontrado
            """
            return self.app_initializer.getClienteController(self.sede).get_cliente_by_id(id)

        @self.app.route(f'{base_path}', methods=['POST'], endpoint=f'create_cliente_{self.sede}')
        def create_cliente():
            """
            Crear un nuevo cliente.
            ---
            tags:
              - Cliente
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    required:
                      - nombre
                      - direccion
                      - telefono
                      - email
                    properties:
                      nombre:
                        type: string
                        example: "Carlos Pérez"
                      direccion:
                        type: string
                        example: "Av. Reforma #123"
                      telefono:
                        type: string
                        example: "5555-5555"
                      email:
                        type: string
                        example: "carlos@example.com"
            responses:
              201:
                description: Cliente creado exitosamente
              400:
                description: Campos obligatorios faltantes
            """
            return self.app_initializer.getClienteController(self.sede).create_cliente(request.json)

        @self.app.route(f'{base_path}/<int:id>', methods=['PUT'], endpoint=f'update_cliente_{self.sede}')
        def update_cliente(id):
            """
            Actualizar un cliente existente.
            ---
            tags:
              - Cliente
            parameters:
              - name: id
                in: path
                required: true
                type: integer
                description: ID del cliente
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      nombre:
                        type: string
                        example: "Carlos Pérez"
                      direccion:
                        type: string
                        example: "Av. Reforma #123"
                      telefono:
                        type: string
                        example: "5555-5555"
                      email:
                        type: string
                        example: "carlos@example.com"
            responses:
              200:
                description: Cliente actualizado exitosamente
              404:
                description: Cliente no encontrado
            """
            return self.app_initializer.getClienteController(self.sede).update_cliente(id, request.json)
