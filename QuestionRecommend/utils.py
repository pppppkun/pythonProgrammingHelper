import os
import json


if __name__ == '__main__':
    s = os.getcwd()
    s = ''.join(reversed(s))
    for _ in range(len(os.getcwd())):
        if s[_] == '\\':
            break
    os.chdir(os.getcwd()[:len(s) - _ - 1])

    f = open('sample.json', encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    l = []
    for _ in data:
        if int(_) not in l:
            l.append(int(_))
    print(max(l))
    print(len(l))
    l = []
    s = 0
    for _ in data:
        for __ in data[_]['cases']:
            if int(__['case_id']) not in l:
                s += len(data[_]['cases'])
                l.append(int(__['case_id']))
    print(max(l))
    print(len(l))
    print(s)
