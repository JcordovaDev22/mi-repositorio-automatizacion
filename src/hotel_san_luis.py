class GestionHotel:
    def __init__(self):
        self.habitaciones_disponibles = [101, 102, 103, 201, 202]
        self.ocupadas = {}

    def reservar_habitacion(self, cliente: str, habitacion: int) -> bool:
        if habitacion in self.habitaciones_disponibles:
            self.habitaciones_disponibles.remove(habitacion)
            self.ocupadas[habitacion] = cliente
            return True
        return False

    def liberar_habitacion(self, habitacion: int) -> bool:
        if habitacion in self.ocupadas:
            del self.ocupadas[habitacion]
            self.habitaciones_disponibles.append(habitacion)
            return True
        return False