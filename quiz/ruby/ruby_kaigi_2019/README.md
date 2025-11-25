# 難読Rubyコードクイズ問題 in RubyKaigi 2019

- Author: [@Owl](https://github.com/owl-bo)

RubyKaigi 2019にてスポンサーブースで紹介した問題です。
以下のブログで解説しています。

- [難読Rubyコードクイズ問題と解説 in RubyKaigi 2019 - エムスリーテックブログ](https://www.m3tech.blog/entry/2019/04/25/123843)

## requierments

irbを使い実行してください。

```sh
rbenv install
rbenv local
irb
```

## quiz

### Day1 - 1

```ruby
!????!:!?!
```

### Day2 - 1

```ruby
%%%%%%..%%[0].size[0]
```

### Day3 - 1

```ruby
puts = :puts
puts = send(puts, puts) || puts(puts) { puts = “puts” }
puts
```

### Day3 - 2

```ruby
%%%%%%%%?????:??
```

### Day3 - 3

```ruby
a = 0.0/0; a == a ? a : irb.quit
```
