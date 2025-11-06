#use "topfind";;#require "zstd";;#require "base64";;#require "compiler-libs";;open Printf;;open String;;

let read_file filename =
  let chan = open_in filename in
  let len = in_channel_length chan in
  let content = really_input_string chan len in
  close_in chan;
  content
;;

let () =
  let code = read_file "base.ml" in
  let len = String.length code in
  let input = (if len > 0 && code.[len - 1] = '\n' then String.sub code 0 (len - 1) else code) in
  let enc = Base64.encode_exn input in
  print_endline enc
