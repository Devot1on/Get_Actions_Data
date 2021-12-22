import requests, json
import os

#获取一个仓库的workflow
def get_repo_workflow(repo):
    token = [{"Authorization":"token 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"}]
    workflow_url = "http://api.github.com/repos/"+repo+"/actions/workflows"
    r = requests.get(workflow_url,headers = token[0])
    final = json.loads(r.text)
    #print(final)
    #for single in final['workflows']:
        #print(single['path'],single['state'])
    return(final['total_count'])
#get_repo_workflow('netdata/netdata')

def get_repo_workflow_inf(repo):
    token = [{"Authorization":"token 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"},{"Authorization":"token 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"}]
    workflow_url = "http://api.github.com/repos/"+repo+"/actions/workflows"
    r = requests.get(workflow_url,headers = token[1])
    final = json.loads(r.text)
    return(final)