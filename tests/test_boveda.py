from src.boveda import BovedaSegura

def test_acceso_correcto_boveda():
    boveda = BovedaSegura()
    assert boveda.ingresar_credenciales("Admin123*") is True
    assert boveda.esta_bloqueado() is False

def test_bloqueo_por_intentos():
    boveda = BovedaSegura()
    boveda.ingresar_credenciales("clave_erronea_1")
    boveda.ingresar_credenciales("clave_erronea_2")
    boveda.ingresar_credenciales("clave_erronea_3")
    assert boveda.esta_bloqueado() is True