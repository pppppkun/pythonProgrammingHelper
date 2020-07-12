import os
import shutil
import zipfile
import re
import json
import csv
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
            if _ == '' or len(_) == 1:
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


def get_msg(res):
    _ = open('result.log', encoding='utf-8')
    cor = eval(_.read())
    _.close()
    cd()
    f = open('sample.json', encoding='utf-8')
    _ = f.read()
    data = json.loads(_)
    r = dict()

    for _ in data:
        for __ in data[_]['cases']:
            case_id = __['case_id']
            if case_id not in r:
                r[case_id] = dict()
                r[case_id]['users'] = 0  # 提交人数
                r[case_id]['uploads'] = 0  # 提交次数
                r[case_id]['average'] = 0  # 总得分
                r[case_id]['100'] = 0  # 满分比例
            r[case_id]['users'] += 1
            if _ + ' ' + case_id in res:
                s = 0
                for ___ in __['upload_records']:
                    if str(___['upload_id']) not in res[_+' '+case_id].match_records:
                        r[case_id]['uploads'] += 1
                        s = max(s, ___['score'])
                r[case_id]['average'] += s
                if s == 100:
                    r[case_id]['100'] += 1
            else:
                r[case_id]['uploads'] += len(__['upload_records'])
                r[case_id]['average'] += __['final_score']
                if __['final_score'] == 100:
                    r[case_id]['100'] += 1
    for _ in r:
        r[_]['100'] = r[_]['100']/r[_]['users']
        try:
            r[_]['average'] = r[_]['average'] / r[_]['uploads']
        except ZeroDivisionError:
            print(_)
            print(r[_])
    l = dict()
    for _ in res:
        c = _.split(' ')[1]
        if c in l:
            l[c] += 1
        else:
            l[c] = 1
    for _ in r:
        if _ in l:
            r[_]['users'] = l[_]/r[_]['users']
        else:
            r[_]['users'] = 0
    csvfile = open('csv_test.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter='\n')
    writer.writerow([','.join(['case_id', 'case_oriented_ratio', 'final_average_score', 'full_score_ratio', 'upload_times'])])
    for _ in r:
        s = []
        s.append(_)
        s.append(str(r[_]['users']))
        s.append(str(r[_]['average']))
        s.append(str(r[_]['100']))
        s.append(str(r[_]['uploads']))
        writer.writerow([','.join(s)])
    csvfile.close()



if __name__ == '__main__':
    code = r'E:\PythonProject\bigHomework\train\3544\2172线性表\268885\main.py'
    case = r'E:\PythonProject\bigHomework\train\3544\2172线性表\268885\.mooctest\testCases.json'
    raa = dict()
    c = detect_use_case_oriented(code, case, user_id='3544', case_id='2172线性表', upload_id='268885', r=raa)
    print(raa['3544 2172'])
    print(raa['3544 2172'].match_records['268885'])
    a = {'a': 2, 'b': 1, 'c': 3}
    print(a)
    print(sorted(a))
    print(sorted(a, key=lambda x:a[x]))




