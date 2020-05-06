import json
import urllib.request
import urllib.parse
import os
f = open('sample.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
case_zip = 'http://mooctest-site.oss-cn-shanghai.aliyuncs.com/target/'
base_env = os.getcwd()
for _ in data:
    cases = data[_]['cases']
    for __ in cases:
        if __['final_score'] == 100:
            os.chdir(base_env)
            path = os.getcwd() + '\\' + 'train'
            path = path + '\\' + str(_)
            if not os.path.exists(path):
                os.mkdir(path)
            path = path + '\\' + str(__['case_id']) + str(__['case_type'])
            if not os.path.exists(path):
                os.mkdir(path)
            path_ = urllib.parse.quote(urllib.parse.unquote(os.path.basename(__['case_zip'])))
            cur_url = case_zip+path_
            temp = os.getcwd()
            os.chdir(path)
            urllib.request.urlretrieve(cur_url, os.path.basename(__['case_zip']))
            os.chdir(temp)
            upload_records = __['upload_records']
            if upload_records:
                for ___ in upload_records:
                    temp = path
                    path = path + '\\' + str(___['upload_id'])
                    if not os.path.exists(path):
                        os.mkdir(path)
                    os.chdir(path)
                    urllib.request.urlretrieve(___['code_url'], urllib.parse.unquote(os.path.basename(___['code_url'])))
                    os.chdir(temp)
                    path = temp

# cases = data['3544']['cases']
# for _ in cases:
#     if _['final_score'] == 100:
#         upload_records = _['upload_records']
#         if upload_records == []:
#             continue
#         else:
#             filename = urllib.parse.unquote(os.path.basename('case_zip'))
#             print(filename)
#             print(upload_records)





