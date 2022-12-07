#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  const tasks = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (tasks[task.userId]) {
        tasks[task.userId]++;
      } else {
        tasks[task.userId] = 1;
      }
    }
  }
  console.log(tasks);
});
