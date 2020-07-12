import os
import shutil
import zipfile
import time
import mccabe
import sys

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


def detect_use_case_oriented_and_cal_complex(file_path, case_path):
    """
    :param file_path: the file which students upload
    :param case_path: the use-case which will be input
    :return: a value between 0-1 represent the rate of how many use-cases this file orient
    """
    c = open(case_path, encoding='utf-8')
    f = open(file_path, encoding='utf-8')
    s = eval(c.read())
    main_ = f.read()
    count = 0
    threshold = 0.15
    for case in s:
        in_ = case['input']
        out_ = case['output']
        if in_ in main_ or out_ in main_:
            count += 1
    if count/len(s) > threshold:
        print('this upload is user-case oriented')
    else:
        print('pass')
        cal_metric(main_)
    # must be close
    c.close()
    f.close()
    return count/len(s)


def cal_time_complex(file_path, case_path):
    # TODO
    c = open(case_path, encoding='utf-8')
    f = open(file_path, encoding='utf-8')
    s = eval(c.read())
    for case in s:
        in_ = case['input']
        test = open('testCases.in', 'w')
        test.write(in_)
        test.close()
        code = 'main.py'
        start = time.time()
        os.system('python ' + code + ' < ' + 'testCases.in' + ' >> ' + 'testCases.in')
        end = time.time()
        print(end - start)

def cal_metric(text):
    mccabe.get_code_complexity(text, 1)

if __name__ == '__main__':
    # 重定向输出流
    f_handler = open('out.log', 'w')
    sys.stdout = f_handler
    MAIN = 'main.py'
    CASE = '.mooctest\\testCases.json'
    file = '..\\train'
    os.chdir(file)
    fstack = list()
    for _ in os.listdir(os.getcwd()):
        fstack.append(os.getcwd())
        os.chdir(os.getcwd()+"\\"+_)
        # print(os.getcwd())
        for __ in os.listdir(os.getcwd()):
            fstack.append(os.getcwd())
            os.chdir(os.getcwd()+"\\"+__)
            # print(os.getcwd())
            for ___ in os.listdir(os.getcwd()):
                if not os.path.isdir(___):
                    continue
                fstack.append(os.getcwd())
                os.chdir(os.getcwd()+"\\"+___)
                # print(os.getcwd())
                for filename in os.listdir(os.getcwd()):
                    print(os.getcwd())
                    unzip(filename)
                    detect_use_case_oriented_and_cal_complex(MAIN, CASE)
                    time.sleep(0.1)
                    rm_file(filename)
                os.chdir(fstack[-1])
                fstack.pop(-1)
            os.chdir(fstack[-1])
            fstack.pop(-1)
        os.chdir(fstack[-1])
        fstack.pop(-1)



