from flask import request
class AbogadoGabinete:
    def __init__(self,app,app_initializer):
        self.app=app
        self.app_initializer=app_initializer
        self.routes()
    def routes(self):
        @self.app.route('/v1/abogado/gabinete',methods=['GET'])
        def get_abogado_gabinete():
            """
            Get all abogado_gabinete
            """
            return self.app_initializer.getAbogadoGabineteControllers().get_abogado_gabinete()
        @self.app.route('/v1/abogado/gabinete/<int:id>',methods=['GET'])
        def get_abogado_gabinete_by_id(id):
            """
            Get abogado_gabinete by id
            """
            return self.app_initializer.getAbogadoGabineteControllers().get_abogado_gabinete_by_id(id)
        @self.app.route('/v1/abogado/gabinete',methods=['POST'])
        def create_abogado_gabinete():
            """
            Create abogado_gabinete
            """
            return self.app_initializer.getAbogadoGabineteControllers().create_abogado_gabinete(request.json)
        @self.app.route('/v1/abogado/gabinete/<int:id>',methods=['PUT'])
        def update_abogado_gabinete(id):
            """
            Update abogado_gabinete
            """
            return self.app_initializer.getAbogadoGabineteControllers().update_abogado_gabinete(id,request.json)