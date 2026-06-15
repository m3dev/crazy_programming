# Terraform Quine

Terraform (HCL) で書かれた M3 ロゴ形状の Quine。

## 実行

```sh
terraform init
terraform apply -auto-approve
terraform output -raw q
```

## 検証

```sh
terraform output -raw q | diff - main.tf
```

## 作り方

`m3_mask.txt` (26 行 × 100 列の 0/1 bitmap) からマスクを読み込み`main.tf` を生成するスクリプトを実行

```sh
python generator.py
```

## 解説

### マスクの埋め込み方

1. ランタイム HCL コード本体をテンプレート `t` として用意
   - `format` の `%s` プレースホルダ 1 個を含む
2. `t` を base64 で符号化し、`base64(t) + "@" + パディング` を「データ」とする
3. マスクを 1 セルずつ走査し
   - マスク = 1 のセルには空白 (M3 ロゴが空白として浮かび上がる)
   - マスク = 0 のセルにはデータの次の 1 文字
4. 出来上がった各行を `"<row content>",` の HCL list 要素として並べる

### ランタイム (HCL) の動作

```hcl
output "q" {
  value = [for p in [join("\n", [<25 list elements>])] :
    format(
      base64decode(split("@", replace(p, "/[ \n]/", ""))[0]),
      join(",\n", [for e in split("\n", p) : "\"${e}\""])
    )
  ][0]
}
```

(実際には 26 行 × 100 列に圧縮済み)

1. `[for p in [join("\n", [<25 elements>])] : ...][0]` - 25 行のリストを `\n` で連結して `p` に let-bind し、最後に `[0]` で取り出す
2. `replace(p, "/[ \n]/", "")` - Terraform の `replace` の regex (`/.../`) で空白と改行を一発で除去
3. `split("@", ...)[0]` - `@` で分割して先頭 (base64(t)) を取得
4. `base64decode(...)` - テンプレート `t` を復元
5. `join(",\n", [for e in split("\n", p) : "\"${e}\""])` - `p` を再度list要素表記 (`"row1",\n"row2",\n...,\n"row25"`) に組み立て直す
6. `format(t, list_repr)` で `t` の `%s` にこの list 表記を差し込み、ソース全体を再生成

### Quine が成立する仕組み

復元される `t` の値は、ソースから 25 個の list 要素行を `%s` プレースホルダ
に置き換えたもの:

```hcl
output "q" { value = [for p in [join("\n", [%s])] : format(base64decode(split("@", replace(p, "/[ \n]/", ""))[0]),
join(",\n", [for e in split("\n", p) : "\"${e}\""]))][0] } # M3 Terraform Quine | We are hiring!! | ...
```

ここに 25 個分の list 要素表記 (`"row1",\n"row2",\n...\n"row25"`) を `%s` に差し込むと、`main.tf` 全体と一致する
