from openai import OpenAI

client = OpenAI(base_url = "http://chatapi.littlewheat.com/v1",
                api_key  = "sk-izKDCDcxAgEn1DXMbm0Yoc89Dn9MSTiikf7PgGQgGdaJXx4u")

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "user",
    "content": ""}
  ],
  temperature=0.7,
)
print(completion.choices[0].message.content)
