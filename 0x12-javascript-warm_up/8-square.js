#!/usr/bin/node
/* print square using numbers of arg */
const argvTwo = parseInt(process.argv[2]);
let s;
if (!argvTwo) {
  console.log('missing size');
}
for (let i = 0; i < argvTwo; i++) {
  s = '';
  for (let j = 0; j < argvTwo; j++) {
    s += 'X';
  }
  console.log(s);
}
