from flask import Flask, request, render_template
from generador_docs import generar_docx, generar_excel
from supabase_config import guardar_interaccion
from consulta_openai import consulta_chatgpt  # Asegúrate de tener este archivo y función

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    respuesta = None
    if request.method == "POST":
        pregunta = request.form["pregunta"]

        # Obtener respuesta de ChatGPT
        respuesta = consulta_chatgpt(pregunta)

        # Guardar interacción en la base de datos (Supabase)
        guardar_interaccion(pregunta, respuesta)

        # Crear documentos si el usuario lo solicita (opcional)
        if "excel" in pregunta.lower():
            generar_excel("respuesta.xlsx", ["Pregunta", "Respuesta"], [[pregunta, respuesta]])
        elif "word" in pregunta.lower() or "documento" in pregunta.lower():
            generar_docx("respuesta.docx", respuesta)

    return render_template("index.html", respuesta=respuesta)

if __name__ == "__main__":
    app.run(debug=True)

