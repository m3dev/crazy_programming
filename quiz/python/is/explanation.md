# 解説

第10問は、記念すべき10問目に相応しく、普通には読めない系の難読クイズです。

//list[v-quiz-10][Python難読クイズ10 - is...][python]{
...is...is...is...is...is...
//}

//noindent
普段からnumpyを直に書いていたり、Python Packageを作成している方には見慣れた表現やもしれません。
@<code>{...}というEllipsisオブジェクトを知っているかが鍵になってきます。
さっそく解説を見ていきます。

//list[v-quiz-10-ans][Python難読クイズ10 - 解説][python]{
# Ellipsisは省略表記のオブジェクトです
print(...)  # Ellipsis

# numpyなどではよくスライス時に省略表記として使われます
import numpy
x = numpy.array([[1, 2], [3, 4]])
print(x[1, ...])  # [3, 4]

# Ellipsisはbool値としてはTrueです
print(bool(...))  # True

# Ellipsisの比較もTrueになります
print(...is...)  # True
//}

//noindent
というわけで、@<code>{...is...is...is...is...is...}は@<code>{True}なのでした。
見慣れないコードで、なんじゃこりゃと思われた方も多かったようです。

Xで先に気付かれた方もいるのですが、この問題は様々なEllipsis実装を考えるのに適した問題です。
例えば、次のような拡張問題が考えられます。
