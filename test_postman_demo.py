

import requests

url = "https://httpbin.testing-studio.com/post"

payload = "{\n\t\"username\":{{username}},\n\t\"password\":{{password}},\n\t\"token\":token_value1\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "0cc672a1-a238-4354-bfa8-d05c47f883a7"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)