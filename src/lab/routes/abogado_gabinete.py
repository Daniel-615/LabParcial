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
            """
            return self.app_initializer.getAbogadoGabineteController(self.sede).get_abogado_gabinete()

        @self.app.route(f'{base_path}/<int:id>', methods=['GET'], endpoint=f'get_abogado_gabinete_by_id_{self.sede}')
        def get_abogado_gabinete_by_id(id):
            """
            Obtener asociaciones por ID de gabinete.
            """
            return self.app_initializer.getAbogadoGabineteController(self.sede).get_abogado_gabinete_by_id(id)

        @self.app.route(f'{base_path}', methods=['POST'], endpoint=f'create_abogado_gabinete_{self.sede}')
        def create_abogado_gabinete():
            """
            Crear una nueva asociación abogado-gabinete.
            """
            return self.app_initializer.getAbogadoGabineteController(self.sede).create_abogado_gabinete(request.json)

        @self.app.route(f'{base_path}/<int:id>', methods=['PUT'], endpoint=f'update_abogado_gabinete_{self.sede}')
        def update_abogado_gabinete(id):
            """
            Actualizar la asociación abogado-gabinete por ID de gabinete.
            """
            return self.app_initializer.getAbogadoGabineteController(self.sede).update_abogado_gabinete(id, request.json)
