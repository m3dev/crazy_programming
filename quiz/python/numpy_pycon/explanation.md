# 解説

文字列のスライスと、オブジェクトが持つ`__name__`属性を組み合わせたお遊び問題です。

まず`np.__name__`は、モジュール（numpy）の名前を表す文字列`'numpy'`です。
これを`[-2:]`で末尾2文字を取り出すと`'py'`になります。

```python
>>> import numpy as np
>>> np.__name__
'numpy'
>>> np.__name__[-2:]
'py'
```

次に`np.conj`は複素共役を求める関数です。関数の`__name__`はその正式名で、`'conjugate'`です。
これを`[:3]`で先頭3文字を取り出すと`'con'`になります。

```python
>>> np.conj.__name__
'conjugate'
>>> np.conj.__name__[:3]
'con'
```

最後に2つを連結すると`'py' + 'con'`で`'pycon'`になります。

```python
>>> np.__name__[-2:]+np.conj.__name__[:3]
'pycon'
```

numpyの中から`"pycon"`という文字列を組み立てる、遊び心のある問題でした。
