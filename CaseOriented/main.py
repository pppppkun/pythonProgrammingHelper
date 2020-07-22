import os
import utils
import zipfile

# init
origin = os.getcwd()
utils.cd()
MAIN = 'main.py'
CASE = '.mooctest\\testCases.json'
file = os.getcwd() + '\\case_zip'
os.chdir(file)
fstack = list()
noc = 0
total = 0
result = dict()

if __name__ == '__main__':
    for _ in os.listdir(os.getcwd()):
        fstack.append(os.getcwd())
        os.chdir(os.getcwd() + "\\" + _)
        # print(os.getcwd())
        for __ in os.listdir(os.getcwd()):
            fstack.append(os.getcwd())
            os.chdir(os.getcwd() + "\\" + __)
            # print(os.getcwd())
            for ___ in os.listdir(os.getcwd()):
                if not os.path.isdir(___):
                    continue
                fstack.append(os.getcwd())
                os.chdir(os.getcwd() + "\\" + ___)
                # print(os.getcwd())
                for filename in os.listdir(os.getcwd()):
                    try:
                        utils.unzip(filename)
                        res = utils.detect_use_case_oriented(MAIN, CASE, _, __, ___, result)
                        if res != -1:
                            noc += 1
                        total += 1
                        utils.rm_file(filename)
                    except PermissionError:
                        print('permissionError')
                        print(_, __, ___)
                        exit()
                    except zipfile.BadZipFile:
                        print('badZipFile')
                        print(_, __, ___)
                        if ___ != '233383':
                            exit()
                    except FileNotFoundError:
                        print('fileNoteFoundError')
                        print(_, __, ___)
                        exit()

                os.chdir(fstack[-1])
                fstack.pop(-1)
            os.chdir(fstack[-1])
            fstack.pop(-1)
        os.chdir(fstack[-1])
        fstack.pop(-1)
    print(noc, total, noc / total)
    sorted(result, key=lambda x: result[x].sort_key)
    # for _ in result:
    #     print(result[_])
    os.chdir(origin)
    utils.get_msg(result)

    # while True:
    #     print("请输入userId和caseId来定位具体的提交")
    #     userId = input()
    #     caseId = input()
    #     print(result[userId+' '+caseId])
    #     print('有嫌疑的提交为')
    #     for _ in result[userId + ' ' + caseId].match_records:
    #         print(_, result[userId+' '+caseId].match_records[_])
    #     print("是否查看具体代码，需要请输出1，否则输入0")
    #     f = int(input())
    #     while True:
    #         if f == 1:
    #             print("请输入提交id，如果想查看其他提交请输出0")
    #             uploadId = input()
    #             if uploadId == '0':
    #                 break
    #             result[userId + ' ' + caseId].get_code(uploadId)
    #         elif f == 0:
    #             break
    #         else:
    #             print("请重新输入")
    #             f = int(input())


