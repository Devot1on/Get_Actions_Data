import requests, json
import csv
import repo_workflow
import get_workflows_with_api
import warnings
warnings.filterwarnings("ignore")

#获取github star数最多的100个项目，通过api记录它们有多少个workflow
def get_famous_repo():
    title = ['full_name','language','stargazers_count','forks','watchers','workflows_count']
    csvfile = open('../数据存储/热门项目.csv', 'w', newline='')
    writer = csv.writer(csvfile)
    writer.writerow(title)

    token = [{"Authorization":"token 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"}]
    repo_url = "https://api.github.com/search/repositories?q=stars:>=100&sort=stars&per_page=100&order=desc"
    r = requests.get(repo_url,headers = token[0])
    final = json.loads(r.text)
    for single in final['items']:
        row = (single['full_name'],single['language'],single['stargazers_count'],single['forks'],single['watchers'],repo_workflow.get_repo_workflow(single['full_name']))
        writer.writerow(row)
    csvfile.close()

#尝试获取前10000个项目
def get_large_famous_repo():
    #title = ['full_name','language','stargazers_count','forks','watchers','workflows_count']
    csvfile = open('../../数据存储/热门项目10000.csv', 'a+', newline='')
    writer = csv.writer(csvfile)
    #writer.writerow(title)

    token = [{"Authorization":"token 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"}]
    workflow_count = []

    pageno = 1
    while(pageno <= 50):
        repo_url = "https://api.github.com/search/repositories?q=watchers:<=16318&sort=stars&per_page=100&order=desc&page="+str(pageno)
        r = requests.get(repo_url,headers = token[0])
        final = json.loads(r.text)

        for single in final['items']:
            workflow_num = repo_workflow.get_repo_workflow(single['full_name'])
            row = (single['full_name'],single['language'],single['stargazers_count'],single['forks'],single['watchers'],workflow_num)
            workflow_count.append(workflow_num)
            writer.writerow(row)
        print(pageno)
        pageno += 1
    print(sum(workflow_count))
    print(float(sum(workflow_count)/len(workflow_count)))
    csvfile.close()


def get_famous_repo_yml():
    csvfile = open('../../数据存储/热门项目10000.csv', 'r', newline='')
    reader = csv.reader(csvfile)
    lines = list(reader)
    index = 1 #从文件的第2行开始
    while(index < len(lines)):
        print(lines[index][0],lines[index][5])
        if(int(lines[index][5]) != 0):
            get_workflows_with_api.get_ymls(lines[index][0])
        index += 1

def main():
    get_large_famous_repo()
    #get_famous_repo_yml()
    #get_famous_repo()

if __name__ == '__main__':
    main()