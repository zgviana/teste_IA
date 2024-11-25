from openai import OpenAI
chave_api = "SUA CHAVE"
client = OpenAI(
    api_key=chave_api
)


def enviar_msg(msg):
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": msg}
        ],
    )
    return resposta["choices"][0]["message"]


print(enviar_msg("que dia é hoje?"))
