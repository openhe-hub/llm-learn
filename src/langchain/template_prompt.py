from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.prompts.chat import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model='gpt-4o')

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""
prompt_template = ChatPromptTemplate.from_template(template_string)


if __name__ == '__main__':	
    customer_style = """American English \
    in a calm and respectful tone
    """
    customer_email = """
    Arrr, I be fuming that me blender lid \
    flew off and splattered me kitchen walls \
    with smoothie! And to make matters worse, \
    the warranty don't cover the cost of \
    cleaning up me kitchen. I need yer help \
    right now, matey!
    """
    customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)
    customer_response = model.invoke(customer_messages).content
    print(customer_response)
