#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (error, response, body) => {
  if (error) throw error;
  fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) throw err;
  });
});
