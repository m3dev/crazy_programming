# 技術書典

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

`dir`という名前を変数にしてしまって混乱する、文字数を使ったクイズ。

```python
f"{chr(len(dir(dir:='技術書典'))-len(dir))}{~(-len(dir))}"
```

## 実行

```sh
uv run python -c "import sys; code=sys.stdin.read(); print(eval(code))" < main.py
```

## 解説

`explanation.md`で解説しています
