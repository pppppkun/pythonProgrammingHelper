import os
import utils

# init
utils.cd()
MAIN = 'main.py'
CASE = '.mooctest\\testCases.json'
file = os.getcwd() + '\\train'
os.chdir(file)
fstack = list()
noc = 0
total = 0
l = []

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
                    utils.unzip(filename)
                    res = utils.detect_use_case_oriented(MAIN, CASE, _, __, ___)
                    if res == 1:
                        print(os.getcwd())
                        noc += 1
                        a = utils.get_score(_, )
                    total += 1
                    utils.rm_file(filename)
                os.chdir(fstack[-1])
                fstack.pop(-1)
            os.chdir(fstack[-1])
            fstack.pop(-1)
        os.chdir(fstack[-1])
        fstack.pop(-1)
    print(noc, total, noc / total)

