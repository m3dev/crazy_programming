# parse int radix

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

`toString` の基数引数がやけに長い式です。何が出力されるでしょう。

```javascript
parseInt("256", ~-16).toString(0+11..toString(16)+11000)
```

## 実行

```sh
nvm use
node -e 'console.log(parseInt("256", ~-16).toString(0+11..toString(16)+11000))'
```

## 解説

`explanation.md`で解説しています
