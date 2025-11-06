# Sum Trick

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

sum関数の仕様をハックする系の難読クイズ。

```python
sum(((1,(2,(3),),(4,)),(5,),),())
```

## 実行

```sh
uv run python -c "import sys; code=sys.stdin.read(); print(eval(code))" < main.py
```

## 解説

`explanation.md`で解説しています
