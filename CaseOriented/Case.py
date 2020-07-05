class Case:
    uploader = ''
    case_id = ''
    case_type = ''
    final_score = 0
    upload_records = list()
    main_ = list()


    def __init__(self, case, uploader):
        self.uploader = uploader
        self.case_id = case['case_id']
        self.case_type = case['case_type']
        self.final_score = case['final_score']
        self.upload_records = case['upload_records']
        self.main_ = []

    def get_every_upload_score(self):
        s = '每次提交分数 ('
        for _ in self.upload_records:
            s += str(_['score'])
            s += ' '
        s += ')'
        return s

    def __str__(self):
        s = '提交者 {} 题目 {} 类型 {} 最后得分 {} 提交次数 {} '.format(self.uploader, self.case_id, self.case_type, self.final_score, len(self.upload_records))
        s += self.get_every_upload_score()
        return s

