#!/usr/bin/node
function add (a, b) {
  if (parseInt(a) && parseInt(b)) {
    console.log(parseInt(a) + parseInt(b));
  } else {
    console.log('NaN');
  }
}
add(process.argv[2], process.argv[3]);
