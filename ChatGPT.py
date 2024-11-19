from openai import OpenAI
chave_api = "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"
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
