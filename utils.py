import re


class Variable(object):
    def __init__(self, value, type_):
        # value = str
        # type_ = str
        self.value = value
        self.type_ = type_

    def __str__(self):
        return self.value + self.type_

    def __repr__(self):
        return str(self.value) + " " + str(self.type_)


def clean_all_space(s):
    l = list(s)
    while ' ' in l:
        l.remove(' ')
    return ''.join(l)


def add_to_var_pool(s, docker):
    s = clean_all_space(s)
    var_name = ''
    value = ''
    index = (str)(s).find('=', 0, len(s))
    for i in range(index):
        var_name += s[i]
    for i in range(index+1, len(s)):
        value += s[i]
    type_ = judge_type(value)
    v = Variable(value, type_)
    docker[var_name] = v

def judge_type(s):
    s = str(s)
    pattern = re.compile(r'[a-zA-Z0-9_]+()')
    if s.isdigit():
        return 'int'
    if s.isalpha():
        return 'str'
    if re.match(pattern, s):
        a = re.match(pattern, s)
        return a[0]
    if '[' in s and ']' in s:
        return 'list'

def print_value(docker):
    for _ in docker:
        v = docker[_]
        type_ = v.type_
        print(_, v.value)




if __name__ == '__main__':
    s = "a = 1"
    statement = ['a = 1', 'a = []', 'a = [\'a\',\'b\',\'c\']', 'var_pool = dict()', 'a_b = [1,2,2]']
    var_pool = dict()
    for s in statement:
        add_to_var_pool(s, var_pool)
    print_value(var_pool)
