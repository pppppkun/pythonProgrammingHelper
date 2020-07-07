import os
import zipfile
import shutil


class Case:

    def __init__(self, case, uploader):
        self.uploader = uploader
        self.case_id = case['case_id']
        self.case_type = case['case_type']
        self.final_score = case['final_score']
        self.upload_records = case['upload_records']
        self.match_records = dict()
        self.sort_key = 0

    def get_every_upload_score(self):
        s = '每次提交分数 { '
        for _ in self.upload_records:
            s += '(' + str(_['upload_id']) + ' ' + str(_['score']) + ')'
            s += ' '
        s += '}'
        return s

    def __str__(self):
        s = '提交者 {} 题目 {} 类型 {} 最后得分 {} 提交次数 {} '.format(self.uploader, self.case_id, self.case_type, self.final_score, len(self.upload_records))
        s += self.get_every_upload_score()
        return s

    def get_code(self, upload_id):
        # 'E:\PythonProject\bigHomework\train\3544\2172线性表\268885\'
        p = os.getcwd()
        basic = 'E:\PythonProject\\bigHomework\\train\\'
        os.chdir(basic + self.uploader + '\\' + self.case_id+self.case_type + "\\" + upload_id+"\\")
        l = os.listdir(os.getcwd())
        s = l[0]
        for fileName in l:
            zip_file = zipfile.ZipFile(fileName)
            sub_name = zip_file.namelist()[0]
            zip_file.extract(sub_name)
            sub_zip_file = zipfile.ZipFile(sub_name)
            for _ in sub_zip_file.namelist():
                sub_zip_file.extract(_)
            sub_zip_file.close()
            zip_file.close()
        f = open('main.py', encoding='utf-8')
        print(f.read())
        f.close()
        dont_rm_file = s
        for _ in os.listdir(os.getcwd()):
            if os.path.isdir(_):
                shutil.rmtree(_)
            else:
                if _ == dont_rm_file:
                    continue
                os.remove(_)
        os.chdir(p)

