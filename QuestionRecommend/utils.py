import os
import json
import numpy as np
# import biasSVD

# 61715
# 271
# 2991
# 882
# 84203


def open_json(filename):
    s = os.getcwd()
    __ = os.getcwd()
    s = ''.join(reversed(s))
    for _ in range(len(os.getcwd())):
        if s[_] == '/':
            break
    os.chdir(os.getcwd()[:len(s) - _ - 1])

    f = open(filename, encoding='utf-8')
    res = f.read()
    data = json.loads(res)
    f.close()
    os.chdir(__)
    return data
    # l = []
    # for _ in data:
    #     if int(_) not in l:
    #         l.append(int(_))
    # print(max(l))
    # print(len(l))
    # l = []
    # s = 0
    # for _ in data:
    #     for __ in data[_]['cases']:
    #         if int(__['case_id']) not in l:
    #             l.append(int(__['case_id']))
    #         s += len(__['upload_records'])
    # print(max(l))
    # print(len(l))
    # print(s)


def get_num_of_user(data):
    l = []
    for _ in data:
        if int(_) not in l:
            l.append(int(_))
    return len(l)


def get_num_of_case(data):
    l = []
    for _ in data:
        for __ in data[_]['cases']:
            if int(__['case_id']) not in l:
                l.append(int(__['case_id']))
    return len(l)


def origin_data_to_list(data):
    user = []
    case = []
    for _ in data:
        user.append(_)
        for __ in data[_]['cases']:
            case_id = int(__['case_id'])
            if case_id not in case:
                case.append(case_id)
    user.sort()
    case.sort()
    return user, case


def get_matrix(filename):
    data = open_json(filename)
    r = get_num_of_user(data)
    c = get_num_of_case(data)
    user, case = origin_data_to_list(data)
    mat = np.empty(shape=[r, c])
    mark_mat = []
    for _ in data:
        i = user.index(_)
        for __ in data[_]['cases']:
            case_id = int(__['case_id'])
            final_score = __['final_score']
            j = case.index(case_id)
            mat[i][j] = final_score
            if [i, j] not in mark_mat:
                mark_mat.append([i, j])
    return mat, mark_mat


if __name__ == '__main__':
    mat, mark_mat = get_matrix('test_data.json')
    # print(len(mark_mat))
    t = np.random.rand(len(mark_mat), 1)
    # print(t[0])
    train = [mark_mat[_] for _ in range(len(mark_mat)) if t[_][0] >= 0.2]
    test = [mark_mat[_] for _ in range(len(mark_mat)) if t[_][0] < 0.2]
    # print(len(train)+len(test))
    # print(len(mark_mat))
    # def biasSVD(data, k, steps, learning_rate, l):
    # biasSVD.biasSVD(mat, 10, 100, 0.0005, 0.1, mark_mat)