from flask import request

class Gabinete:
    def __init__(self, app, app_initializer):
        self.app = app
        self.app_initializer = app_initializer
        self.routes()

    def routes(self):
        @self.app.route('/v1/gabinete', methods=['GET'])
        def get_gabinetes():
            """
            Get all gabinetes
            """
            return self.app_initializer.getGabineteControllers().get_gabinetes()

        @self.app.route('/v1/gabinete/<int:id>', methods=['GET'])
        def get_gabinete_by_id(id):
            """
            Get gabinete by ID
            """
            return self.app_initializer.getGabineteControllers().get_gabinete_by_id(id)

        @self.app.route('/v1/gabinete', methods=['POST'])
        def create_gabinete():
            """
            Create gabinete
            """
            return self.app_initializer.getGabineteControllers().create_gabinete(request.json)

        @self.app.route('/v1/gabinete/<int:id>', methods=['PUT'])
        def update_gabinete(id):
            """
            Update gabinete by ID
            """
            return self.app_initializer.getGabineteControllers().update_gabinete(id, request.json)