class CloudPrinter:
    def __init__(self, tinto_nivel: int = 100):
        self.toner = tinto_nivel
        self.cola_impresion = []

    def enviar_documento(self, nombre_doc: str) -> str:
        if self.toner < 5:
            return "Error: Toner bajo"
        self.cola_impresion.append(nombre_doc)
        self.toner -= 5
        return f"Documento '{nombre_doc}' en cola"

    def procesar_cola(self) -> bool:
        if not self.cola_impresion:
            return False
        self.cola_impresion.pop(0)
        return True