# Python Quine

以下2つのQuineを含んでいます。

- シンプルなPython Quine
  - Author: [@Hi-king](https://github.com/Hi-king)
- 「M3」→「福岡」→「積極」→「採用」→「M3」のように出力が変化、ループするQuine
  - Author: [@ujiuji1259](https://github.com/ujiuji1259)

## 実行

シンプルなPython Quineの実行

```sh
uv run python quine.py
```

出力が変化、ループするQuineの実行

```sh
SRC="fukuoka_quine.py"
TMP="fukuoka_quine.tmp"
while true; do
    if uv run python "$SRC" | tee "$TMP"; then
        mv "$TMP" "$SRC"
    fi
    sleep 1
done
```

## 解説

以下2つのブログで実装方法を解説しています。

- [エムスリーが難読プログラミングオタクに送るノベルティ、Python Quineクリアファイルの作り方 - エムスリーテックブログ](https://www.m3tech.blog/entry/python_quine)
- [エムスリー福岡Quineを作りました！ - エムスリーテックブログ](https://www.m3tech.blog/entry/2024/11/07/110000)
