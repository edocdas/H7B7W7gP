import requests

params = {'username': 'aaa', 'password': 'password'}

s = requests.Session()

s.post(
    'https://pythonscraping.com/pages/cookies/login.html', params)
print('Cookie is set to:')
print(s.cookies.get_dict())
print('Going to profile page...')
result = s.get('http://pythonscraping.com/pages/cookies/profile.php')
print(result.text)
