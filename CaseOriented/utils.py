import os
import shutil
import zipfile
import re
import json
from Case import Case

def unzip(zip_name):
    zip_file = zipfile.ZipFile(zip_name)
    sub_name = zip_file.namelist()[0]
    zip_file.extract(sub_name)
    sub_zip_file = zipfile.ZipFile(sub_name)
    for _ in sub_zip_file.namelist():
        sub_zip_file.extract(_)
    sub_zip_file.close()
    zip_file.close()


def rm_file(dont_rm_file):
    for _ in os.listdir(os.getcwd()):
        if os.path.isdir(_):
            shutil.rmtree(_)
        else:
            if _ == dont_rm_file:
                continue
            os.remove(_)


def detect_use_case_oriented(file_path, case_path, user_id, case_id, upload_id):
    """
    :param file_path: the file which students upload
    :param case_path: the use-case which will be input
    :return: a value between 0-1 represent the rate of how many use-cases this file orient
    """
    c = open(case_path, encoding='utf-8')
    f = open(file_path, encoding='utf-8')
    s = eval(c.read())
    main_ = f.read()
    prints = get_print(main_)
    count = 0
    threshold = 0
    s_ = ''
    for case in s:
        in_ = case['input']
        ins = in_.split('\n')
        for _ in ins:
            if _ == '':
                continue
            # TODO

        out_ = case['output']
        outs = out_.split('\n')
        for _ in outs:
            if _ == '':
                continue
            for __ in prints:
                if _ in __:
                    count += 1
                    s_ += _ + " " + __ + "\n"
                    print(_+" "+__)
                    break
    if count/len(s) > threshold:
        s_ += 'The {} upload is user-case oriented. '.format(case_id+' '+upload_id)
        s_ += 'Num of cases which match in this code : {}:{} ({}%)'.format(count, len(s), count/len(s)*100)
        return 1, s_
    return 0, ''


def get_print(main_function):
    pattern = re.compile('.*(print\(.*\)).*')
    p = pattern.findall(main_function)
    return p


def cd():
    s = os.getcwd()
    s = ''.join(reversed(s))
    for _ in range(len(os.getcwd())):
        if s[_] == '\\':
            break
    os.chdir(os.getcwd()[:len(s)-_-1])


def get_score(user_id, case_id):
    f = open(r'E:\PythonProject\bigHomework\sample.json', encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    cases = data[user_id]['cases']
    for _ in cases:
        if _['case_id'] == case_id:
            return Case(_, user_id)



if __name__ == '__main__':
    case = get_score('48117', '2081')
    print(case.get_code('249346'))
#     MAIN = 'main.py'
#     CASE = '.mooctest\\testCases.json'
#     file = os.getcwd() + '\\train'
#     os.chdir(file)
#     fstack = list()
#     for _ in os.listdir(os.getcwd()):
#         fstack.append(os.getcwd())
#         os.chdir(os.getcwd()+"\\"+_)
#         # print(os.getcwd())
#         for __ in os.listdir(os.getcwd()):
#             fstack.append(os.getcwd())
#             os.chdir(os.getcwd()+"\\"+__)
#             # print(os.getcwd())
#             for ___ in os.listdir(os.getcwd()):
#                 if not os.path.isdir(___):
#                     continue
#                 fstack.append(os.getcwd())
#                 os.chdir(os.getcwd()+"\\"+___)
#                 # print(os.getcwd())
#                 for filename in os.listdir(os.getcwd()):
#                     print(os.getcwd())
#                     unzip(filename)
#                     detect_use_case_oriented(MAIN, CASE)
#                     rm_file(filename)
#                 os.chdir(fstack[-1])
#                 fstack.pop(-1)
#             os.chdir(fstack[-1])
#             fstack.pop(-1)
#         os.chdir(fstack[-1])
#         fstack.pop(-1)



