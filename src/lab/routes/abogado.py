from flask import request

class Abogado:
    def __init__(self, app, app_initializer, sede):
        self.app = app
        self.app_initializer = app_initializer
        self.sede = sede
        self.routes()

    def routes(self):
        base_path = f'/v1/{self.sede}/abogado'

        @self.app.route(f'{base_path}', methods=['GET'], endpoint=f'get_abogado_{self.sede}')
        def get_abogado():
            """
            Obtener todos los abogados.
            """
            return self.app_initializer.getAbogadoController(self.sede).get_abogado()

        @self.app.route(f'{base_path}/<string:pasaporte>', methods=['GET'], endpoint=f'get_abogado_by_id_{self.sede}')
        def get_abogado_by_id(pasaporte):
            """
            Obtener abogado por pasaporte.
            """
            return self.app_initializer.getAbogadoController(self.sede).get_abogado_by_id(pasaporte)

        @self.app.route(f'{base_path}', methods=['POST'], endpoint=f'create_abogado_{self.sede}')
        def create_abogado():
            """
            Crear nuevo abogado.
            """
            return self.app_initializer.getAbogadoController(self.sede).create_abogado(request.json)

        @self.app.route(f'{base_path}/<string:pasaporte>', methods=['PUT'], endpoint=f'update_abogado_{self.sede}')
        def update_abogado(pasaporte):
            """
            Actualizar abogado por pasaporte.
            """
            return self.app_initializer.getAbogadoController(self.sede).update_abogado(pasaporte, request.json)
