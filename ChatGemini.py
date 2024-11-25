import google.generativeai as genai
from google.generativeai import models

# api da google da minha conta
api_key_google = "SUA CHAVE"

genai.configure(api_key=api_key_google)

modelo = genai.GenerativeModel("gemini-pro")
resposta = modelo.generate_content(
    "cria pra mim uma API em python que me retorne um 'olá mundo'?")

print(resposta.text)
