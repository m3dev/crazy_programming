# 解説

この問題は `Reduce 5000` の発展版です。lambdaのデフォルト引数の中でセイウチ演算子を使い、`reduce`や`map`という名前を再代入する目くらましを重ねています。

まず前提として、`unicodedata.numeric`はUnicode文字の数値を返す関数です。

```python
>>> from unicodedata import numeric
>>> list(map(numeric, '5000兆'))
[5.0, 0.0, 0.0, 0.0, 1000000000000.0]
```

次に問題のlambdaを見ます。

```python
lambda numeric=(reduce:=map), map=(reduce:=numeric): numeric*map
```

デフォルト引数の右辺に `reduce:=map` や `reduce:=numeric` といったセイウチ代入が書かれており、`reduce`という名前があちこちで書き換えられているように見えます。しかしこれらはデフォルト値を計算するときに評価されるだけで、実際に`reduce`関数が呼ばれた後の畳み込み計算には影響しません。

lambda本体は `numeric * map`、つまり受け取った2つの引数の掛け算です。`reduce`はこのlambdaで列を左から畳み込みます。

```python
>>> from functools import reduce
>>> reduce(lambda numeric=(reduce:=map), map=(reduce:=numeric): numeric*map, [5.0, 0.0, 0.0, 0.0, 1000000000000.0])
0.0
```

列の中に`0.0`が含まれるので、積はどこかで`0.0`になり、最終結果も`0.0`です。

```python
>>> reduce(lambda numeric=(reduce:=map), map=(reduce:=numeric):numeric*map, map(numeric,'5000兆'))
0.0
```

答えは`0.0`です。
デフォルト引数でのセイウチ代入という派手な目くらましがあっても、計算の本質は0を含む積なので0になる、という問題でした。
