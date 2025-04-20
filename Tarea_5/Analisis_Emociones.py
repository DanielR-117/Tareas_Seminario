import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

# Descargar recursos necesarios de NLTK
nltk.download('vader_lexicon')
nltk.download('punkt')

# Palabras clave asociadas a ansiedad social
palabras_clave = {"nervioso", "evitar", "temor", "vergüenza", "tímido", "ansiedad", "inseguro", "preocupado", "juzgado", "observado"}

# Función para analizar indicios de ansiedad social
def detectar_ansiedad_social(frases):
    sia = SentimentIntensityAnalyzer()
    resultados = []

    for frase in frases:
        puntajes = sia.polarity_scores(frase)
        palabras_en_frase = set(frase.lower().split())
        coincidencias = palabras_clave.intersection(palabras_en_frase)
        
        indicador_ansiedad = len(coincidencias) > 0 or puntajes['neg'] > 0.4
        
        resultados.append({
            "frase": frase,
            "positivo": puntajes['pos'],
            "negativo": puntajes['neg'],
            "neutral": puntajes['neu'],
            "ansiedad_social": "Sí" if indicador_ansiedad else "No",
            "palabras_detectadas": list(coincidencias)
        })

    return resultados

# Ejemplo de uso
frases_prueba = [
    "Me siento muy nervioso cuando hablo en público.",
    "Evito reuniones sociales porque temo hacer el ridículo.",
    "Me encanta conversar con mis amigos sin problemas."
]

resultado = detectar_ansiedad_social(frases_prueba)
for r in resultado:
    print(r)
