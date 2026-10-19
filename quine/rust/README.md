# Rust Quine

Author: [@inakam00](https://github.com/inakam00)

m3ロゴの形をしたRust言語のQuine。標準ライブラリだけで動作し、ソースファイルの読み込みは行いません。

以下の2種類があります。

- `with-comments/`：`fn/**/main`のようなコメントでトークンを区切り、`m3_mask.txt`の空白配置をそのまま使う版
- `comment-free/`：コメントを使わず、コードの区切りに必要な空白をマスクに足した版

## 実行

```sh
cd with-comments # または cd comment-free
rustc --edition=2024 quine.rs
./quine
```

## ジェネレータ

以下のファイルで、オリジナルのRust Quineを作成できます。

- `m3_mask.txt`：0/1でロゴを定義したマスク（0: コード、1: 空白）。2つの版で共通
- `template.rs`：読みやすく整形した生成元
- `generate.py`：生成元を`m3_mask.txt`のロゴ形状に配置し、`quine.rs`を書き出すスクリプト。末尾の採用メッセージは`FOOTER`で指定する

```sh
cd with-comments # または cd comment-free
python3 generate.py
```

以下のような形で開発しています。

1. `m3_mask.txt`でロゴの形を、`template.rs`でコードを編集する（末尾の`@`は生成時に自分自身の文字列で置き換わる）
2. `generate.py`を実行して`quine.rs`を生成
3. 生成された`quine.rs`を実行し、出力が`quine.rs`と一致することを確認

```sh
rustc --edition=2024 quine.rs
./quine | cmp - quine.rs
```

## 解説

[Rustで自己言及プログラムであるQuineを作っていく](https://www.m3tech.blog/entry/rust-quine-m3)にて解説しています。
