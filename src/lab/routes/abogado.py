from flask import request
class Abogado:
    def __init__(self,app,app_initializer):
        self.app=app
        self.app_initializer=app_initializer
        self.routes()
    def routes(self):
        @self.app.route('/v1/abogado',methods=['GET'])
        def get_abogado():
            """
            Get all abogado
            """
            return self.app_initializer.getAbogadoControllers().get_abogado()
        @self.app.route('/v1/abogado/<int:id>',methods=['GET'])
        def get_abogado_by_id(id):
            """
            Get abogado by id
            """
            return self.app_initializer.getAbogadoControllers().get_abogado_by_id(id)
        @self.app.route('/v1/abogado',methods=['POST'])
        def create_abogado():
            """
            Create abogado
            """
            return self.app_initializer.getAbogadoControllers().create_abogado(request.json)
        @self.app.route('/v1/abogado/<int:id>',methods=['PUT'])
        def update_abogado(id):
            """
            Update abogado by id
            """
            return self.app_initializer.getAbogadoControllers().update_abogado(id,request.json)