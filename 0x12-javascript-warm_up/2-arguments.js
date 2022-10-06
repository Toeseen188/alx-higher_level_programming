#!/usr/bin/node
/* Script that print to console based on the number of arguments */
const numArg = process.argv.length;

if (numArg <= 2) {
  console.log('No argument');
} else if (numArg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
