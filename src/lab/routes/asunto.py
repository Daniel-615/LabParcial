from flask import request
class Asunto:
    def __init__(self,app,app_initializer):
        self.app=app
        self.app_initializer=app_initializer
        self.routes()
    def routes(self):
        @self.app.route('/v1/asunto',methods=['GET'])
        def get_asunto():
            """
            Get all asunto
            """
            return self.app_initializer.getAsuntoControllers().get_asunto()
        @self.app.route('/v1/asunto/<string:expediente>',methods=['GET'])
        def get_asunto_by_id(expediente):
            """
            Get asunto by expediente
            """
            return self.app_initializer.getAsuntoControllers().get_asunto_by_id(expediente)
        @self.app.route('/v1/asunto',methods=['POST'])
        def create_asunto():
            """
            Create asunto
            """
            return self.app_initializer.getAsuntoControllers().create_asunto(request.json)
        @self.app.route('/v1/asunto/<string:expediente>',methods=['PUT'])
        def update_asunto(expediente):
            """
            Update asunto by expediente
            """
            return self.app_initializer.getAsuntoControllers().update_asunto(expediente,request.json)