from flask import request

class Incidencia:
    def __init__(self, app, app_initializer):
        self.app = app
        self.app_initializer = app_initializer
        self.routes()

    def routes(self):
        @self.app.route('/v1/incidencia', methods=['GET'])
        def get_incidencias():
            """
            Get all incidencias
            """
            return self.app_initializer.getIncidenciaControllers().get_incidencias()

        @self.app.route('/v1/incidencia/<int:id>', methods=['GET'])
        def get_incidencia_by_id(id):
            """
            Get incidencia by ID
            """
            return self.app_initializer.getIncidenciaControllers().get_incidencia_by_id(id)

        @self.app.route('/v1/incidencia', methods=['POST'])
        def create_incidencia():
            """
            Create incidencia
            """
            return self.app_initializer.getIncidenciaControllers().create_incidencia(request.json)

        @self.app.route('/v1/incidencia/<int:id>', methods=['PUT'])
        def update_incidencia(id):
            """
            Update incidencia by ID
            """
            return self.app_initializer.getIncidenciaControllers().update_incidencia(id, request.json)