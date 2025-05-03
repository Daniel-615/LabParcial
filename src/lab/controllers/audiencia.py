from flask import request, jsonify
from datetime import datetime

class Audiencia:
    def __init__(self, db, models):
        self.db = db
        self.models = models

    def get_all_audiencias(self):
        try:
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)
            audiencias= self.models.AUDIENCIA.query.order_by(self.models.AUDIENCIA.fecha).paginate(
                page=page, per_page=per_page, error_out=False
            )

            if not audiencias.items:
                return jsonify({'message': 'No hay audiencias registradas'}), 404

            return jsonify({
                'audiencias': [a.to_dict() for a in audiencias.items],
                'total': audiencias.total,
                'pagina_actual': audiencias.page,
                'total_paginas': audiencias.pages
            }), 200

        except Exception as e:
            print("Error en get_all_audiencias:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def get_audiencia_by_id(self, id):
        try:
            audiencia = self.models.AUDIENCIA.query.get(id)
            if not audiencia:
                return jsonify({'message': 'Audiencia no encontrada'}), 404

            return jsonify({'audiencia': audiencia.to_dict()}), 200

        except Exception as e:
            print("Error en get_audiencia_by_id:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def _validar_fecha(self, fecha_str):
        try:
            return datetime.fromisoformat(fecha_str.replace(" ", "T"))
        except (ValueError, TypeError):
            return None

    def create_audiencia(self, json_data):
        try:
            asunto_exp = json_data.get('asunto_exp')
            fecha_str = json_data.get('fecha')
            abogado_pasaporte = json_data.get('abogado_pasaporte')

            if not asunto_exp or not fecha_str or not abogado_pasaporte:
                return jsonify({'message': 'Campos obligatorios: asunto_exp, fecha, abogado_pasaporte'}), 400

            fecha = self._validar_fecha(fecha_str)
            if not fecha:
                return jsonify({'message': 'Formato de fecha inválido. Usa ISO 8601: YYYY-MM-DDTHH:MM:SS o YYYY-MM-DD HH:MM:SS'}), 400

            asunto = self.models.ASUNTO.query.filter_by(expediente=asunto_exp).first()
            abogado = self.models.ABOGADO.query.filter_by(pasaporte=abogado_pasaporte).first()

            if not asunto:
                return jsonify({'message': 'Asunto no encontrado'}), 404
            if not abogado:
                return jsonify({'message': 'Abogado no encontrado'}), 404

            nueva_audiencia = self.models.AUDIENCIA(
                asunto_exp=asunto_exp,
                fecha=fecha,
                abogado_pasaporte=abogado_pasaporte
            )

            self.db.session.add(nueva_audiencia)
            self.db.session.commit()

            return jsonify({'audiencia': nueva_audiencia.to_dict()}), 201

        except Exception as e:
            print("Error en create_audiencia:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def update_audiencia(self, id, json_data):
        try:
            audiencia = self.models.AUDIENCIA.query.get(id)
            if not audiencia:
                return jsonify({'message': 'Audiencia no encontrada'}), 404

            if 'fecha' in json_data:
                fecha = self._validar_fecha(json_data['fecha'])
                if not fecha:
                    return jsonify({'message': 'Formato de fecha inválido. Usa ISO 8601: YYYY-MM-DDTHH:MM:SS o YYYY-MM-DD HH:MM:SS'}), 400
                audiencia.fecha = fecha

            if 'abogado_pasaporte' in json_data:
                abogado = self.models.ABOGADO.query.filter_by(pasaporte=json_data['abogado_pasaporte']).first()
                if not abogado:
                    return jsonify({'message': 'Abogado no encontrado'}), 404
                audiencia.abogado_pasaporte = abogado.pasaporte

            self.db.session.commit() 

            return jsonify({'audiencia': audiencia.to_dict()}), 200

        except Exception as e:
            print("Error en update_audiencia:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500
