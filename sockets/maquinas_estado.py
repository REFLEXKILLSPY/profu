import speech_recognition as sr
import requests
import raylibpy as rl

# Estado inicial
state = 'dormido'
keyword = 'okay google'
timeout = 20
wait_time = 0

# Variable para almacenar lo que escucha el asistente
recognized_text = ""

modelo_carga = ""

# URL para obtener la hora
URL = 'https://timeapi.io/api/time/current/zone?timeZone=America%2FBogota'
response = requests.get(URL)

r = sr.Recognizer()
m = sr.Microphone()

app = Application()

# Código que escucha y reconoce el comando
with m as source:
    print('Ajustando ruido ambiente...')
    r.adjust_for_ambient_noise(source)

with m as source:
    print('Di algo...')
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language='es-ES')
    if text.lower().startswith("ok google"):
        recognized_text = text.lower().partition("ok google")[2].strip()

        if response.status_code == 200:
            data = response.json()

            if recognized_text == 'qué hora es':
                hora = f"La hora es {data['time']}"
                print(hora)
            elif recognized_text == 'qué fecha es':
                fecha = f"La fecha es {data['date']}"
                print(fecha)
            elif recognized_text == 'qué día es':
                dia = f"El día es {data['dayOfWeek']}"
                print(dia)

except sr.UnknownValueError:
    print('No se pudo entender el audio.')
except sr.RequestError as e:
    print(f'Error al solicitar resultados del servicio: {e}')

# Lógica de estados
match state:
    case 'dormido':
        if keyword == 'ok google':
            state = 'atento'
    case 'atento':
        if wait_time == timeout:
            state = 'dormido'
        elif recognized_text:
            print(f"Procesando comando: {recognized_text}")
            state = 'hablando'  
    case 'hablando':
        # Aquí se pueden realizar otras acciones basadas en el comando escuchado
        pass
    case _:
        pass

# Lógica del asistente
match state:
    case 'dormido':
        pass
    case 'atento':
        if wait_time == timeout:
            state = 'dormido'
    case 'hablando':
        pass
    case _:
        pass

def run():
    app.run(state)

t_run = threading.Thread(target=run)
