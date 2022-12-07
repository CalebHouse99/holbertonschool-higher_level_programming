#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    let i = 0;
    for (const title in data) {
      const chars = data[title].characters;
      for (const char in chars) {
        if (chars[char].includes('/18/')) {
          i++;
        }
      }
    }
    console.log(i);
  }
});
