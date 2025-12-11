let type = "type";
type type<type> = type extends type ? type : typeof type;

const a: type<"type"> = type;
const b: type<"type"> = "type";
const c: type<"type"> = typeof type;
const d: type<"type"> = typeof "type";
