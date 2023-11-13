#!/usr/bin/node
const list = process.argv;
list.splice(0, 2);
const length = list.length;
let nextLargest = 0;

if (length === 0 || length === 1) {
  console.log('0');
} else {
  list.sort();
  nextLargest = list[length - 2];
  console.log(nextLargest);
}
