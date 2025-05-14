import speech_recognition as sr


def hablar(texto):
    """Función para que la aplicación hable (opcional)."""
    print(texto) # Siempre imprimir en consola
    # if TTS_ENGINE:
    #     try:
    #         TTS_ENGINE.say(texto)
    #         TTS_ENGINE.runAndWait()
    #     except Exception as e:
    #         print(f"Error al intentar hablar: {e}")


def mostrar_menu():
    """Muestra las opciones disponibles al usuario."""
    mensaje_menu = """
--- Centro de Salud León (Control por Voz) ---
Comandos disponibles:
  - 'registrar paciente' (o 'nuevo', 'agregar')
  - 'atender paciente' (o 'siguiente')
  - 'consultar próximo' (o 'ver siguiente', 'peek')
  - 'mostrar cola' (o 'ver cola')
  - 'salir' (o 'terminar')
------------------------------------------------
    """
    hablar(mensaje_menu.strip()) # strip() para quitar espacios extra al inicio/final

def obtener_comando_voz(prompt="Di un comando..."):
    """Escucha el micrófono y devuelve el texto reconocido."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        hablar(prompt)
        # print("(Ajustando sensibilidad al ruido...)") # Descomentar si hay mucho ruido
        # r.adjust_for_ambient_noise(source, duration=0.5)
        print("Escuchando...")
        try:
            # timeout: tiempo máximo esperando que comience el habla
            # phrase_time_limit: tiempo máximo para una frase
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Reconociendo...")
            texto_comando = r.recognize_google(audio, language='es-ES')
            print(f"Usuario dijo: {texto_comando}")
            return texto_comando.lower()
        except sr.WaitTimeoutError:
            hablar("No se detectó audio en el tiempo esperado. Intenta de nuevo.")
            return None
        except sr.UnknownValueError:
            hablar("No pude entender lo que dijiste. ¿Podrías repetirlo?")
            return None
        except sr.RequestError as e:
            hablar(f"No se pudo conectar con el servicio de reconocimiento de voz; {e}")
            return None
        except Exception as e:
             hablar(f"Ocurrió un error inesperado al procesar el audio: {e}")
             return None

def mostrar_mensaje(mensaje):
    """Muestra un mensaje general al usuario."""
    hablar(mensaje)

def mostrar_siguiente_paciente(paciente):
    """Informa al usuario quién es el siguiente paciente."""
    if paciente:
        hablar(f"El próximo paciente en la cola es: {paciente}")
    else:
        hablar("No hay pacientes esperando en la cola.")

def mostrar_paciente_atendido(paciente):
    """Informa al usuario qué paciente ha sido atendido."""
    if paciente:
        hablar(f"Atendiendo al paciente: {paciente}")
    else:
        hablar("La cola está vacía, no hay pacientes para atender.")

def mostrar_cola_actual(cola):
     """Muestra el estado actual de la cola de pacientes."""
     if not cola:
         hablar("La cola de pacientes está vacía.")
     else:
         hablar("Cola de pacientes actual (del primero al último):")
         # Para la voz, leer solo algunos o un resumen podría ser mejor si la cola es larga
         hablar(" -> ".join(cola))