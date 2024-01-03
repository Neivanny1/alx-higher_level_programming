#!/usr/bin/node
const request = require('request');
// Make a GET request and display the status code

request.get(process.argv[2], (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Code:', response.statusCode);
  }
});
