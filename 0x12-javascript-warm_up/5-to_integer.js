#!/usr/bin/node
/* convert argument to integer */
const argTwo = Number(process.argv[2]);
if (!argTwo) {
  console.log('Not a number');
}
console.log(`My number: ${argTwo}`);
