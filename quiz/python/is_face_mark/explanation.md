# 解説

Pythonの三項演算子(if/else)の実行順序を確認してみます。

```python
>>> def func(x, y=None):
        print(x)
        return y

>>> func('a') if func('b', True) else func('c')
b
a

>>> func('a') if func('b', False) else func('c')
b
c
```

まずifの後ろの条件文が評価され、その後2つの値に分岐することがわかります。
クイズのif句の後ろの顔文字が何を実行しているのかを知るのが第一歩です。

まず変数cにAssignment Expressionsを使い値を代入しています。
Assignment Expressionsはセイウチ演算子とも呼ばれる式です。
以下の式では変数xに1を代入するだけでなく、1が標準出力にprintされます。

```python
>>> print(x := 1)
1
```

以下の式は変数cに何かを代入し、その値を返す式であることがわかります。

```python
(c:=('ω')<"hi")
```

以下は顔文字のように見せていますが、実は文字列と文字列の比較です。

```python
('ω') < "hi"
```

以下はtupleのように見えますが、文字列`ω`と同値です。
tupleのような記述でも1要素かつカンマが付かない場合は中身が評価されるだけです。

```python
>>> ('ω')
"ω"

>>> ('ω',)
("ω",)
```

つまり以下の文字列比較であると言えます。
Pythonの文字列同士の比較はUnicode コードポイントの比較です。
英語アルファベットの方がUnicodeコードポイント上で前方（数値的には小さい）です。
Unicodeコードポイントの原理が感覚的に分かっていればFalseと読み解けます。

```python
>>> "a" < "b"
True

>>> "c" < "b"
False

>>> "ω" < "hi"
False
```

もう一度クイズ全体を見てみます。
if句後の条件式が、変数cにFalseを代入しながらFalseを返す式であると分かり、シンプルな構造だと分かります。

```python
(d >_< b) if (c:=('ω')<"hi") else (c^0^c)-~3
```

次にelseの後ろの式について考えてみます。
変数cにはFalseが入っているので、変数を置き換えてみると以下のようになります。

```python
(False ^ 0 ^ False) -~ 3
```

`^`はXOR(排他的論理和)です。
PythonにおいてBool型はint型のサブクラスですので、Falseは0と解釈できます。

```python
>>> 0 ^ 0 ^ 0
0
```

括弧の中が0だとすると後半の式は以下のようになります。
チルダ("~")によるbool値のNOTです、実質的に~xは-(x+1)にあたります。

```python
>>> 0 -~ 3  # 4
```

つまり以下を実行するとelseの後ろの式が実行され数値の4が返ってくる訳です。

```python
>>> (d >_< b) if (c:=('ω')<"hi") else (c^0^c)-~3
4
```

いくつかのPythonらしいトリックを複数使った難読クイズでした。
気付いた方もいるやもしれませんが、実はこの問題の前半の顔文字は実行できません。

```python
>>> (d >_< b) if True else (c^0^c)-~3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined. Did you mean: 'id'?
```

変数dやbが定義されていないというエラーです。
言ってしまえば、実行されない部分は何を書いても良いという訳です。
