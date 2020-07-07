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


def detect_use_case_oriented(file_path, case_path, user_id, case_id, upload_id, r):
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
    lines = main_.split('\n')
    threshold = 0
    ID = user_id + ' '+case_id[0:4]
    s_ = ''
    si_ = ''
    so_ = ''
    ic = 0
    oc = 0
    for case in s:
        in_ = case['input']
        ins = in_.split('\n')
        for _ in ins:
            if _ == '':
                continue
            for __ in lines:
                if _ in __:
                    ic += 1
                    si_ += _ + ' ' + __ + '\n'
                    break

        out_ = case['output']
        outs = out_.split('\n')
        for _ in outs:
            if _ == '':
                continue
            for __ in prints:
                if _ in __:
                    oc += 1
                    so_ += _ + " " + __ + "\n"
                    break
    count = ic + oc
    if count/len(s) > threshold:
        s_ += 'The {} upload is user-case oriented. '.format(user_id + ' ' + case_id + ' ' + upload_id)
        s_ += 'Matched times : {}:{} ({}%)\n'.format(count, 2*len(s), count/(2*len(s))*100)
        s_ += 'Input( {} ):\n'.format(ic/len(s))
        s_ += si_
        s_ += 'Output( {} )\n'.format(oc/len(s)) + so_
        if ID in r:
            r[ID].match_records[upload_id] = s_
        else:
            r[ID] = get_score(user_id, case_id[0:4])
            r[ID].match_records[upload_id] = s_
        r[ID].sort_key = len(r[ID].match_records) / (2*len(s))
        return count

    return -1, ''


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
    # code = r'E:\PythonProject\bigHomework\train\3544\2172线性表\268885\main.py'
    # case = r'E:\PythonProject\bigHomework\train\3544\2172线性表\268885\.mooctest\testCases.json'
    # raa = dict()
    # c = detect_use_case_oriented(code, case, user_id='3544', case_id='2172线性表', upload_id='268885', r=raa)
    # print(raa['3544 2172'])
    # print(raa['3544 2172'].match_records['268885'])
    a = {'a': 2, 'b': 1, 'c': 3}
    print(a)
    print(sorted(a))
    print(sorted(a, key=lambda x:a[x]))


