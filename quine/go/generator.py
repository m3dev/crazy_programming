#!/usr/bin/env python3
from base64 import b64encode
from pathlib import Path

MASK_FILE = Path("m3_mask.txt")
OUT_FILE = Path("main.go")
DELIM = "::M3::"
WIDTH = 100


def load_mask():
    lines = MASK_FILE.read_text().splitlines()
    bits = []
    for line in lines:
        bits.extend(0 if c == "0" else 1 for c in line.strip())
    return bits


def pack_bits(bits):
    packed = []
    for i in range(0, len(bits), 8):
        chunk = bits[i : i + 8]
        while len(chunk) < 8:
            chunk.append(0)
        byte = 0
        for b in chunk:
            byte = (byte << 1) | b
        packed.append(byte)
    return b64encode(bytes(packed)).decode()


def apply_required_spaces(bits, full, rows=4):
    """上部4行のGo構文で必須な空白をマスクに反映"""
    limit = min(len(bits), WIDTH * rows)
    bits = bits[:]
    for pos in range(limit):
        bits[pos] = 0
    return bits


def build_template(mask_b64: str, pad: int):
    base = (
        'package main;import(b"encoding/base64";f"fmt";s"strings");'
        "func main() {r:=s.ReplaceAll(s.ReplaceAll(p,\" \",\"\"),\"\\n\",\"\");"
        'u:=s.SplitN(r,"::M3::",2);d:=b.StdEncoding.DecodeString;'
        "t,_:=d(u[0]);m,_:=d(u[1]);q:=f.Sprintf(string(t),r);i:=0;"
        "for n:=0;n<2600;n++{if n>0&&n%%100==0{f.Println()}; x:=m[n/8];"
        "b:=(x>>(7-uint(n%%8)))&1;if b==1{f.Print(\" \")}"
        "else{f.Printf(\"%%c\",q[i]);i++}};f.Println();};"
        "const p=`%s`"
    )
    tmpl = base + (" " * pad)
    code_b64 = b64encode(tmpl.encode()).decode()
    payload = code_b64 + DELIM + mask_b64
    full = tmpl.replace("%s", payload, 1).replace("%%", "%")
    return tmpl, full


def find_padding(bits, mask_b64, max_pad=20000):
    zeros = len(bits) - sum(bits)
    for pad in range(max_pad):
        _, full = build_template(mask_b64, pad)
        if len(full) == zeros:
            return pad, full
    raise RuntimeError(f"pad not found up to {max_pad}, zeros={zeros}")


def shape_source(bits, full):
    out = []
    idx = 0
    for pos, bit in enumerate(bits):
        if bit == 1:
            out.append(" ")
        else:
            out.append(full[idx])
            idx += 1
        if (pos + 1) % WIDTH == 0:
            out.append("\n")
    if idx != len(full):
        raise RuntimeError("mask/code length mismatch")
    return "".join(out)


def main():
    bits = load_mask()
    # Pass1: provisional full (pad=0) -> mask override on top rows
    mask_b64 = pack_bits(bits)
    _, full0 = build_template(mask_b64, 0)
    bits = apply_required_spaces(bits, full0, rows=4)

    # Pass2: find padding with updated mask
    mask_b64 = pack_bits(bits)
    pad, full = find_padding(bits, mask_b64)

    # Pass3: align mask to the final full (stabilize top rows) and refind
    bits = apply_required_spaces(bits, full, rows=4)
    mask_b64 = pack_bits(bits)
    pad, full = find_padding(bits, mask_b64)

    shaped = shape_source(bits, full)
    OUT_FILE.write_text(shaped)
    print(f"pad={pad} chars, code_len={len(full)}, zeros={len(bits)-sum(bits)}")
    print(f"wrote {OUT_FILE} ({len(shaped)} chars including newlines)")


if __name__ == "__main__":
    main()

