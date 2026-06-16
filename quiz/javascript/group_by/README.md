# group by

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

`M` で始まる単語を `Object.groupBy` でまとめています。何が出力されるでしょう。

```javascript
Object.entries(Object.groupBy(["Medicine","Media","Metamorphosis"],([m]) => m))[0].map(m=>Array.isArray(m)?m.length:m).join("")
```

## 実行

```sh
nvm use
node -e 'console.log(Object.entries(Object.groupBy(["Medicine","Media","Metamorphosis"],([m]) => m))[0].map(m=>Array.isArray(m)?m.length:m).join(""))'
```

## 解説

`explanation.md`で解説しています
