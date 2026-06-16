# Colab Encode

Author: [@vaaaaanquish](https://github.com/vaaaaanquish)

サポーターズ株式会社が運営するColab Conf 2025に向けて作成した問題です。`"Colab"` を渡すと何が出力されるでしょう。

```javascript
((s,[a,b,c,d,e]=new TextEncoder().encode(s))=>String.fromCharCode(a+c-e)+(b-c))("Colab")
```

## 実行

```sh
nvm use
node -e 'console.log(((s,[a,b,c,d,e]=new TextEncoder().encode(s))=>String.fromCharCode(a+c-e)+(b-c))("Colab"))'
```

## 解説

`explanation.md`で解説しています
