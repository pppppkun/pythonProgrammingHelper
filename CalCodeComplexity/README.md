## 代码复杂度模块

圈复杂度(Cyclomatic complexity)是一种用于衡量代码复杂度的标准，具体表现为一个模块判定逻辑（条件分支、循环）的复杂度，数量上为线性无关的路径条数。圈复杂度大说明代码模块逻辑复杂，较难进行测试和维护，代码质量较低。

通过python中的ast与astpretty可以生成一段python代码的抽象语法树（AST）并以用户友好的方式打印出来，如下以程序

```python
a = 1
if a > 0:
    print(a)
else:
    print(0)
```

使用下列代码可得到可视化的抽象语法树
```python
import ast
import astpretty

astpretty.pprint(ast.parse('''a = 1
if a > 0:
    print(a)
else:
    print(0)
''', "exec"),indent="  ")
```

生成ast为

```python
Module(
  body=[
    Assign(
      lineno=1,
      col_offset=0,
      targets=[Name(lineno=1, col_offset=0, id='a', ctx=Store())],
      value=Num(lineno=1, col_offset=4, n=1),
    ),
    If(
      lineno=2,
      col_offset=0,
      test=Compare(
        lineno=2,
        col_offset=3,
        left=Name(lineno=2, col_offset=3, id='a', ctx=Load()),
        ops=[Gt()],
        comparators=[Num(lineno=2, col_offset=7, n=0)],
      ),
      body=[
        Expr(
          lineno=3,
          col_offset=4,
          value=Call(
            lineno=3,
            col_offset=4,
            func=Name(lineno=3, col_offset=4, id='print', ctx=Load()),
            args=[Name(lineno=3, col_offset=10, id='a', ctx=Load())],
            keywords=[],
          ),
        ),
      ],
      orelse=[
        Expr(
          lineno=5,
          col_offset=4,
          value=Call(
            lineno=5,
            col_offset=4,
            func=Name(lineno=5, col_offset=4, id='print', ctx=Load()),
            args=[Num(lineno=5, col_offset=10, n=0)],
            keywords=[],
          ),
        ),
      ],
    ),
  ],
)

```

进而通过遍历程序抽象语法树中的节点，递归分析抽象语法树中的条件分支表达式、循环表达式以及函数模块，分别计算各节点的圈复杂度

```python
If(expr test, stmt* body, stmt* orelse)
For(expr target, expr iter, stmt* body, stmt* orelse)
While(expr test, stmt* body, stmt* orelse)
FunctionDef(identifier name, arguments args,stmt* body, expr* decorator_list, expr? returns)
```

在计算python程序复杂度时，使用了mccabe库，原理即分析程序的抽象语法树，由于提交的python程序可能涉及多个模块，之前已计算出各节点即各模块的复杂度，故需要使用一种算法通过多个模块的复杂度计算出一个值以衡量整个程序的复杂度



参考 [Python抽象语法树](https://www.dazhuanlan.com/2019/12/14/5df3f50c003f4/)
