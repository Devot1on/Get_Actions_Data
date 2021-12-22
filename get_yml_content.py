import requests,json


headers = {"Authorization":"token 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"}

github_url = "https://raw.githubusercontent.com/Devot1on/rapidsms/develop/.github/workflows/greetings.yml"
r = requests.get(github_url)


print(r.text)

with open('greetings.yml','w') as f:
    f.write(r.text)
