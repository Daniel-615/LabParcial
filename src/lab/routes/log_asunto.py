from flask import request

class LogAsunto:
    def __init__(self, app, app_initializer):
        self.app = app
        self.app_initializer = app_initializer
        self.routes()

    def routes(self):
        @self.app.route('/v1/log_asunto', methods=['GET'])
        def get_logs():
            """
            Get all log_asunto records
            """
            return self.app_initializer.getLogAsuntoController().get_logs()

        @self.app.route('/v1/log_asunto/<int:id>', methods=['GET'])
        def get_log_by_id(id):
            """
            Get log_asunto by ID
            """
            return self.app_initializer.getLogAsuntoController().get_log_by_id(id)

        @self.app.route('/v1/log_asunto', methods=['POST'])
        def create_log():
            """
            Create log_asunto
            """
            return self.app_initializer.getLogAsuntoController().create_log(request.json)

        @self.app.route('/v1/log_asunto/<int:id>', methods=['PUT'])
        def update_log(id):
            """
            Update log_asunto by ID
            """
            return self.app_initializer.getLogAsuntoController().update_log(id, request.json)