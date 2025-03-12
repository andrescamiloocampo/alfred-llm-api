from utils import dsConnection

response = dsConnection.client.chat.completions.create(
    model='deepseek/deepseek-r1:free',
    messages=[         
         {"role":"system","content":"Eres un profesor experto de ingles y solo respondes en ese idioma"},     
         {"role": "user", "content": "Dame una frase motivacional"},
    ],
    stream=False
)

print(response.choices[0].message.content)