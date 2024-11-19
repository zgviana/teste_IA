import google.generativeai as genai

# api da google da minha conta
api_key_google = "AIzaSyAVRjHHZEj55pqSs0XPKlFhum_cNHDawLw"

genai.configure(api_key=api_key_google)

# Escolhendo o modelo do Gemini .
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Upload o arquivo
sample_file = genai.upload_file(path="manual_carro.pdf",
                                display_name="Gemini 1.5 PDF")

# Perguntando para o modelo sobre o arquivo carregado.
response = model.generate_content(
    [sample_file, "What car is this manual about?"])

print(response.text)
