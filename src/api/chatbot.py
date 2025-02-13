from openai import OpenAI

client = OpenAI(base_url = "http://chatapi.littlewheat.com/v1",
                api_key  = "sk-izKDCDcxAgEn1DXMbm0Yoc89Dn9MSTiikf7PgGQgGdaJXx4u")

def get_completion(prompt, model="gpt-4o", temperature=0.5):
    messages = [{
        "role": "user",
        "content": prompt
	}]
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
	)
    return completion.choices[0].message.content

def get_completion_from_messages(messages, model="gpt-4o", temperature=0.5):
    print(messages)
    completion = client.chat.completions.create(
        model = model,
        messages=messages,
        temperature=temperature,
	)
    return completion.choices[0].message.content



if __name__ == '__main__':
    context = [ {'role':'system', 'content':"""
        You are OrderBot, an automated service to collect orders for a pizza restaurant. \
        You first greet the customer, then collects the order, \
        and then asks if it's a pickup or delivery. \
        You wait to collect the entire order, then summarize it and check for a final \
        time if the customer wants to add anything else. \
        If it's a delivery, you ask for an address. \
        Finally you collect the payment.\
        Make sure to clarify all options, extras and sizes to uniquely \
        identify the item from the menu.\
        You respond in a short, very conversational friendly style. \
        The menu includes \
        pepperoni pizza  12.95, 10.00, 7.00 \
        cheese pizza   10.95, 9.25, 6.50 \
        eggplant pizza   11.95, 9.75, 6.75 \
        fries 4.50, 3.50 \
        greek salad 7.25 \
        Toppings: \
        extra cheese 2.00, \
        mushrooms 1.50 \
        sausage 3.00 \
        canadian bacon 3.50 \
        AI sauce 1.50 \
        peppers 1.00 \
        Drinks: \
        coke 3.00, 2.00, 1.00 \
        sprite 3.00, 2.00, 1.00 \
        bottled water 5.00 \
        """} ]  # accumulate messages
    while True:	
        prompt = input()
        context.append({
            'role': 'user',
            'content': f'{prompt}',
        })
        response = get_completion_from_messages(context)
        context.append({
            'role': 'assistant',
            'content': f"{response}",
        })
        print(response)
