# 難読Rubyコードクイズ問題 in RubyWorldConference2022

- Author: [@Owl](https://github.com/owl-bo)

RubyWorldConference2022にてスポンサーブースで紹介した問題です。
以下のブログで解説しています。

- [難読RubyクイズReturns Day0 @RubyWorldConference2022 - エムスリーテックブログ](https://www.m3tech.blog/entry/2022/11/01/143000)
- [難読RubyクイズReturns Day1 & Day2 @RubyWorldConference2022 - エムスリーテックブログ](https://www.m3tech.blog/entry/2022/11/23/110000)

## requierments

irbを使い実行してください。

```sh
rbenv install
rbenv local
irb
```

## Quiz

### Day0 - 1. マイナスのマイナスは？

```ruby
-a=--1.to_s
```

### Day0 - 2. アンダースコアの意味

```ruby
[1_1, 1_2, 1_3].map{_2}|[]
```

### Day0 - 3. 綺麗で不可解で無意味

```ruby
_=_|_=__=_|_=_
```

### Day1 - 1

```ruby
!??[?!]
!??[??]
```

### Day1 - 2

```ruby
!%.!..!
```

### Day1 - 3

```ruby
?%%/?%/
```

### Day2 - 1

```ruby
+-+-+-1===-+-+-+1
```

### Day2 - 2

```ruby
().|(0).!()
```

### Day2 - 3

```ruby
(?a..?A).to_a[-2]
```
