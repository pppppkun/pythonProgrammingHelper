import os
import shutil
import zipfile
import re


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


def detect_use_case_oriented(file_path, case_path):
    """
    :param file_path: the file which students upload
    :param case_path: the use-case which will be input
    :return: a value between 0-1 represent the rate of how many use-cases this file orient
    """
    c = open(case_path, encoding='utf-8')
    f = open(file_path, encoding='utf-8')
    s = c.read()
    s = s[1:len(s)-1]
    c = s.split(',')



if __name__ == '__main__':
    c = open('testCases.json', encoding='utf-8')
    s = c.read()
    pattern = re.compile(r'".+"')
    c = pattern.findall(s)


    # MAIN = 'main.py'
    # CASE = '.mooctest\\testCases.json'
    # file = os.getcwd() + '\\train'
    # os.chdir(file)
    # fstack = list()
    # for _ in os.listdir(os.getcwd()):
    #     fstack.append(os.getcwd())
    #     os.chdir(os.getcwd()+"\\"+_)
    #     # print(os.getcwd())
    #     for __ in os.listdir(os.getcwd()):
    #         fstack.append(os.getcwd())
    #         os.chdir(os.getcwd()+"\\"+__)
    #         # print(os.getcwd())
    #         for ___ in os.listdir(os.getcwd()):
    #             if not os.path.isdir(___):
    #                 continue
    #             fstack.append(os.getcwd())
    #             os.chdir(os.getcwd()+"\\"+___)
    #             # print(os.getcwd())
    #             for filename in os.listdir(os.getcwd()):
    #                 print(os.getcwd())
    #                 unzip(filename)
    #                 detect_use_case_oriented(MAIN, CASE)
    #                 rm_file(filename)
    #             os.chdir(fstack[-1])
    #             fstack.pop(-1)
    #         os.chdir(fstack[-1])
    #         fstack.pop(-1)
    #     os.chdir(fstack[-1])
    #     fstack.pop(-1)



