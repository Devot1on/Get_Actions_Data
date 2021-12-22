import os
import requests,json
import warnings
warnings.filterwarnings("ignore")


headers = [{"Authorization":"token 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"},
           {"Authorization":"token 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"},
           {"Authorization":"token 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"}]

#def get_headers:

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录,创建目录操作函数
        '''
        os.mkdir(path)与os.makedirs(path)的区别是,当父目录不存在的时候os.mkdir(path)不会创建，os.makedirs(path)则会创建父目录
        '''
        #此处路径最好使用utf-8解码，否则在磁盘中可能会出现乱码的情况
        os.makedirs(path)
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False

##获取一个项目中的.github/workflows文件夹下的yml文件,存到mkdir的路径中
def get_ymls(repo):
    mkdir(r'../数据存储/top100_workflows/'+repo.replace('/','-'))
    pageno = 1
    while True:
        github_url = "http://api.github.com/repos/"+repo+"/contents/.github/workflows?page="+str(pageno)
        r = requests.get(github_url,headers = headers[0],verify = False)
        final = json.loads(r.text)
        for single in final:
            if 'download_url' in single:
                yml_cont = get_workflow_content(single['download_url'])
                with open('../数据存储/top100_workflows/'+repo.replace('/','-')+'/'+single['name'],'w',encoding='utf-8') as f:
                    f.write(yml_cont)
            else: break
        print(222)
        if(len(final) != 30):
            break
        pageno += 1

##从获取的下载链接中获取yml文件全文
def get_workflow_content(download_url):
    token = 0

    for i in range (10):
        try:
            r = requests.get(download_url,headers = headers[token],verify = False)
            break
        except:
            token = (token + 1) % 3
            continue
    return r.text
