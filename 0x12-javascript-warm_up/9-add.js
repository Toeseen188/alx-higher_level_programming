#!/usr/bin/node
/* add argv[2] and argv[3] */
function add (a, b) {
  return a + b;
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
const result = add(a, b);
console.log(result);
