# 解説

3つのメンバを定義したように見える`Enum`ですが、答えは1要素の辞書になります。
これは「Enumのエイリアス」と「辞書の後勝ち」という2つの仕組みが重なった問題です。

まずEnumには、同じ値を持つメンバは「エイリアス（別名）」になるという仕様があります。
Pythonでは`1 == True == 1.0`なので、`bool_num`と`float_num`は、最初に定義された`int_num`のエイリアスになります。

```python
>>> from enum import Enum
>>> class Ex(Enum):
...     int_num = 1
...     bool_num = True
...     float_num = 1.0
...
>>> Ex['bool_num'] is Ex['int_num']
True
>>> Ex['float_num'] is Ex['int_num']
True
>>> Ex['bool_num']
<Ex.int_num: 1>
```

つまり`Ex['int_num']`・`Ex['bool_num']`・`Ex['float_num']`はすべて同一のオブジェクト`Ex.int_num`です。

次に辞書のリテラルを見ます。キーがすべて同じ`Ex.int_num`なので1つのキーに衝突し、
値は後から書かれたもので上書きされます（後勝ち）。

```python
>>> {Ex['int_num']:'int', Ex['bool_num']:'bool', Ex['float_num']:'float'}
{<Ex.int_num: 1>: 'float'}
```

キーは最初に定義された`Ex.int_num`、値は最後の`'float'`が残ります。
Enumのエイリアス仕様と、辞書の後勝ちの二段構えがポイントの問題でした。
