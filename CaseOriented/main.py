from utils import *
import numpy as np
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

import zxing
import requests


Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_2 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7D11 Safari/528.16



for i in range(50):
    reader = zxing.BarCodeReader()
    barcode = reader.decode('h.png')
