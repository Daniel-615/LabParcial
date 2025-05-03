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
            """
            return self.app_initializer.getAsuntoController(self.sede).get_asunto()

        @self.app.route(f'{base_path}/<string:expediente>', methods=['GET'], endpoint=f'get_asunto_by_id_{self.sede}')
        def get_asunto_by_id(expediente):
            """
            Obtener asunto por expediente.
            """
            return self.app_initializer.getAsuntoController(self.sede).get_asunto_by_id(expediente)

        @self.app.route(f'{base_path}', methods=['POST'], endpoint=f'create_asunto_{self.sede}')
        def create_asunto():
            """
            Crear nuevo asunto.
            """
            return self.app_initializer.getAsuntoController(self.sede).create_asunto(request.json)

        @self.app.route(f'{base_path}/<string:expediente>', methods=['PUT'], endpoint=f'update_asunto_{self.sede}')
        def update_asunto(expediente):
            """
            Actualizar asunto por expediente.
            """
            return self.app_initializer.getAsuntoController(self.sede).update_asunto(expediente, request.json)
