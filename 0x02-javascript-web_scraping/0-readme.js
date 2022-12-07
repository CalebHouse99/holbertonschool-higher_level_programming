#!/usr/bin/node
// File System Object
const fs = require('fs');
// Read File
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
