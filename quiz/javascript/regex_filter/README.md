# regex filter

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

同じ正規表現でフィルタしているのに、配列の順番で結果が変わります。それぞれ何が出力されるでしょう。

```javascript
(r => ["3M", "M3"].filter(s => r.test(s)))(/[0-9]+/g)
(r => ["M3", "3M"].filter(s => r.test(s)))(/[0-9]+/g)
```

## 実行

```sh
nvm use
node -e 'console.log((r => ["3M", "M3"].filter(s => r.test(s)))(/[0-9]+/g))'
node -e 'console.log((r => ["M3", "3M"].filter(s => r.test(s)))(/[0-9]+/g))'
```

## 解説

`explanation.md`で解説しています
