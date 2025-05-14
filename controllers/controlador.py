from models.modelo import ColaPacientes
from views import vista

class Controlador:
    def __init__(self):
        self._modelo = ColaPacientes()

    def iniciar(self):
        """Inicia el bucle principal de la aplicación."""
        vista.mostrar_mensaje("Bienvenido al sistema de atención por voz del Centro de Salud León.")

        while True:
            vista.mostrar_menu()
            comando = vista.obtener_comando_voz("Esperando comando principal...")

            if not comando:
                continue # Vuelve al inicio del bucle si no se reconoció comando

            # Interpretar comandos de voz
            if any(k in comando for k in ["registrar", "nuevo", "agregar"]):
                nombre = vista.obtener_comando_voz("Por favor, diga el nombre completo del paciente:")
                if nombre:
                    self._modelo.enqueue(nombre)
                    vista.mostrar_mensaje(f"Paciente '{nombre}' agregado correctamente a la cola.")
                else:
                    vista.mostrar_mensaje("No se pudo reconocer el nombre del paciente. Intente registrar de nuevo.")

            elif any(k in comando for k in ["atender", "siguiente"]):
                if self._modelo.is_empty():
                    vista.mostrar_mensaje("La cola está vacía, no hay pacientes para atender.")
                else:
                    paciente_atendido = self._modelo.dequeue()
                    vista.mostrar_paciente_atendido(paciente_atendido)


            elif any(k in comando for k in ["consultar", "próximo", "ver siguiente", "peek"]):
                if self._modelo.is_empty():
                    vista.mostrar_mensaje("La cola está vacía, no hay próximo paciente.")
                else:
                    siguiente = self._modelo.peek()
                    vista.mostrar_siguiente_paciente(siguiente)


            elif any(k in comando for k in ["mostrar cola", "ver cola", "estado cola"]):
                 cola_actual = self._modelo.obtener_cola_completa()
                 vista.mostrar_cola_actual(cola_actual)

            elif any(k in comando for k in ["salir", "terminar", "adiós"]):
                vista.mostrar_mensaje("Saliendo del sistema. ¡Hasta pronto!")
                break
            else:
                vista.mostrar_mensaje(f"Comando '{comando}' no reconocido. Por favor, intente de nuevo con uno de los comandos disponibles.")