#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number
// matches a given integer
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data['title']);
  }
});
