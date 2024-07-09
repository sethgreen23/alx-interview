#!/usr/bin/node

const request = require('request');

function promisifyRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(body);
    });
  });
}
async function getCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  try {
    const response = await promisifyRequest(url);
    const characters = JSON.parse(response).characters;
    const charactersList = characters.map(async (characterLink) => {
      const characterResponse = await promisifyRequest(characterLink);
      return JSON.parse(characterResponse).name;
    });
    const charactersBodie = await Promise.all(charactersList);
    charactersBodie.forEach((character) => {
      console.log(character);
    });
  } catch (err) {
    console.log(err);
  }
}

const movieId = process.argv[2];
getCharacters(movieId);
