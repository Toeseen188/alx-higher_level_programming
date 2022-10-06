#!/usr/bin/node
/* factorial */
const argv = parseInt(process.argv[2]);
function factorial (a) {
  if (isNaN(a) || a <= 0) {
    return 1;
  }
  return factorial(a - 1) * a;
}
console.log(factorial(argv));
