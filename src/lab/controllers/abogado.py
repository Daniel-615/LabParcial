from flask import request, jsonify
class Abogado:
    def __init__(self,db,models):
        self.db=db
        self.models=models
    def get_abogado(self):
        try:
            page=request.args.get('page',default=1,type=int)
            per_page=request.args.get('per_page',default=10,type=int)
            all_abogado=self.models.ABOGADO.query.paginate(page=page,per_page=per_page,error_out=False)
            if not all_abogado.items:
                return {'message':'No hay abogados registrados'},404
            else:
                return jsonify({
                    "abogados": [abogado.to_dict() for abogado in all_abogado.items],
                    "total": all_abogado.total,
                    "pagina_actual": all_abogado.page,
                    "total_paginas": all_abogado.pages,
                }),200
        except Exception as e:
            print("Error en get_abogado:", e)
            return {'message':'Error interno del servidor'},500
    def get_abogado_by_id(self,pasaporte):
        try:
            abogado=self.models.ABOGADO.query.filter_by(pasaporte=pasaporte).first()
            if not abogado:
                return {'message':'Abogado no encontrado'},404
            else:
                return jsonify(
                    abogado.to_dict()
                ),200
        except Exception as e:
            print("Error en get_abogado_by_id:", e)
            return {'message':'Error interno del servidor'},500
    def create_abogado(self,json_abogado):
        try:
            if not json_abogado.get('pasaporte') or not json_abogado.get('nombre'):
                return {'message':'Faltan datos obligatorios'},400
            abogado=self.models.ABOGADO(
                pasaporte=json_abogado['pasaporte'],
                nombre=json_abogado['nombre']
            )
            self.db.session.add(abogado)
            self.db.session.commit()
            return jsonify({
                "message":"Abogado creado correctamente"
            }),201
        except Exception as e:
            print("Error en create_abogado:", e)
            return {'message':'Error interno del servidor'},500
    def update_abogado(self,pasaporte,json_abogado):
        try:
            abogado=self.models.ABOGADO.query.filter_by(pasaporte=pasaporte).first()
            if not abogado:
                return {'message':'Abogado no encontrado'},404
            if json_abogado.get('nombre'):
                abogado.nombre=json_abogado['nombre']
            self.db.session.commit()
            return jsonify({
                "message":"Abogado actualizado correctamente"
            }),200
        except Exception as e:
            print("Error en update_abogado:", e)
            return {'message':'Error interno del servidor'},500