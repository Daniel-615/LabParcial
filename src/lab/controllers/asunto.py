from flask import request, jsonify

class Asunto:
    ESTADOS_VALIDOS = {
        "en trámite",
        "archivado",
        "finalizado",
        "en apelación",
        "amparo provisional",
        "amparo definitivo",
        "cerrado"
    }

    def __init__(self, db, models):
        self.db = db
        self.models = models

    def get_asunto(self):
        try:
            page = request.args.get('page', default=1, type=int)
            page_size = request.args.get('page_size', default=10, type=int)

            all_asuntos = self.models.ASUNTO.query.paginate(page=page, per_page=page_size, error_out=False)

            if not all_asuntos.items:
                return jsonify({'Error': 'No hay asuntos disponibles'}), 404

            return jsonify({
                'asuntos': [asunto.to_dict() for asunto in all_asuntos.items],
                'total': all_asuntos.total,
                'page': all_asuntos.page,
                'pages': all_asuntos.pages
            }), 200

        except Exception as e:
            print(f"Error en get_asunto: {e}")
            return jsonify({'Error': 'Error interno del servidor'}), 500

    def get_asunto_by_id(self, expediente):
        try:
            asunto = self.models.ASUNTO.query.filter_by(expediente=expediente).first()
            if not asunto:
                return jsonify({'Error': 'No se encontró el asunto'}), 404

            return jsonify({'asunto': asunto.to_dict()}), 200

        except Exception as e:
            print(f"Error en get_asunto_by_id: {e}")
            return jsonify({'Error': 'Error interno del servidor'}), 500

    def create_asunto(self, json_asunto):
        try:
            expediente = json_asunto.get('expediente')
            cliente_id = json_asunto.get('cliente_id')
            estado = json_asunto.get('estado')

            if not expediente or not cliente_id:
                return jsonify({'Error': "'expediente' y 'cliente_id' son requeridos"}), 400

            if estado:
                estado = estado.lower()
                if estado not in self.ESTADOS_VALIDOS:
                    return jsonify({
                        'Error': f"Estado inválido. Estados permitidos: {', '.join(sorted(self.ESTADOS_VALIDOS))}"
                    }), 400

            cliente = self.models.CLIENTE.query.filter_by(id=cliente_id).first()
            if not cliente:
                return jsonify({'Error': 'No se encontró el cliente'}), 404

            nuevo_asunto = self.models.ASUNTO(
                expediente=expediente,
                cliente_id=cliente_id,
                estado=estado
            )

            self.db.session.add(nuevo_asunto)
            self.db.session.commit()

            return jsonify({'asunto': nuevo_asunto.to_dict()}), 201

        except Exception as e:
            print(f"Error en create_asunto: {e}")
            return jsonify({'Error': 'Error interno del servidor'}), 500

    def update_asunto(self, expediente, json_asunto):
        try:
            asunto = self.models.ASUNTO.query.filter_by(expediente=expediente).first()
            if not asunto:
                return jsonify({'Error': 'No se encontró el asunto'}), 404

            estado = json_asunto.get('estado')
            if estado:
                estado = estado.lower()
                if estado not in self.ESTADOS_VALIDOS:
                    return jsonify({
                        'Error': f"Estado inválido. Estados permitidos: {', '.join(sorted(self.ESTADOS_VALIDOS))}"
                    }), 400
                asunto.estado = estado

            asunto.fecha_fin = json_asunto.get('fecha_fin')

            self.db.session.commit()

            return jsonify({'asunto': asunto.to_dict()}), 200

        except Exception as e:
            print(f"Error en update_asunto: {e}")
            return jsonify({'Error': 'Error interno del servidor'}), 500
