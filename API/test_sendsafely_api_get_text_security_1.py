import requests

def test_sendsafely_api_get_text_security_1():
    r=requests.get('https://www.sendsafely.com/security/')

    if r.status_code == 200:
        print(f"\nPASS_STATUS = {r.status_code}")
    else:
        print(f'\nFAIL_STATUS ="{r.status_code}"')

    whole_txt = r.text
    wrd = 'Web Application Security'
    # print(whole_txt)
    if wrd in whole_txt:
        print(f'\nFound: "{wrd}"')
    else:
        print(f'\nNot found: "{wrd}"')

    print(f'\nUrl of the response: {r.url}')  # url of the response



