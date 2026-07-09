from src.cloud_printer import CloudPrinter

def test_enviar_documento_exitoso():
    printer = CloudPrinter()
    resultado = printer.enviar_documento("reporte.pdf")
    assert "en cola" in resultado
    assert printer.toner == 95

def test_procesar_cola_vacia():
    printer = CloudPrinter()
    assert printer.procesar_cola() is False