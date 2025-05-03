from flask import request, jsonify
from datetime import datetime

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

    def __init__(self, db, models, sede):
        self.db = db
        self.models = models
        self.sede = sede

    def _get_model(self):
        try:
            return self.models.ASUNTO[self.sede], self.models.CLIENTE[self.sede]
        except KeyError:
            return None, None

    def get_asunto(self):
        try:
            AsuntoModel, _ = self._get_model()
            if not AsuntoModel:
                return jsonify({'message': 'Sede inválida'}), 400

            page = request.args.get('page', default=1, type=int)
            page_size = request.args.get('page_size', default=10, type=int)

            asuntos = AsuntoModel.query.order_by(AsuntoModel.fecha_inicio).paginate(
                page=page, per_page=page_size, error_out=False
            )

            if not asuntos.items:
                return jsonify({'message': 'No hay asuntos disponibles'}), 404

            return jsonify({
                'asuntos': [a.to_dict() for a in asuntos.items],
                'total': asuntos.total,
                'page': asuntos.page,
                'pages': asuntos.pages
            }), 200

        except Exception as e:
            print(f"Error en get_asunto: {e}")
            return jsonify({'message': 'Error interno del servidor'}), 500

    def get_asunto_by_id(self, expediente):
        try:
            AsuntoModel, _ = self._get_model()
            if not AsuntoModel:
                return jsonify({'message': 'Sede inválida'}), 400

            asunto = AsuntoModel.query.filter_by(expediente=expediente).first()
            if not asunto:
                return jsonify({'message': 'Asunto no encontrado'}), 404

            return jsonify({'asunto': asunto.to_dict()}), 200

        except Exception as e:
            print(f"Error en get_asunto_by_id: {e}")
            return jsonify({'message': 'Error interno del servidor'}), 500

    def create_asunto(self, json_data):
        try:
            AsuntoModel, ClienteModel = self._get_model()
            if not AsuntoModel or not ClienteModel:
                return jsonify({'message': 'Sede inválida'}), 400

            expediente = json_data.get('expediente')
            cliente_id = json_data.get('cliente_id')
            estado = json_data.get('estado')

            if not expediente or not cliente_id:
                return jsonify({'message': "'expediente' y 'cliente_id' son obligatorios"}), 400

            if estado:
                estado = estado.casefold()
                if estado not in {e.casefold() for e in self.ESTADOS_VALIDOS}:
                    return jsonify({
                        'message': f"Estado inválido. Permitidos: {', '.join(sorted(self.ESTADOS_VALIDOS))}"
                    }), 400

            cliente = ClienteModel.query.filter_by(id=cliente_id).first()
            if not cliente:
                return jsonify({'message': 'Cliente no encontrado'}), 404

            nuevo_asunto = AsuntoModel(
                expediente=expediente,
                cliente_id=cliente_id,
                estado=estado
            )

            self.db.session.add(nuevo_asunto)
            self.db.session.commit()

            return jsonify({
                'message': 'Asunto creado correctamente',
                'asunto': nuevo_asunto.to_dict()
            }), 201

        except Exception as e:
            print(f"Error en create_asunto: {e}")
            return jsonify({'message': 'Error interno del servidor'}), 500

    def update_asunto(self, expediente, json_data):
        try:
            AsuntoModel, _ = self._get_model()
            if not AsuntoModel:
                return jsonify({'message': 'Sede inválida'}), 400

            asunto = AsuntoModel.query.filter_by(expediente=expediente).first()
            if not asunto:
                return jsonify({'message': 'Asunto no encontrado'}), 404

            estado = json_data.get('estado')
            if estado:
                estado = estado.casefold()
                if estado not in {e.casefold() for e in self.ESTADOS_VALIDOS}:
                    return jsonify({
                        'message': f"Estado inválido. Permitidos: {', '.join(sorted(self.ESTADOS_VALIDOS))}"
                    }), 400
                asunto.estado = estado

            fecha_fin = json_data.get('fecha_fin')
            if fecha_fin:
                try:
                    asunto.fecha_fin = datetime.fromisoformat(fecha_fin)
                except ValueError:
                    return jsonify({'message': 'Fecha inválida. Usa formato ISO 8601 (YYYY-MM-DD)'}), 400

            self.db.session.commit()

            return jsonify({
                'message': 'Asunto actualizado correctamente',
                'asunto': asunto.to_dict()
            }), 200

        except Exception as e:
            print(f"Error en update_asunto: {e}")
            return jsonify({'message': 'Error interno del servidor'}), 500
