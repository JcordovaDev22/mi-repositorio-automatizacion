class BovedaSegura:
    def __init__(self):
        self.bloqueado = True
        self.intentos = 0

    def ingresar_credenciales(self, clave: str) -> bool:
        if clave == "Admin123*":
            self.bloqueado = False
            self.intentos = 0
            return True
        self.intentos += 1
        if self.intentos >= 3:
            self.bloqueado = True
        return False

    def esta_bloqueado(self) -> bool:
        return self.bloqueado