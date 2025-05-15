# main.py
__version__ = "0.0.1"

from controllers.controlador import Controlador

if __name__ == "__main__":
    controlador_app = Controlador()
    controlador_app.iniciar()