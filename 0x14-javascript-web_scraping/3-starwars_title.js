#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request('http://swapi.co/api/films/' + id + '/', function (error, response, body) {
  if (error) console.log(error);
  else {
    console.log(JSON.parse(body).title);
  }
});
