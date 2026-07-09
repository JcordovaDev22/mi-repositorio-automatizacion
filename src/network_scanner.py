lass NetworkScanner:
    def __init__(self, red_base: str = "192.168.1."):
        self.red = red_base
        self.dispositivos_activos = []

    def escanear_ip(self, ultimo_octeto: int) -> dict:
        ip_completa = f"{self.red}{ultimo_octeto}"
        # Simulación de respuesta de ping
        if ultimo_octeto in [1, 10, 50]:
            self.dispositivos_activos.append(ip_completa)
            return {"ip": ip_completa, "estado": "Activo", "latencia": "15ms"}
        return {"ip": ip_completa, "estado": "Inactivo", "latencia": "0ms"}