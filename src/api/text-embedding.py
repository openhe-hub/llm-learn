import openai
from openai import OpenAI

client = OpenAI(base_url = "http://chatapi.littlewheat.com/v1",
                api_key  = "sk-izKDCDcxAgEn1DXMbm0Yoc89Dn9MSTiikf7PgGQgGdaJXx4u")

def get_embedding(text_to_embed):
	response = client.embeddings.create(
    	model= "text-embedding-3-small",
    	input=text_to_embed
	)
	embedding = response.data[0].embedding
    
	return embedding

print(get_embedding('hello world'))

