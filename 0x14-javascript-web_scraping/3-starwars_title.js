#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number
// matches a given integer
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected response status code:', response.statusCode);
  } else {
    console.log('Response body:', body); // Log the entire response body for inspection
    try {
      const data = JSON.parse(body);
      console.log('Title:', data['title']);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  }
});
