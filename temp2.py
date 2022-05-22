import requests,jsonify,json

program = {
    "script" : """print('hello')""",
    "language": "python3",
    "versionIndex": "0",   
    "clientId": "98d1dddd58d0319280f7fc985c00a0e3",
    "clientSecret":"5599cf7a4690d6fb72e3f1abdbe89c1f6b976ef23515281b03ff179655dc022f"
}

url = "https://api.jdoodle.com/v1/execute"

response = requests.post(url, json=program)
data_json = json.loads(response.text)

print(data_json['output'])
