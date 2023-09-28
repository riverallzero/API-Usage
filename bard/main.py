import requests
from bardapi import Bard, SESSION_HEADERS

session = requests.Session()
token = '__Secure-1PSID token'
session.cookies.set('__Secure-1PSID', '__Secure-1PSID token')
session.cookies.set('__Secure-1PSIDCC', '__Secure-1PSIDCC token')
session.cookies.set('__Secure-1PSIDTS', '__Secure-1PSIDTS token')
session.headers = SESSION_HEADERS

bard = Bard(token=token, session=session)

messages = 'question_input'
answer = bard.get_answer(messages)['content']
print(answer)
