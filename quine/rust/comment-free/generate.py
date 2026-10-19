"""Rustのトークン境界を保ち、ロゴの空白配置にコメントなしで自己複製コードを配置する。"""

from itertools import groupby
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
MASK = ROOT.parent / "m3_mask.txt"
FOOTER = "We are hiring !! https://jobs.m3.com/engineer/ ======================="
TOKEN = re.compile(r'''b?"(?:\\.|[^"\\])*"|b?'(?:\\.|[^'\\])*'|[A-Za-z_]\w*|\d+|::|->|=>|\.\.|&&|==|!=|\+=|[^\s]''')


def generate() -> str:
    layout = MASK.read_text().replace("0", "x").replace("1", " ")
    canvas = list(layout)
    prefix = (ROOT / "template.rs").read_text().split('r#"@"#;')[0]
    tokens = TOKEN.findall(prefix) + ['r#"']
    cursor = 0
    previous = ""
    for token in tokens:
        if re.search(r"\w$", previous) and re.match(r"\w", token):
            if cursor < len(canvas) and not canvas[cursor].isspace():
                canvas[cursor] = " "
            cursor += 1
        while cursor + len(token) <= len(canvas):
            if all(not c.isspace() for c in canvas[cursor:cursor + len(token)]):
                break
            if not canvas[cursor].isspace():
                canvas[cursor] = " "
            cursor += 1
        else:
            raise ValueError("トークンをロゴ内に配置できません")
        cursor += len(token)
        previous = token

    positions = [i for i, c in enumerate(canvas) if not c.isspace()]
    packed = "".join(tokens)
    template = (packed + '@"#;').replace("#", "$")
    footer = "".join(FOOTER.split())
    runs = ""
    for _, group in groupby("".join(canvas).replace("\n", ""), key=lambda c: c == " "):
        high, low = divmod(sum(1 for _ in group), 26)
        runs += chr(ord("A") + high) + chr(ord("A") + low)
    padding = len(positions) - (2 * len(template) - 1 + len(runs) + 2 + len(footer))
    if padding < 0:
        raise ValueError(f"文字数が{-padding}文字超過しています")
    payload = template + "~" + runs + "~" + "=" * padding + footer
    compact = packed + payload + '"#;'
    result = canvas
    for position, character in zip(positions, compact):
        result[position] = character
    assert len(compact) == len(positions)
    prefix, tail = "".join(result).rsplit("~", 1)
    fill, footer = tail.split("\n", 1)
    fill = ("M3" * ((len(fill) + 1) // 2))[:len(fill)]
    return prefix + "~" + fill + "\n" + footer


if __name__ == "__main__":
    (ROOT / "quine.rs").write_text(generate())
