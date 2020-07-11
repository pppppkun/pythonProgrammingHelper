import mccabe

file_path = ".\\demo_combine.py"
f = open(file_path, encoding='utf-8')
text = f.read()
mccabe.get_code_complexity(text,1)
f.close()
print('----------------------------------------')
file_path = ".\\demo_separate.py"
f = open(file_path, encoding='utf-8')
text = f.read()
mccabe.get_code_complexity(text,1)
f.close()