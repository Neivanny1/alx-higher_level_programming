#!/usr/bin/node
const myString = 'C is fun';
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(myString);
  }
}
