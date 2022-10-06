#!/usr/bin/node
/* Script that print to console based on the number of arguments */
const numArg = process.argv.length;

if (numArg <= 2) {
  console.log('No arguments');
} else {
  console.log('Arguments found');
}
