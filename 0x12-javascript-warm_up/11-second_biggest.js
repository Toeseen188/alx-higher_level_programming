#!/usr/bin/node
/* find the second biggest number in argv */
const len = process.argv.length;
if (len <= 3) {
  console.log('0');
} else {
  const args = process.argv.map(Number)
    .slice(2, len)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
