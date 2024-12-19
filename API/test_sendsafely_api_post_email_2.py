import requests
import random
import string

def test_sendsafely_api_post_email_2():
    payload = {
        'email': 'email@email.email',
    }
    r = requests.post('https://www.sendsafely.com/auth/#signup', data=payload)

    if r.status_code == 200:
        print(f"\nPASS_STATUS = {r.status_code}")
    else:
        print(f'\nFAIL_STATUS ="{r.status_code}"')

    print(f'\nUrl of the response: {r.url}')  # url of the response


