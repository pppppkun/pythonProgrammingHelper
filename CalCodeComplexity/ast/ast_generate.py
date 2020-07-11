import ast
import astpretty

file_path = ".\\ast_demo.py"
f = open(file_path, encoding='utf-8')
text = f.read()
astpretty.pprint(ast.parse(text, "exec"),indent="  ")
f.close()