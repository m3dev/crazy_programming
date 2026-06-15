# 解説

```ruby
p|p|p
```

このコードの実行結果は `false` です。

## ポイント

`p` はおなじみのデバッグ出力メソッドですが、引数なしで呼ぶと動きが変わります。

### 引数なしの `p` は `nil` を返す

`Kernel#p` は引数を渡すとその値を出力して返しますが、**引数を1つも渡さないと何も出力せず `nil` を返します**。

ここでの `p` はいずれも引数なしなので、それぞれ `nil` と評価されます。

```ruby
p|p|p
# = nil | nil | nil
```

### `NilClass#|` の挙動

`|` はここではビット演算ではなく `NilClass#|` の呼び出しです。`nil | other` は、`other` が偽（`nil` または `false`）のとき `false` を、真のとき `true` を返します。

```ruby
nil | nil    # => false
```

左から評価していくと、

```ruby
nil | nil       # => false
false | nil     # => false （NilClass#| ではないが、FalseClass#| も other が偽なら false を返す）
```

いずれの段階でも右オペランドが `nil`（偽）なので、最終結果は `false` になります。

`p` が引数なしだと `nil` を返すこと、`|` が `nil`/`false` に対して論理演算メソッドとして働くことを問う問題でした。
