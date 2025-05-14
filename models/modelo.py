class ColaPacientes:
    """
    Representa la cola de espera de pacientes y gestiona sus operaciones.
    Utiliza una lista de Python donde el final de la lista es el final de la cola
    y el principio de la lista (índice 0) es el frente de la cola.
    """
    def __init__(self):
        """Inicializa una cola de pacientes vacía."""
        self._pacientes = []

    def enqueue(self, paciente):
        """
        Agrega un nuevo paciente al final de la cola.

        Args:
            paciente (str): El nombre o identificador del paciente a agregar.
        """
        self._pacientes.append(paciente)
        # print(f"DEBUG (Modelo): Paciente '{paciente}' agregado. Cola actual: {self._pacientes}")

    def dequeue(self):
        """
        Elimina y devuelve el paciente al frente de la cola (el que llegó primero).

        Returns:
            str: El paciente que fue atendido.
            None: Si la cola está vacía.
        """
        if not self.is_empty():
            paciente_atendido = self._pacientes.pop(0)
            # print(f"DEBUG (Modelo): Paciente '{paciente_atendido}' eliminado. Cola actual: {self._pacientes}")
            return paciente_atendido
        else:
            # print("DEBUG (Modelo): Intento de dequeue en cola vacía.")
            return None

    def peek(self):
        """
        Devuelve el paciente al frente de la cola sin eliminarlo.

        Returns:
            str: El siguiente paciente a ser atendido.
            None: Si la cola está vacía.
        """
        if not self.is_empty():
            siguiente_paciente = self._pacientes[0]
            # print(f"DEBUG (Modelo): Peek realizado. Siguiente es '{siguiente_paciente}'. Cola: {self._pacientes}")
            return siguiente_paciente
        else:
            # print("DEBUG (Modelo): Intento de peek en cola vacía.")
            return None

    def is_empty(self):
        """
        Verifica si la cola de pacientes está vacía.

        Returns:
            bool: True si la cola está vacía, False en caso contrario.
        """
        return len(self._pacientes) == 0

    def obtener_cola_completa(self):
         """
         Devuelve una copia de la lista de pacientes actual (para visualización segura).
         """
         return self._pacientes[:] # Devuelve una copia