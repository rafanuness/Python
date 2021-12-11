from typing_extensions import Required
from flask_restful import  Resource, reqparse
from models.hotel_model import HotelModel

class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}


class HoteisCidade(Resource):
    def get(self, cidade):
        return {'hoteis': [hotel.json() for hotel in HotelModel.find_hotel_by_cidade(cidade)]}, 200

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="O campo 'nome' não pode ser deixado em branco.")
    argumentos.add_argument('cidade', type=str, required=True, help="O campo 'cidade' não pode ser deixado em branco.")
    argumentos.add_argument('estrelas', type=float, required=True, help="O campo 'estrelas' não pode ser deixado em branco.")
    argumentos.add_argument('diaria', type=float, required=True, help="O campo 'diaria' não pode ser deixado em branco.")
    

    

    def get(self, hotel_id):
        
        hotel = HotelModel.find_hotel(hotel_id)
        
        if hotel:
            return hotel.json()

        return {'message': 'Hotel não encontrado!'}, 404

    def post(self, hotel_id):
        
        if HotelModel.find_hotel(hotel_id):
            return {"message":"Hotel id '{}' já existe.".format(hotel_id)}, 400
       
        dados = Hotel.argumentos.parse_args()
        objHotel = HotelModel(hotel_id, **dados) 

        try:
             objHotel.save_hotel()
        except:
            return {'message' : 'Um erro interno ocorreu no servidor ao tentar salvar o hotel'}, 500

        return objHotel.json(), 200

    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        
        hotel_encontrado = HotelModel.find_hotel(hotel_id) 
        
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            try:
                hotel_encontrado.save_hotel()                
            except:
                return {'message' : 'Um erro interno ocorreu no servidor ao tentar salvar o hotel'}
            return hotel_encontrado.json(), 200

        novo_hotel = HotelModel(hotel_id, **dados)
        
        try:
             novo_hotel.save_hotel()        
        except:
            return {'message' : 'Um erro interno ocorreu no servidor ao tentar salvar o hotel'}
        
        return novo_hotel.json(), 201
        
        
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message' : 'Um erro interno ocorreu no servidor ao tentar deletar o hotel'}
            
            return {"message":"Hotel removido."}, 200
        
        return {"message":"Hotel não existe."}, 404
        

        

        
