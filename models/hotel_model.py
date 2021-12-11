


class HotelModel:
    def __init__(self, hotel_id, nome, cidade, estrelas, diaria):
        self.hotel_id = hotel_id
        self.nome = nome
        self.cidade = cidade
        self.estrelas = estrelas
        self.diaria = diaria
    
    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'cidade': self.cidade,
            'estrelas': self.estrelas,
            'diaria': self.diaria
        }
