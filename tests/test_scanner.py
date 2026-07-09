from src.network_scanner import NetworkScanner

def test_escanear_ip_activa():
    scanner = NetworkScanner()
    resultado = scanner.escanear_ip(10)
    assert resultado["estado"] == "Activo"
    assert "192.168.1.10" in scanner.dispositivos_activos

def test_escanear_ip_inactiva():
    scanner = NetworkScanner()
    resultado = scanner.escanear_ip(99)
    assert resultado["estado"] == "Inactivo"