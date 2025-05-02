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
        @self.app.route('/v1/asunto/<int:id>',methods=['GET'])
        def get_asunto_by_id(id):
            """
            Get asunto by id
            """
            return self.app_initializer.getAsuntoControllers().get_asunto_by_id(id)
        @self.app.route('/v1/asunto',methods=['POST'])
        def create_asunto():
            """
            Create asunto
            """
            return self.app_initializer.getAsuntoControllers().create_asunto(request.json)
        @self.app.route('/v1/asunto/<int:id>',methods=['PUT'])
        def update_asunto(id):
            """
            Update asunto by id
            """
            return self.app_initializer.getAsuntoControllers().update_asunto(id,request.json)