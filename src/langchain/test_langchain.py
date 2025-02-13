from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model='gpt-4o')

messages = [
    SystemMessage(content="translate the following sentences to Chinese"),
    HumanMessage(content="what's the weather today?")
]

print(model.invoke(messages).content)