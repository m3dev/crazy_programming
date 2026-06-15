# undefined label

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

`eval`の中身はオブジェクトリテラルでしょうか。何が出力されるでしょう。

```javascript
eval("{undefined:[1]}['undefined'][0]")
```

## 実行

```sh
nvm use
node -e "console.log(eval(\"{undefined:[1]}['undefined'][0]\"))"
```

## 解説

`explanation.md`で解説しています
