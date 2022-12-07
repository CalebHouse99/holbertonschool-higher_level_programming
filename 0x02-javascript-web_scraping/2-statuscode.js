#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (err, data) {
  if (err) throw err;
  console.log(`code: ${data.statusCode}`);
});
