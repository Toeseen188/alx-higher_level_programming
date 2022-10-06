#!/usr/bin/node
/* print 'C is fun' x number of times,
 * where x is argv[2]
 */
const argvTwo = parseInt(process.argv[2]);
if (!argvTwo) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < argvTwo; i++) {
  console.log('C is fun');
}
