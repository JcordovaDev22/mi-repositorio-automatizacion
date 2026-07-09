from src.hotel_san_luis import GestionHotel

def test_reserva_exitosa():
    hotel = GestionHotel()
    assert hotel.reservar_habitacion("Juan Perez", 101) is True
    assert 101 not in hotel.habitaciones_disponibles

def test_reserva_duplicada():
    hotel = GestionHotel()
    hotel.reservar_habitacion("Juan Perez", 102)
    assert hotel.reservar_habitacion("Maria Lopez", 102) is False