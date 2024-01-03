#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number
const request = require('request');
let count = 0;

request(process.argv[2], function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        count += 1;
      }
    }
  }

  console.log(count);
});
