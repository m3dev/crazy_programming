# 解説

numpy.arangeは等差数列のarrayを作成するメソッドです。

```python
>>> import numpy as np

>>> np.arange(3))
array([0, 1, 2])
```

Pythonでは四則演算子を繋げて書くことができます。

```python
>>> print(1-+1)
0

>>> print(1---+++1)
0

>>> print(1-+-1)
2
```

上記の法則はnumpy配列でも同様です。
下記は、`[0,1,2]`と`[0,1,2]`の足し算を難読化した例です。

```python
>>> import numpy as np
>>> x = np.arange(3)
>>> x-+-x
array([0, 2, 4])
```

NOTやマイナスの発生を加味して前から読み解いていきます。

```python
>>> x-+x
array([0, 0, 0])

>>> x-+~-x
array([1, 1, 1])

>>> x-+~--~+-x
array([0, 2, 4])

>>> x-+~--~+-~~++x
array([0, 2, 4])

>>> x-+~--~+-~~++~+-x
array([-1,  1,  3])
```

気付いてしまえば前から読み解くだけですが、頭の中で暗算していくのがちょっと難しい、そんな問題でした。
