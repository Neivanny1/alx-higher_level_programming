#!/usr/bin/node
// Write the string to the file in utf-8
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
