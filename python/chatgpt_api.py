
api_key = ""

with open("./openai-apikey.txt") as f:
    api_key = f.readlines()[0].rstrip()

import openai
openai.api_key = api_key
print(openai.Model.list())
