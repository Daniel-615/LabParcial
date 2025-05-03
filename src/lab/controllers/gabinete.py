from flask import jsonify, request

class Gabinete:
    def __init__(self, db, models):
        self.db = db
        self.models = models

    def get_gabinetes(self):
        try:
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            gabinetes = self.models.GABINETE.query.order_by(self.models.GABINETE.nombre).paginate(
                page=page, per_page=per_page, error_out=False)

            if not gabinetes.items:
                return jsonify({'message': 'No hay gabinetes registrados'}), 404

            return jsonify({
                'gabinetes': [gabinete.to_dict() for gabinete in gabinetes.items],
                'total': gabinetes.total,
                'pagina_actual': gabinetes.page,
                'total_paginas': gabinetes.pages
            }), 200

        except Exception as e:
            print("Error en get_gabinetes:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def get_gabinete_by_id(self, id):
        try:
            gabinete = self.models.GABINETE.query.filter_by(id=id).first()

            if not gabinete:
                return jsonify({'message': 'Gabinete no encontrado'}), 404

            return jsonify(gabinete.to_dict()), 200

        except Exception as e:
            print("Error en get_gabinete_by_id:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def create_gabinete(self, json_data):
        try:
            nombre = json_data.get('nombre')
            pais = json_data.get('pais')
            sistema_operativo = json_data.get('sistema_operativo')

            if not nombre or not pais or not sistema_operativo:
                return jsonify({'message': "'nombre', 'pais' y 'sistema_operativo' son requeridos"}), 400

            nuevo_gabinete = self.models.GABINETE(
                nombre=nombre,
                pais=pais,
                sistema_operativo=sistema_operativo
            )
            self.db.session.add(nuevo_gabinete)
            self.db.session.commit()

            return jsonify({
                'message': 'Gabinete creado',
                'gabinete': nuevo_gabinete.to_dict()
            }), 201

        except Exception as e:
            print("Error en create_gabinete:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500

    def update_gabinete(self, id, json_data):
        try:
            gabinete = self.models.GABINETE.query.filter_by(id=id).first()

            if not gabinete:
                return jsonify({'message': 'Gabinete no encontrado'}), 404

            nombre = json_data.get('nombre')
            pais = json_data.get('pais')

            if nombre:
                gabinete.nombre = nombre
            if pais:
                gabinete.pais = pais

            self.db.session.commit()

            return jsonify({
                'message': 'Gabinete actualizado',
                'gabinete': gabinete.to_dict()
            }), 200

        except Exception as e:
            print("Error en update_gabinete:", e)
            return jsonify({'message': 'Error interno del servidor'}), 500