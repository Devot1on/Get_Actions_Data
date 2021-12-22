import csv
import repo_workflow

def get_workflow_created(path):
    title = ['repo_name', 'workflow_name','path','state','created_at','updated_at']
    csvfile1 = open('../数据存储/workflow信息.csv', 'w', newline='',encoding = "utf-8")
    writer = csv.writer(csvfile1)
    writer.writerow(title)

    csvfile = open(path, 'r')
    reader = csv.reader(csvfile)
    lines = list(reader)
    index = 1 #从文件的第2行开始
    while(index < len(lines)):
        print(lines[index][0])
        inf = repo_workflow.get_repo_workflow_inf(lines[index][0])
        for single in inf['workflows']:
            newline = [lines[index][0],single['name'],single['path'],single['state'],single['created_at'],single['updated_at']]
            writer.writerow(newline)
        index += 1
    csvfile1.close()
    csvfile.close()

get_workflow_created('../数据存储/热门项目.csv')