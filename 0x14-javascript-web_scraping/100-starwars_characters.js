#!/usr/bin/node

const req = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

req.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const i of characters) {
    req(i, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const chardata = JSON.parse(body);
      console.log(chardata.name);
    });
  }
});
