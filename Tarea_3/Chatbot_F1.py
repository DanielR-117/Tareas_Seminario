import requests

API_KEY = 'sk-53751d5c6f344a5dbc0571de9f51313e'
API_URL = 'https://api.deepseek.com/v1/chat/completions'

def send_mensaje(mensaje, modelo='deepseek-chat'):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': modelo,
        'messages': [{'role': 'user', 'content': f'Contesta únicamente preguntas relacionadas con la historia de la Fórmula 1. Si la pregunta no está relacionada, responde educadamente que solo puedes hablar de Fórmula 1. Pregunta: {mensaje}'}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as err:
        return f"Error de la API: {err}"
    except Exception as e:
        return f"Error inesperado: {e}"

def main():
    print("🏎️ Bienvenido al chatbot de historia de la Fórmula 1. Pregúntame sobre campeonatos, pilotos legendarios, escuderías y más.")
    print("Escribe 'salir' para terminar la conversación.")

    while True:
        user_mensaje = input("Tú: ")

        if user_mensaje.lower() == 'salir':
            print("Chatbot: ¡Gracias por hablar conmigo sobre la Fórmula 1! ¡Hasta la próxima!")
            break

        respuesta = send_mensaje(user_mensaje)
        print("Chatbot:", respuesta)

if __name__ == "__main__":
    main()
