from cli.cli import run

run(no_verify=True, debug=False)

from openai import OpenAI


# base_url = "https://newapi.yybot.tech/v1"
# key = "sk-qXRsvZxyPdSNY7zzF03b7f377c5d4063847fC1F7634c87B8"
base_url = "https://api.aigcbest.top/v1"
key = "sk-QFf7bfnGRvSmzpnD9678B5000250401f93A30e3b9eA87775"
client = OpenAI(api_key=key, base_url=base_url)

text = "It seems there was an issue saving your name to the archival memory. Let me try that again. Thank you for your patience, Chad."

import http.client
import json

# conn = http.client.HTTPSConnection(base_url)
# payload = json.dumps({
#    "model": "text-embedding-3-large",
#    "input": text
# })
# headers = {
#    'Authorization': f'Bearer {key}',
#    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
#    'Content-Type': 'application/json'
# }
# conn.request("POST", "/v1/embeddings", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))

print(client.embeddings.create(input=text, model="text-embedding-3-small"))

# headers = {"Content-Type": "application/json"}
# json_data = {"input": text, "model": "text-embedding-ada-002", "user": 0000-00000-00000000000}
# import httpx

# with httpx.Client() as client:
#     response = client.post(
#         f"{base_url}/embeddings",
#         headers=headers,
#         json=json_data,
#         timeout=60,
#     )

# response_json = response.json()

# print(response_json)