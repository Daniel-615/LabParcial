from flask import request

class Cliente:
    def __init__(self, app, app_initializer):
        self.app = app
        self.app_initializer = app_initializer
        self.routes()

    def routes(self):
        @self.app.route('/v1/cliente', methods=['GET'])
        def get_clientes():
            """
            Get all clientes
            """
            return self.app_initializer.getClienteControllers().get_clientes()

        @self.app.route('/v1/cliente/<int:id>', methods=['GET'])
        def get_cliente_by_id(id):
            """
            Get cliente by ID
            """
            return self.app_initializer.getClienteControllers().get_cliente_by_id(id)

        @self.app.route('/v1/cliente', methods=['POST'])
        def create_cliente():
            """
            Create cliente
            """
            return self.app_initializer.getClienteControllers().create_cliente(request.json)

        @self.app.route('/v1/cliente/<int:id>', methods=['PUT'])
        def update_cliente(id):
            """
            Update cliente by ID
            """
            return self.app_initializer.getClienteControllers().update_cliente(id, request.json)