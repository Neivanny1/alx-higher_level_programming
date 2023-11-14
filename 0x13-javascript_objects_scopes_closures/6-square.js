#!/usr/bin/node
const SquareA = require('./5-square');

class Square extends SquareA {
  charPrint (c) {
    if (c === undefined) {
      return super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
