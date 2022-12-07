#!/usr/bin/node
// File System Object
const fs = require("fs");
// Read File
fs.readFile(process.argv[2], "utf8", function (err, data) {
  err ? Function("error", "throw error")(err) : console.log(data);
});
