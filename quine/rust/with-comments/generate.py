"""Rustのトークン境界を保ち、元の空白配置に自己複製コードを配置する。"""

from functools import lru_cache
from itertools import groupby
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
MASK = ROOT.parent / "m3_mask.txt"
FOOTER = "We are hiring !! https://jobs.m3.com/engineer/ ======================="
TOKEN = re.compile(r'''b?"(?:\\.|[^"\\])*"|b?'(?:\\.|[^'\\])*'|[A-Za-z_]\w*|\d+|::|->|=>|\.\.|&&|==|!=|\+=|[^\s]''')


def generate() -> str:
    layout = MASK.read_text().replace("0", "x").replace("1", " ")
    positions = [i for i, c in enumerate(layout) if not c.isspace()]
    prefix = (ROOT / "template.rs").read_text().split('r#"@"#;')[0]
    tokens = TOKEN.findall(prefix)
    separated = []
    for token in tokens:
        if separated and re.search(r"\w$", separated[-1]) and re.match(r"\w", token):
            separated.append("/**/")
        separated.append(token)
    separated.append('r#"')

    def fits(start: int, size: int) -> bool:
        return start + size <= len(positions) and positions[start + size - 1] - positions[start] == size - 1

    @lru_cache(None)
    def place(index: int, offset: int):
        if index == len(separated):
            return ""
        token = separated[index]
        candidates = []
        for padding in [0, *range(4, 105)]:
            if padding and not (fits(offset, 2) and fits(offset + padding - 2, 2)):
                continue
            if not fits(offset + padding, len(token)):
                continue
            suffix = place(index + 1, offset + padding + len(token))
            if suffix is not None:
                comment = "/*" + "_" * (padding - 4) + "*/" if padding else ""
                candidates.append(comment + token + suffix)
                if padding == 0:
                    break
        return min(candidates, key=len) if candidates else None

    packed = place(0, 0)
    if packed is None:
        raise ValueError("トークンを固定レイアウトに配置できません")
    template = (packed + '@"#;').replace("#", "$")
    footer = "".join(FOOTER.split())
    runs = ""
    for _, group in groupby(layout.replace("\n", ""), key=lambda c: c == " "):
        high, low = divmod(sum(1 for _ in group), 26)
        runs += chr(ord("A") + high) + chr(ord("A") + low)
    padding = len(positions) - (2 * len(template) - 1 + len(runs) + 2 + len(footer))
    if padding < 0:
        raise ValueError(f"文字数が{-padding}文字超過しています")
    payload = template + "~" + runs + "~" + "=" * padding + footer
    compact = packed + payload + '"#;'
    result = list(layout)
    for position, character in zip(positions, compact):
        result[position] = character
    assert len(compact) == len(positions)
    prefix, tail = "".join(result).rsplit("~", 1)
    fill, footer = tail.split("\n", 1)
    fill = ("M3" * ((len(fill) + 1) // 2))[:len(fill)]
    return prefix + "~" + fill + "\n" + footer


if __name__ == "__main__":
    (ROOT / "quine.rs").write_text(generate())
