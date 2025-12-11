import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { styleText } from "node:util";

const sourcecode = await readFile(
  new URL("./quine.ts", import.meta.url),
  "utf8"
).then((data) => data.trim());

const buffer = execFileSync("node", ["./src/quine.ts"]);
const output = Buffer.from(buffer).toString("utf-8").trim();

console.log(styleText(["blue"], "------------------------------"));
console.log(styleText(["blue"], sourcecode));
console.log(styleText(["blue"], "------------------------------"));
console.log(styleText(["blue"], output));
console.log(styleText(["blue"], "------------------------------"));
console.log(
  output === sourcecode
    ? styleText(["bold", "bgGreen"], " OK! ")
    : styleText(["bold", "bgRed"], " NG........ ")
);
