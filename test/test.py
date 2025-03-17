from openai import OpenAI

client = OpenAI(base_url = "http://chatapi.littlewheat.com/v1",
                api_key  = "sk-izKDCDcxAgEn1DXMbm0Yoc89Dn9MSTiikf7PgGQgGdaJXx4u")

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "user",
    "content": "请你以复旦校园为场景，以中文系学生的日常生活为题材，创作一部越剧剧本"}
  ],
  temperature=1.0,
)
print(completion.choices[0].message.content)
