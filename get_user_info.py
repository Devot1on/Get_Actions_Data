import requests,json

def get_user(username):
    header = {"Authorization":"token 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"}
    user_url = "https://api.github.com/user/%s"%(username)
    r = requests.get(user_url,headers = header)
    final = json.loads(r.text)
    print(final)

def main():
    username = input("输入查询的用户名：")
    get_user(username)
    #get_famous_repo()

if __name__ == '__main__':
    main()