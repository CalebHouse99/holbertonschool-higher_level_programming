#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const list = process.argv.slice(2);
  list.sort(function (a, b) {
    return a - b;
  });
  list.reverse();
  console.log(list[1]);
}
