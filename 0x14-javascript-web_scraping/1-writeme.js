#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.arg[2], process.arg[3], error => {
  if (error) console.log(error);
});
