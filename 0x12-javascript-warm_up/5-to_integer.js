#!/usr/bin/node
/* convert argument to integer */
const argTwo = parseInt(process.argv[2]);
if (argTwo) {
  console.log(`My Number: ${argTwo}`);
} else {
  console.log('Not a number');
}