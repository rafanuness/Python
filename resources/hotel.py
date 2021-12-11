from flask_restful import  Resource, reqparse


hoteis= [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'cidade': 'Recife',
        'estrelas': '4.3',
        'diaria': 420.34
    },

    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'cidade': 'Olinda',
        'estrelas': '4.1',
        'diaria': 310.34
    },

    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'cidade': 'Petrolina',
        'estrelas': '4.9',
        'diaria': 820.34
    }
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

      
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        
        hotel = Hotel.find_hotel(hotel_id)
        
        if hotel:
            return hotel

        return {'message': 'Hotel não encontrado!'}, 404

    def post(self, hotel_id):
        
        dados = Hotel.argumentos.parse_args()

        novo_hotel = {
            'hotel_id': hotel_id,
            **dados
        }

        hoteis.append(novo_hotel)

        return novo_hotel, 200


    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()

        novo_hotel = {
            'hotel_id': hotel_id,
            **dados
        }

        hotel = Hotel.find_hotel(hotel_id)

        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
            

        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        pass
