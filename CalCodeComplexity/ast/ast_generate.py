import ast
import astpretty

file_path = ".\\ast_demo.py"
f = open(file_path, encoding='utf-8')
text = f.read()
astpretty.pprint(ast.parse(text, "exec"),indent="  ")
f.close()

# astpretty.pprint(ast.parse('''a = 1
# if a > 0:
#     print(a)
# else:
#     print(0)
# ''', "exec"),indent="  ")