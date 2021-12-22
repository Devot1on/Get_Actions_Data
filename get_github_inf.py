import requests, json

token = [{"Authorization": "token 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"}]
repo_url = "https://api.github.com/search/repositories?q=stars:>=0"
r = requests.get(repo_url, headers=token[0])
final = json.loads(r.text)
print(final)