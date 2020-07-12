import re
import numpy as np
import csv


def generate_csv(user_id, question_id, submit_id, moduleComplex):
    codeComplex = 0.1
    for i in range(len(moduleComplex)):
        # print(moduleComplex[i])  # stdin:6:1: C901 'Loop 6' is too complex (4)
        matchObjComplex = re.match(".*is too complex \(([0-9]*)\)", moduleComplex[i])
        moduleComplexVal = eval(matchObjComplex.group(1))
        codeComplex += moduleComplexVal * moduleComplexVal / 10
    csv_line.append(str(user_id) + ',' + str(question_id) + ',' + str(submit_id) + ',' + str(codeComplex))
    # csv_line.append('\n')
    # print(user_id, end=',')
    # print(question_id, end=',')
    # print(submit_id, end=',')
    # print(codeComplex)


csv_line = []
file = open("out.log", "r")
s = file.readline()
last_question_id = ""
user_id = 0
question_id = ""
submit_id = 0
moduleComplex = []
while True:
    # print(s)  # s has \n
    if not s:
        break
    s = s.strip()
    # print(s)  # s has not \n
    matchObj = re.match(".*\\\\([0-9]*)\\\\(.*)\\\\([0-9]*)", s)
    matchFlag = False
    if matchObj:
        # print(s)
        # print(matchObj.group(1))
        # print(matchObj.group(2))
        # print(matchObj.group(3))
        question_id = matchObj.group(2)
        # 过滤掉相同类型的其他提交 只剩最后一次
        if question_id == last_question_id:
            user_id = eval(matchObj.group(1))
            submit_id = eval(matchObj.group(3))
        elif user_id != 0:
            generate_csv(user_id, last_question_id, submit_id, moduleComplex)
        user_id = eval(matchObj.group(1))
        submit_id = eval(matchObj.group(3))
        last_question_id = question_id
    s = file.readline()
    if s == "pass\n":
        moduleComplex.clear()
        s = file.readline()
        while s:
            # 存储模块复杂度
            s = s.strip()
            if re.match(".*\\\\([0-9]*)\\\\(.*)\\\\([0-9]*)", s):
                matchFlag = True
                break
            else:
                moduleComplex.append(s)
            s = file.readline()
    if not matchFlag:
        s = file.readline()

# out.log文件中的最后一次提交
generate_csv(user_id, last_question_id, submit_id, moduleComplex)
# for i in range(len(csv_line)):
#     print(csv_line[i])

# np.savetxt('codeComplex.csv', 5, delimiter='\n')
csvfile = open('csv_test.csv', 'w', newline='')
writer = csv.writer(csvfile, delimiter='\n')
writer.writerow([','.join(['user_id', 'question_id', 'submit_id', 'codeComplex'])])
writer.writerow(csv_line)
