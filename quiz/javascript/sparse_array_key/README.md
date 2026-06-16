# sparse array key

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

`[[,,]]` が並んでいますが、何が出力されるでしょう。

```javascript
x = {[[,,]]:[[,,]]}
y = JSON.stringify(x)
console.log(y)
```

## 実行

```sh
nvm use
node -e "x = {[[,,]]:[[,,]]}; y = JSON.stringify(x); console.log(y)"
```

## 解説

`explanation.md`で解説しています
