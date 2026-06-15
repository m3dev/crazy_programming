#!/usr/bin/env python3
"""M3 ロゴが空白として刻まれた Terraform Quine ジェネレータ (26 行 × 100 列).

26 行に詰めるため:
  - 1 行目: HCL プレフィックス + 第 1 要素 (data 53 chars)
  - 2-24 行目: 第 2-24 要素 (data 97 chars each)
  - 25 行目: 第 25 要素 (data 30 chars) + closing 第 1 部
  - 26 行目: closing 第 2 部 + コメントパディング

リスト要素は 25 個. m3_mask.txt 26 行のうち最終行 (sparse tagline) を捨て、
1 行目はマスクの右端 53 cell (col 45-97) を使う事で M3 ロゴが col 1 で揃う.

ランタイム動作 (locals 不使用、output 単体に for-comp の let-binding):
  1. `[for p in [join("\\n", [...])]` で 25 行を `\\n` で連結して `p` に bind
  2. `replace(p, "/[ \\n]/", "")` で空白と改行を regex で除去
  3. `split("@", ...)[0]` で base64(t) を取り出し、`base64decode` でテンプレ復元
  4. `join(",\\n", [for e in split("\\n", p) : "\\"${e}\\""])` で 25 個の HCL
     リスト要素表記を再構成
  5. `format(t, list_repr)` でソース全体を復元
"""
import base64
from pathlib import Path

HERE = Path(__file__).parent
MASK_FILE = HERE / "m3_mask.txt"
OUT_FILE = HERE / "main.tf"

DELIM = "@"
TARGET = 100

PREFIX = 'output "q" { value = [for p in [join("\\n", ['
CLOSING_PART1 = '])] : format(base64decode(split("@", replace(p, "/[ \\n]/", ""))[0]),'
ARG2 = 'join(",\\n", [for e in split("\\n", p) : "\\"${e}\\""])'
CLOSING_PART2 = f"{ARG2})][0] }}"

COMMENT = " # We are hiring!! - jobs.m3.com/engineer/"  # 42 chars

ROW26 = f"{CLOSING_PART2}{COMMENT}"
assert len(ROW26) == TARGET, f"row 26 length {len(ROW26)} != {TARGET}"

# Template t (decoded at runtime). %s is replaced by 25 list-element source lines:
#   "<row1>",\n"<row2>",\n..."<row25>"
T_VALUE = f"{PREFIX}%s{CLOSING_PART1}\n{ROW26}\n"


def main() -> None:
    mask_lines = MASK_FILE.read_text().splitlines()
    # 25 行使う (最終 26 行目は捨てる)
    mask_lines = mask_lines[:25]

    # 各 source 行で利用できる data 幅に従ってマスクを切り出す
    truncated = []
    truncated.append(mask_lines[0][44:97])  # 行 1: マスク col 45-97 (右 53 cell)
    for i in range(1, 24):
        truncated.append(mask_lines[i][:97])  # 行 2-24: 全 97 cell
    truncated.append(mask_lines[24][:30])  # 行 25: マスク col 1-30 (左 30 cell)

    mask_zero_count = sum(row.count("0") for row in truncated)

    t_b64 = base64.b64encode(T_VALUE.encode()).decode()

    needed = mask_zero_count - len(t_b64) - len(DELIM)
    if needed < 0:
        raise ValueError(
            f"Template too long: need {len(t_b64) + len(DELIM)} chars, "
            f"only {mask_zero_count} mask=0 cells available"
        )

    padding = (t_b64 * (needed // len(t_b64) + 1))[:needed]
    data = t_b64 + DELIM + padding
    assert len(data) == mask_zero_count

    row_contents = []
    idx = 0
    for row in truncated:
        chars = []
        for c in row:
            if c == "1":
                chars.append(" ")
            else:
                chars.append(data[idx])
                idx += 1
        row_contents.append("".join(chars))

    # Build list_elements: 前 24 個は trailing comma 付き、最後の 25 番目はカンマ無し
    elements = [f'"{c}",' for c in row_contents[:-1]] + [f'"{row_contents[-1]}"']
    list_elements = "\n".join(elements)

    source = T_VALUE % list_elements
    OUT_FILE.write_text(source)
    print(
        f"wrote {OUT_FILE} ({len(source)} chars, "
        f"{source.count(chr(10))} lines, "
        f"template b64 = {len(t_b64)} chars, padding = {needed} chars)"
    )


if __name__ == "__main__":
    main()
