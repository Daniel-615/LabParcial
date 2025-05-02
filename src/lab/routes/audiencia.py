from flask import request
class Audiencia:
    def __init__(self,app,app_initializer):
        self.app=app
        self.app_initializer=app_initializer
        self.routes()
    def routes(self):
        @self.app.route('/v1/audiencia',methods=['GET'])
        def get_audiencia():
            """
            Get all audiencia
            """
            return self.app_initializer.getAudienciaControllers().get_audiencia()
        @self.app.route('/v1/audiencia/<int:id>',methods=['GET'])
        def get_audiencia_by_id(id):
            """
            Get audiencia by id
            """
            return self.app_initializer.getAudienciaControllers().get_audiencia_by_id(id)
        @self.app.route('/v1/audiencia',methods=['POST'])
        def create_audiencia():
            """
            Create audiencia
            """
            return self.app_initializer.getAudienciaControllers().create_audiencia(request.json)
        @self.app.route('/v1/audiencia/<int:id>',methods=['PUT'])
        def update_audiencia(id):
            """
            Update audiencia by id
            """
            return self.app_initializer.getAudienciaControllers().update_audiencia(id,request.json)