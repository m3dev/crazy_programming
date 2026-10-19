fn main() {
    let payload = P.split_whitespace().collect::<String>();
    let mut parts = payload.rsplitn(3, '~');
    parts.next();
    let runs = parts.next().unwrap().as_bytes().chunks(2)
        .map(|n| 26 * usize::from(n[0] - b'A') + usize::from(n[1] - b'A'));
    let template = parts.next().unwrap().replace('\x24', "\x23");
    let (head, tail) = template.rsplit_once('@').unwrap();
    let source = [head, &payload, tail].concat();
    let mut text = source.chars();
    let mut out = String::new();
    let mut space = false;
    for len in runs {
        for _ in 0..len {
            out.push(if space { '\x20' } else { text.next().unwrap() });
            if out.len() % 101 == 100 {
                out.push('\n');
            }
        }
        space = !space;
    }
    print!("{out}");
}
const P: &str = r#"@"#;
