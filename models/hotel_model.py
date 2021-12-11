from sql_alchemy import banco


class HotelModel(banco.Model):
    nome = banco.Column(banco.String(80))
    __tablename__ = 'hoteis'

    hotel_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    cidade = banco.Column(banco.String(40))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))

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

    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        
        if hotel:
            return hotel
        return None

    @classmethod
    def find_hotel_by_cidade(cls, cidade):
        return cls.query.filter_by(cidade=cidade)
            

    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()
    
    def update_hotel(self, nome, cidade, estrelas, diaria):
        self.nome = nome
        self.cidade = cidade
        self.estrelas = estrelas
        self.diaria = diaria
