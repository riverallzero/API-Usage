import openai

openai.api_key = 'openai_api_key'
model = 'gpt-3.5-turbo'

messages = [{'role': 'user', 'content': 'question_input'}]

response = openai.ChatCompletion.create(model=model, messages=messages)
answer = response['choices'][0]['message']['content']
print(answer)
