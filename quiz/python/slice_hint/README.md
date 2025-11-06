# Slice Hint

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

リストのスライスの知識を深める難読クイズ（上級編）。

```python
_:...=[];_[:]:...=f'{f"{[...][::][0]}"::^0}';_
```

## 実行

`uv run python`でREPLを起動して、上記を貼り付けて実行するのが最も簡単です。

REPLの一部機能を再現して実行する以下のスクリプトでも、同じ結果が得られます。

```sh
uv run python -c 'import sys, ast as A
src = sys.stdin.read()
mod = A.parse(src, "<stdin>", "exec")

class Echo(A.NodeTransformer):
    def visit_Expr(self, node):
        assign = A.Assign(targets=[A.Name("_", A.Store())], value=node.value)
        pr = A.Expr(
            value=A.Call(func=A.Name("print", A.Load()),
                         args=[A.Call(func=A.Name("repr", A.Load()),
                         args=[A.Name("_", A.Load())], keywords=[])],
                         keywords=[]))
        return [assign, pr]

mod = Echo().visit(mod)
A.fix_missing_locations(mod)
exec(compile(mod, "<stdin>", "exec"), {})
' < main.py
```

## 解説

`explanation.md`で解説しています
