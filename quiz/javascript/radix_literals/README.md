# radix literals

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

同じ見た目の数を、リテラルとして足す場合と `parseInt` で足す場合で結果が変わります。それぞれ何が出力されるでしょう。

```javascript
010 + 0b10 + 0o10 + 0x10
parseInt("010") + parseInt("0b10") + parseInt("0o10") + parseInt("0x10")
```

## 実行

```sh
nvm use
node -e 'console.log(010 + 0b10 + 0o10 + 0x10)'
node -e 'console.log(parseInt("010") + parseInt("0b10") + parseInt("0o10") + parseInt("0x10"))'
```

## 解説

`explanation.md`で解説しています
